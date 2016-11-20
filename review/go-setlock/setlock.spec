%global with_debug 0
%global with_check 1

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

Summary: a go port of setlock (an utility of daemontools)
Name: setlock
Version: 1.3.0
Release: 1%{?dist}
Source0: https://github.com/moznion/go-setlock/archive/v%{version}.tar.gz#/go-%{name}-%{version}.tar.gz
Patch0: go-setlock-1.3.0_libpath.patch
License: MIT
URL: https://github.com/moznion/go-setlock

ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
BuildRequires: %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
go-setlock is a go port of setlock (an utility of daemontools).

%prep
%setup -q -n go-%{name}-%{version}
%patch0 -p1 -b .libpath
%{__mkdir_p} go-setlock
%{__cp} locker* go-setlock

%build
go build cmd/setlock/setlock.go

%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_bindir}
%{__install} -m0755 setlock ${RPM_BUILD_ROOT}%{_bindir}

%if 0%{?with_check}
%check
go test
%endif

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_bindir}/setlock

%changelog
* Sun Nov 20 2016 IWAI, Masaharu <iwaim.sub@gmail.com> - 1.3.0-1
- initial build for Fedora
