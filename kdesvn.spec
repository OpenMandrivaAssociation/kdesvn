Summary:	KDE client for subversion
Name:		kdesvn
Version:	0.14.6
Release:	%mkrel 1
License:	GPLv2
Group:		Graphical desktop/KDE
Url:		http://kdesvn.alwins-world.de/
Source:		http://kdesvn.alwins-world.de/trac.fcgi/downloads/%name-%version.tar.bz2
Requires:	graphviz
BuildRequires:	cmake
BuildRequires:	kdelibs-devel 
BuildRequires:	subversion-devel >= 1.2
BuildRequires:	neon-devel
BuildRequires:	apr-devel
BuildRequires:	desktop-file-utils
Requires:       iceauth 
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
%doc README AUTHORS COPYING ChangeLog
%_kde3_bindir/*
%_kde3_libdir/kde3/*
%_kde3_datadir/apps/kdesvn
%_kde3_datadir/apps/kdesvnpart
%_kde3_datadir/apps/kconf_update/*
%_kde3_datadir/apps/konqueror/servicemenus/kdesvn_subversion.desktop
%_kde3_iconsdir/hicolor/*/*/*
%_kde3_datadir/applications/kde/kdesvn.desktop
%_kde3_datadir/config.kcfg/*
%_kde3_datadir/services/*.protocol
%_kde3_datadir/services/kded/kdesvnd.desktop
%_kde3_mandir/man1/*

#-----------------------------------------------------------------

%define lib_svn_qt_major 4
%define lib_svn_qt %mklibname svnqt %lib_svn_qt_major

%package -n %lib_svn_qt
Summary:   KDE Svn core library
Group:     System/Libraries
Obsoletes: %mklibname svnqt 1
Obsoletes: %mklibname svnqt 2
Obsoletes: %mklibname svnqt 3

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
%_kde3_libdir/*.so.%{lib_svn_qt_major}*

#-----------------------------------------------------------------

%package devel
Summary:	Kdesvn devel package
Group:		Development/KDE and Qt
Requires:	%lib_svn_qt = %version-%release

%description devel
kdesvn devel package

%files devel 
%defattr(-,root,root,-)
%_kde3_includedir/*
%_kde3_libdir/*.so

#-----------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_kde3_prefix}
%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd -

desktop-file-install --vendor='' \
	--dir=%buildroot%_kde3_datadir/applications/kde/ \
	--add-category='RevisionControl' \
	%buildroot%_kde3_datadir/applications/kde/kdesvn.desktop

%find_lang %{name} --with-html

%clean
rm -rf %{buildroot}
