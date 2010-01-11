Summary:	KDE client for subversion
Name:		kdesvn
Version:	1.5.0
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kdesvn.alwins-world.de/
Source:		http://kdesvn.alwins-world.de/downloads/%name-%version.tar.bz2
Requires:	graphviz
BuildRequires:	kdelibs4-devel
BuildRequires:	subversion-devel >= 1.5
Requires:	cervisia >= 1:4.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
kdesvn is yet another client for subversion. But it uses native 
KDE API instead of a extra lib like GAMBAS and it is using the 
native subversion delevelopment API instead of just parsing the 
output of the commandline tool like most other clients do. It tries 
to setup a look and feel like the standard filemanager of KDE and is 
integrated into it via KPart.
The base C++ interface to subversion I took from the (real great) tool 
Rapidsvn (see http://rapidsvn.tigris.org/) with some modifcations and fixes.

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog
%_kde_bindir/*
%_kde_libdir/kde4/*
%_kde_datadir/apps/kdesvn
%_kde_datadir/apps/kdesvnpart
%_kde_datadir/apps/kconf_update/*
%_kde_iconsdir/hicolor/*/*/*
%_kde_datadir/applications/kde4/kdesvn.desktop
%_kde_datadir/config.kcfg/*
%_kde_services/ServiceMenus/kdesvn_subversion.desktop
%_kde_services/ServiceMenus/kdesvn_subversion_toplevel.desktop
%_kde_services/kded/kdesvnd.desktop
%_kde_services/kdesvnpart.desktop
%_kde_services/ksvn*.protocol
%_mandir/man1/*

#-----------------------------------------------------------------

%define lib_svn_qt_major 6
%define lib_svn_qt %mklibname svnqt4_ %lib_svn_qt_major

%package -n %lib_svn_qt
Summary:   KDE Svn core library
Group:     System/Libraries
Obsoletes: %mklibname svnqt 1
Obsoletes: %mklibname svnqt 2
Obsoletes: %mklibname svnqt 3
Obsoletes: %{mklibname svnqt_ 5} < %version

%if %mdkversion < 200900
%post -n %lib_svn_qt -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %lib_svn_qt -p /sbin/ldconfig
%endif

%description -n %lib_svn_qt
KDE Svn core library

%files -n %lib_svn_qt
%defattr(-,root,root,-)
%_kde_libdir/*.so.%{lib_svn_qt_major}*

#-----------------------------------------------------------------

%package devel
Summary:	Kdesvn devel package
Group:		Development/KDE and Qt
Requires:	%lib_svn_qt = %version-%release

%description devel
kdesvn devel package

%files devel 
%defattr(-,root,root,-)
%_kde_includedir/*
%_kde_libdir/*.so
%_datadir/dbus-1/interfaces/org.kde.kdesvnd.xml

#-----------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{name} --with-html

# fwang: conflicts with cervisia
rm -f %buildroot%_kde_services/svn*.protocol

%clean
rm -rf %{buildroot}
