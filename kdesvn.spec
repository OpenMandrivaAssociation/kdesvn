Summary:	KDE client for subversion
Name:		kdesvn
Version:	1.6.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kdesvn.alwins-world.de/
Source0:	http://kdesvn.alwins-world.de/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	subversion-devel
Requires:	cervisia
Requires:	graphviz

%description
kdesvn is yet another client for subversion. But it uses native 
KDE API instead of a extra lib like GAMBAS and it is using the 
native subversion delevelopment API instead of just parsing the 
output of the commandline tool like most other clients do. It tries 
to setup a look and feel like the standard filemanager of KDE and is 
integrated into it via KPart.
The base C++ interface to subversion I took from the (real great) tool 
Rapidsvn (see http://rapidsvn.tigris.org/) with some modifcations and fixes.

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/svnqt
%{_kde_appsdir}/kdesvn
%{_kde_appsdir}/kdesvnpart
%{_kde_appsdir}/kconf_update/*
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_applicationsdir}/kdesvn.desktop
%{_kde_datadir}/config.kcfg/*
%{_kde_services}/ServiceMenus/kdesvn_subversion.desktop
%{_kde_services}/ServiceMenus/kdesvn_subversion_toplevel.desktop
%{_kde_services}/kded/kdesvnd.desktop
%{_kde_services}/kdesvnpart.desktop
%{_kde_services}/ksvn*.protocol
%{_mandir}/man1/*

#-----------------------------------------------------------------

%define lib_svn_qt_major 7
%define lib_svn_qt %mklibname svnqt4_ %{lib_svn_qt_major}

%package -n %{lib_svn_qt}
Summary:	KDE Svn core library
Group:		System/Libraries

%description -n %{lib_svn_qt}
KDE Svn core library

%files -n %{lib_svn_qt}
%{_kde_libdir}/*.so.%{lib_svn_qt_major}*

#-----------------------------------------------------------------

%package devel
Summary:	Kdesvn devel package
Group:		Development/KDE and Qt
Requires:	%{lib_svn_qt} = %{version}-%{release}

%description devel
kdesvn devel package

%files devel
%{_kde_includedir}/*
%{_kde_libdir}/*.so
%{_datadir}/dbus-1/interfaces/org.kde.kdesvnd.xml

#-----------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

# fwang: conflicts with cervisia
rm -f %{buildroot}%{_kde_services}/svn*.protocol

