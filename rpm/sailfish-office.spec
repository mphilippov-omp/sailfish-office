Name: sailfish-office
Version: 0.1
Release: 1
Summary: Sailfish office viewer
Group: System/Base
License: GPLv2
Source0: %{name}-%{version}.tar.gz
BuildRequires: pkgconfig(Qt5Declarative)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(libjollasignonuiservice-qt5)
#BuildRequires: poppler-qt5-devel poppler-qt5 poppler-devel poppler
BuildRequires: mapplauncherd-qt5-devel
BuildRequires: cmake
Requires: calligra-components
Requires: sailfishsilica
Requires: sailfish-accounts


%description
%{summary}.

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/qt4/imports/Sailfish/Office/
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/dbus-1/services/org.sailfish.documents.service
#%{_datadir}/translations/

%prep
%setup -q -n %{name}-%{version}


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}


%install
make DESTDIR=%{buildroot} install
