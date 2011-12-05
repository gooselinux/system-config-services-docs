# Command line configurables

%if 0%{?fedora}%{?rhel} == 0 || 0%{?fedora} >= 8 || 0%{?rhel} >= 6
%bcond_without rarian_compat
%else
%bcond_with rarian_compat
%endif

Summary: Documentation for configuring system services
Name: system-config-services-docs
Version: 1.1.8
Release: 1%{?dist}
URL: https://fedorahosted.org/%{name}
Source0: http://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Documentation
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: gnome-doc-utils
BuildRequires: docbook-dtds
%if %{with rarian_compat}
BuildRequires: rarian-compat
%else
BuildRequires: scrollkeeper
%endif
# Until version 0.99.28, system-config-services contained online documentation.
# From version 0.99.29 on, online documentation is split off into its own
# package system-config-services-docs. The following ensures that updating from
# earlier versions gives you both the main package and documentation.
Obsoletes: system-config-services < 0.99.29
Requires: system-config-services >= 0.99.29
Requires: yelp
%if %{with rarian_compat}
Requires: rarian-compat
%else
Requires(post): scrollkeeper
Requires(postun): scrollkeeper
%endif

%description
This package contains the online documentation for system-config-services is a
utility which allows you to configure which services should be enabled on your
machine.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%buildroot install

%post
%{_bindir}/scrollkeeper-update -q || :

%postun
%{_bindir}/scrollkeeper-update -q || :

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%doc %{_datadir}/omf/system-config-services
%doc %{_datadir}/gnome/help/system-config-services

%changelog
* Tue Mar 23 2010 Nils Philippsen <nils@redhat.com> - 1.1.8-1
- pick up translation updates

* Mon Sep 28 2009 Nils Philippsen <nils@redhat.com> - 1.1.7-1
- pick up new translations

* Wed Aug 26 2009 Nils Philippsen <nils@redhat.com>
- explain obsoleting old versions

* Thu May 28 2009 Nils Philippsen <nils@redhat.com>
- use simplified source URL

* Tue Apr 14 2009 Nils Philippsen <nils@redhat.com> - 1.1.6-1
- add sr@latin structure, move po file (#495460)
- pull in updated translations

* Wed Apr 08 2009 Nils Philippsen <nils@redhat.com> - 1.1.5-1
- pull in updated translations

* Thu Dec 18 2008 Nils Philippsen <nils@redhat.com> - 1.1.4-1
- add runtime requirements for rarian-compat/scrollkeeper

* Wed Dec 17 2008 Nils Philippsen <nils@redhat.com>
- add yelp dependency

* Mon Dec 15 2008 Nils Philippsen <nils@redhat.com> - 1.1.3-1
- remove unnecessary "Obsoletes: serviceconf <= 0.8.1", "Obsoletes:
  redhat-config-services <= 0.8.5"

* Mon Dec 08 2008 Nils Philippsen <nils@redhat.com> - 1.1.2-1
- remove unnecessary "Conflicts: system-config-services < 0.99.29"

* Fri Nov 28 2008 Nils Philippsen <nils@redhat.com> - 1.1.1-1
- separate documentation from system-config-services
- remove stuff not related to documentation
- add source URL
