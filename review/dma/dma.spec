# add --with aliases option; enable /etc/aliases file option. it provides by setup package in Fedora
%bcond_with aliases

Summary: a small Mail Transport Agent (MTA)
Name: dma
Version: 0.10
Release: 1%{?dist}
Source0: https://github.com/corecode/dma/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: dma-aliases
Patch0: dma-0.10_owners.patch
License: BSD
Provides: MTA
URL: https://github.com/corecode/dma/

BuildRequires: byacc
BuildRequires: flex
BuildRequires: openssl-devel

%description
dma (DragonFly Mail Agent) is a small Mail Transport Agent (MTA), designed 
for home and office use.  It accepts mails from locally installed 
Mail User Agents (MUA) and delivers the mails either locally or to 
a remote destination.
Remote delivery includes several features like TLS/SSL support and
SMTP authentication.

dma is not intended as a replacement for real, big MTAs like sendmail(8)
or postfix(1).  Consequently, dma does not listen on port 25 for
incoming connections.


%prep
%setup -q
%patch0 -p1

%build
%{__make} %{?_smp_mflags} PREFIX=%{_prefix}  LIBEXEC=%{_libexecdir} \
                          CONFDIR=%{_sysconfdir}/dma MAN=%{_mandir} VAR=%{_var} 


%install
%{__rm} -rf ${RPM_BUILD_ROOT}
%{__make} install sendmail-link mailq-link install-spool-dirs install-etc \
          DESTDIR=${RPM_BUILD_ROOT} PREFIX=%{_prefix} LIBEXEC=%{_libexecdir} \
          CONFDIR=%{_sysconfdir}/dma MAN=%{_mandir} VAR=%{_var}

%if %{with aliases}
%{__install} -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_sysconfdir}/aliases
%endif


%files
%defattr(-,root,root)
%doc LICENSE README.* TODO
%attr(-,root,mail) %{_sbindir}/dma
%{_sbindir}/mailq
%{_sbindir}/sendmail
%attr(-,root,mail) %{_libexecdir}/dma-mbox-create
%dir %{_sysconfdir}/dma
%attr(-,root,mail) %config(noreplace) %{_sysconfdir}/dma/auth.conf
%attr(-,root,mail) %config(noreplace) %{_sysconfdir}/dma/dma.conf
%if %{with aliases}
%config(noreplace) %{_sysconfdir}/aliases
%endif
%{_mandir}/man8/dma.8*
%attr(-,root,mail) %dir %{_var}/spool/dma

%changelog
* Fri Jan 22 2016 IWAI, Masaharu <iwaim.sub@gmail.com> - 0.10-1
- initial build for Fedora

