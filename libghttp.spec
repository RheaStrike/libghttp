Summary:	GNOME http client library
Summary(pl):	Biblioteka funkcji klienta http
Name:		libghttp
Version:	1.0.9
Release:	5
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libghttp/1.0/%{name}-%{version}.tar.gz
# Source0-md5: 0690e7456f9a15c635f240f3d6d5dab2
Patch0:		%{name}-ac.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for making HTTP 1.1 requests.

%description -l pl
Biblioteka funkcji umożliwiających realizację zapytań HTTP 1.1.

%package devel
Summary:	GNOME http client development
Summary(pl):	Biblioteki i pliki nagłówkowe libghttp
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Libraries and includes files you can use for libghttp development.

%description devel -l pl
Biblioteki i pliki nagłówkowe potrzebne do programowania z
wykorzystaniem libghttp.

%package static
Summary:	GNOME http client static library
Summary(pl):	Statyczna biblioteka libghttp
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GNOME http client static library.

%description static -l pl
Wersja statyczna biblioteki libghttp.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/ghttp-1.0

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install http_*.h $RPM_BUILD_ROOT%{_includedir}/ghttp-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.sh
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
