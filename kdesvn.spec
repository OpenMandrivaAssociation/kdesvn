Summary:	KDE client for subversion
Name:		kdesvn
Version:	2.0.0
Release:	6
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kdesvn.alwins-world.de/
Source0:	http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Patch0:		kdesvn-2.0.0-qt-5.13.patch
BuildRequires:	pkgconfig(uuid)
BuildRequires:	subversion-devel
BuildRequires:	db-devel
BuildRequires:	openldap-devel
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Widgets)
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
%{_bindir}/*
%{_libdir}/qt5/plugins/*
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/applications/org.kde.kdesvn.desktop
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/ServiceMenus/*.desktop
%{_datadir}/kxmlgui5/kdesvn
%{_datadir}/dbus-1/*/*
%{_datadir}/kconf_update/*
%{_datadir}/kdesvn

%prep
%autosetup -p1

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --with-html

