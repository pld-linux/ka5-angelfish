#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		angelfish
Summary:	A webbrowser for small mobile devices
Name:		ka5-%{kaname}
Version:	23.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	3cc9c08f4e2e422e79e0277ea9531545
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Network-devel >= 5.15.9
BuildRequires:	Qt5Positioning-devel >= 5.15
BuildRequires:	Qt5Qml-devel >= 5.15.9
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test
BuildRequires:	Qt5WebChannel-devel >= 5.15
BuildRequires:	Qt5WebEngine-devel >= 5.15
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.95.0
BuildRequires:	kf5-kconfig-devel >= 5.95.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.95.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.95.0
BuildRequires:	kf5-ki18n-devel >= 5.95.0
BuildRequires:	kf5-kirigami2-devel >= 5.95.0
BuildRequires:	kf5-knotifications-devel >= 5.95.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.95.0
BuildRequires:	kf5-purpose-devel >= 5.95.0
BuildRequires:	kf5-qqc2-desktop-style-devel >= 5.95.0
BuildRequires:	kirigami-addons-devel >= 0.6
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a webbrowser designed to

- be used on small mobile devices,
- integrate well in Plasma workspaces

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/angelfish
%attr(755,root,root) %{_bindir}/angelfish-webapp
%{_desktopdir}/org.kde.angelfish.desktop
%{_datadir}/config.kcfg/angelfishsettings.kcfg
%{_iconsdir}/hicolor/scalable/apps/org.kde.angelfish.svg
%{_datadir}/knotifications5/angelfish.notifyrc
%{_datadir}/metainfo/org.kde.angelfish.metainfo.xml
