#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		angelfish
Summary:	A webbrowser for small mobile devices
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	4a40f4a7b712f90e808f7abf7aecf706
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Network-devel >= 5.15.9
BuildRequires:	Qt6Positioning-devel >= 5.15
BuildRequires:	Qt6Qml-devel >= 5.15.9
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Sql-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test
BuildRequires:	Qt6WebChannel-devel >= 5.15
BuildRequires:	Qt6WebEngine-devel >= 5.15
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	futuresql-qt6-devel >= 0.1.1
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 5.95.0
BuildRequires:	kf6-kconfig-devel >= 5.95.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.95.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.95.0
BuildRequires:	kf6-ki18n-devel >= 5.95.0
BuildRequires:	kf6-kirigami-devel >= 5.95.0
BuildRequires:	kf6-knotifications-devel >= 5.95.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.95.0
BuildRequires:	kf6-purpose-devel >= 5.95.0
BuildRequires:	kf6-qqc2-desktop-style-devel >= 5.95.0
BuildRequires:	kirigami-addons-devel >= 0.6
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
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
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
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
%{_datadir}/knotifications6/angelfish.notifyrc
%{_datadir}/metainfo/org.kde.angelfish.metainfo.xml
