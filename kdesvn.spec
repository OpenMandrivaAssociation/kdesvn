Summary:	kdesvn is yet another client for subversion
Name:		kdesvn
Version:	0.13.0
Release:	%mkrel 1
License:	GPL
Group:		Graphical desktop/KDE
Url:		http://www.alwins-world.de/programs/kdesvn/
Source0:	http://www.alwins-world.de/programs/download/kdesvn/%{name}-%{version}.tar.bz2
Requires:	graphviz
BuildRequires:	cmake
BuildRequires:	kdelibs-devel 
BuildRequires:	subversion-devel >= 1.2
BuildRequires:	neon-devel
BuildRequires:	apr-devel
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

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,-)
%doc README AUTHORS COPYING ChangeLog
%_bindir/*
%_libdir/kde3/*
%_datadir/apps/*
%doc %_docdir/HTML/*/*
%_iconsdir/*/*/*/*
%_datadir/locale/*/*
%_datadir/applications/*
%_datadir/config.kcfg/*
%_datadir/services/*
%_datadir/man/man1/*

#-----------------------------------------------------------------

%define lib_svn_qt %mklibname svnqt 2
%define invalid_lib %mklibname svnqt 1

%package -n %lib_svn_qt
Summary:	KDE Svn core library
Group:		Graphical desktop/KDE
Obsoletes: %invalid_lib 

%post -n %lib_svn_qt -p /sbin/ldconfig
%postun -n %lib_svn_qt -p /sbin/ldconfig

%description -n %lib_svn_qt
KDE Svn core library

%files -n %lib_svn_qt
%defattr(-,root,root,-)
%_libdir/*.so.*

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
%_libdir/*.la

#-----------------------------------------------------------------

%prep
%setup -q

%build
export QTDIR=%qt3dir
export KDEDIR=%{_prefix}
%cmake

%make

%install
rm -rf %{buildroot}

cd build
%makeinstall_std
cd -

%clean
rm -rf %{buildroot}
