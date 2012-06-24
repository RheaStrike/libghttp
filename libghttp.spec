Summary:	GNOME http client library
Summary(es):	Biblioteca cliente http del GNOME
Summary(ko):	GNOME http Ŭ���̾�Ʈ ���̺귯��
Summary(pl):	Biblioteka funkcji klienta http
Summary(pt_BR):	Biblioteca cliente para http do GNOME
Summary(ru):	���������� http-������� ��� GNOME
Summary(uk):	��̦����� http-�̦���� ��� GNOME
Name:		libghttp
Version:	1.0.9
Release:	9
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libghttp/1.0/%{name}-%{version}.tar.gz
# Source0-md5: 0690e7456f9a15c635f240f3d6d5dab2
Patch0:		%{name}-ac.patch
Patch1:		%{name}-fixlocale.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for making HTTP 1.1 requests.

%description -l es
Biblioteca cliente http 1.1 del GNOME.

%description -l pl
Biblioteka funkcji umo�liwiaj�cych realizacj� zapyta� HTTP 1.1.

%description -l pt_BR
Biblioteca cliente para http 1.1 do GNOME.

%description -l ru
���������� ��� ���������� HTTP 1.1 ��������.

%description -l uk
��̦����� ��� ��������� HTTP 1.1 ����Ԧ�.

%package devel
Summary:	GNOME http client development
Summary(es):	Biblioteca cliente http 1.1 del GNOME - desarrollo
Summary(ko):	GNOME http Ŭ���̾�Ʈ ���߿� �ʿ��� ���̺귯���� ��� ����
Summary(pl):	Biblioteki i pliki nag��wkowe libghttp
Summary(pt_BR):	Componentes para desenvolvimento com o cliente http do GNOME.
Summary(ru):	���������� http-�������� ��� GNOME
Summary(uk):	�������� http-�̦��Ԧ� Ц� GNOME
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}

%description devel
Libraries and includes files you can use for libghttp development.

%description devel -l es
Biblioteca cliente http 1.1 del GNOME - desarrollo.

%description devel -l pl
Biblioteki i pliki nag��wkowe potrzebne do programowania z
wykorzystaniem libghttp.

%description devel -l pt_BR
Componentes para desenvolvimento com o cliente http do GNOME.

%description devel -l ru
������ ��� ���������� �������� � �������������� libghttp.

%description devel -l uk
������ ��� �������� ������� � ������������� libghttp.

%package static
Summary:	GNOME http client static library
Summary(pl):	Statyczna biblioteka libghttp
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libghttp
Summary(ru):	���������� http-�������� ��� GNOME - ����������� ����������
Summary(uk):	�������� http-�̦��Ԧ� Ц� GNOME - ������Φ ¦�̦�����
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
GNOME http client static library.

%description static -l pl
Wersja statyczna biblioteki libghttp.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libghttp.

%description static -l ru
����������� ���������� ��� ���������� �������� � ��������������
libghttp.

%description static -l uk
������Φ ¦�̦����� ��� �������� ������� � ������������� libghttp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
