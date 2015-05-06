Summary:	VXI-11 RPC protocol libraries
Summary(pl.UTF-8):	Biblioteki protokołu RPC VXI-11
Name:		vxi
Version:	0.0.20121221
Release:	2
License:	Public Domain
Group:		Libraries
Source0:	http://www.librevisa.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	5958206a0c60990227c000474b319c34
Patch0:		%{name}-shared.patch
URL:		http://www.librevisa.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.10
BuildRequires:	libtool >= 2:2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# both libraries require external *_svc symbols
%define		skip_post_check_so	libvxi.*

%description
The VXI-11 protocol is used for communication with test and
measurement equipment. It provides a "virtual" representation of the
command, event and abort channels specified in the LXI protocol.

%description -l pl.UTF-8
Protokół VXI-11 służy do komunikacji ze sprzętem testowym i
pomiarowym. Zapewnia "wirtualną" reprezentację kanałów poleceń,
zdarzeń i przerwania, opisanych w protokole LXI.

%package devel
Summary:	Header files for VXI libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek VXI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for VXI libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek VXI.

%package static
Summary:	Static VXI libraries
Summary(pl.UTF-8):	Statyczne biblioteki VXI
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VXI libraries.

%description static -l pl.UTF-8
Statyczne biblioteki VXI.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvxiclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvxiclient.so.0
%attr(755,root,root) %{_libdir}/libvxiserver.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvxiserver.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvxiclient.so
%attr(755,root,root) %{_libdir}/libvxiserver.so
%{_libdir}/libvxiclient.la
%{_libdir}/libvxiserver.la
%{_includedir}/vxi.h
%{_includedir}/vxi_intr.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libvxiclient.a
%{_libdir}/libvxiserver.a
