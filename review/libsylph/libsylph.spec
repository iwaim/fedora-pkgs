Name:           libsylph
Summary:        E-Mail client library
Version:        1.1.0
Release:        1%{?dist}
License:        LGPLv2.1+

URL:            http://sylpheed.sraoss.jp/en/
Source0:        http://sylpheed.sraoss.jp/sylpheed/libsylph/%{name}-%{version}.tar.bz2
Patch0:         libsylph-1.1.0-glib-header.patch
BuildRequires:  glib2-devel >= 2.4.0

%description
LibSylph is an e-mail client library which is derived from Sylpheed.
LibSylph is a lightweight but featureful library. It has many common e-mail
related features and other useful functions, and you can utilize them from
your application. Moreover you can create a new e-mail client by wrapping
LibSylph with any UI.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .glibheader

%build
%configure --enable-shared --disable-static
make

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} %{buildroot}%{_libdir}/libsylph.la
%find_lang %{name}

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc README* AUTHORS COPYING ChangeLog NEWS TODO
%{_libdir}/libsylph.so.*

%files devel
%doc doc
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Mon Dec  7 2015 IWAI, Masaharu <iwaim.sub@gmail.com> - 1.1.0-1
- initial build for Fedora

