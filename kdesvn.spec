Summary:	kdesvn is yet another client for subversion
Name:		kdesvn
Version:	0.14.1
Release:	%mkrel 2
License:	GPLv2
Group:		Graphical desktop/KDE
Url:		http://kdesvn.alwins-world.de/
Source0:	http://www.alwins-world.de/programs/download/kdesvn/0.13.x/%{name}-%{version}.tar.bz2
Requires:	graphviz
BuildRequires:	cmake
BuildRequires:	kdelibs-devel 
BuildRequires:	subversion-devel >= 1.2
BuildRequires:	neon-devel
BuildRequires:	apr-devel
BuildRequires:	desktop-file-utils
Requires:       iceauth 

%description
kdesvn is yet another client for subversion. But it uses native 
KDE API instead of a extra lib like GAMBAS and it is using the 
native subversion delevelopment API instead of just parsing the 
output of the commandline tool like most other clients do. It tries 
to setup a look and feel like the standard filemanager of KDE and is 
integrated into it via KPart.
The base C++ interface to subversion I took from the (real great) tool 
Rapidsvn (see http://rapidsvn.tigris.org/) with some modifcations and fixes.

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root,-)
%doc README AUTHORS COPYING ChangeLog
%_bindir/*
%_libdir/kde3/*
%_datadir/apps/kdesvn
%_datadir/apps/kdesvnpart
%_datadir/apps/kconf_update/*
%_datadir/apps/konqueror/servicemenus/kdesvn_subversion.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/applications/kde/kdesvn.desktop
%_datadir/config.kcfg/*
%_datadir/services/*.protocol
%_datadir/services/kded/kdesvnd.desktop
%_mandir/man1/*

#-----------------------------------------------------------------

%define lib_svn_qt_major 4
%define lib_svn_qt %mklibname svnqt %lib_svn_qt_major

%package -n %lib_svn_qt
Summary:	KDE Svn core library
Group:		Graphical desktop/KDE
Obsoletes: %mklibname svnqt 1
Obsoletes: %mklibname svnqt 2
Obsoletes: %mklibname svnqt 3

%post -n %lib_svn_qt -p /sbin/ldconfig
%postun -n %lib_svn_qt -p /sbin/ldconfig

%description -n %lib_svn_qt
KDE Svn core library

%files -n %lib_svn_qt
%defattr(-,root,root,-)
%_libdir/*.so.%{lib_svn_qt_major}*

#-----------------------------------------------------------------

%package devel
Summary:	kdesvn devel package
Group:		Development/KDE and Qt
Requires:	%lib_svn_qt = %version-%release

%description devel
kdesvn devel package

%files devel 
%defattr(-,root,root,-)
%_includedir/*
%_libdir/*.so

#-----------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make

%install
rm -rf %{buildroot}

cd build
%makeinstall_std
cd -

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications/kde/ \
	--add-category='RevisionControl' \
	%buildroot%_datadir/applications/kde/kdesvn.desktop

%find_lang %{name} --with-html

%clean
rm -rf %{buildroot}
