Summary:     GNOME http client library
Name:        libghttp
Version:     0.30
Release:     1
Copyright:   GPL
Group:       X11/gnome
Source:      ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
URL:         http://www.gnome.org/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Library for making HTTP 1.1 requests.

%package devel
Summary:     GNOME http client development
Group:       X11/gnome
Requires:    %{name} = %{version}

%description devel
Libraries and includes files you can use for libghttp development

%package static
Summary:     GNOME http client static library
Group:       X11/gnome
Requires:    %{name}-devel = %{version}

%description static
GNOME http client static library.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr/X11R6

make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*so.*.*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)

/usr/X11R6/lib/lib*.so.*

%files devel
%defattr(644, root, root, 755)
%doc AUTHORS ChangeLog NEWS README
/usr/X11R6/lib/lib*.so
/usr/X11R6/include/*

%files static
%attr(644, root, root) /usr/X11R6/lib/*a

%changelog
* Fri Oct  2 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.30-1]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- changed Copyright field to GPL,
- removed Packager field (this must be placed in private ~/.rpmrc),
- removed COPYING from %doc,
- all %doc moved to devel,
- added full %attr description in %files,
- added striping shared libraries.
