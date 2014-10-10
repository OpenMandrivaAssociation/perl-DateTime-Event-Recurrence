%define upstream_name    DateTime-Event-Recurrence
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	DateTime::Set extension for create basic recurrence sets
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Set)
BuildArch:	noarch

%description
This module provides convenience methods that let you easily create
'DateTime::Set' objects for various recurrences, such as "once a month" or
"every day". You can also create more complicated recurrences, such as
"every Monday, Wednesday and Thursday at 10:00 AM and 2:00 PM".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.160.0-2mdv2011.0
+ Revision: 654908
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 542955
- import perl-DateTime-Event-Recurrence


* Thu May 06 2010 cpan2dist 0.16-1mdv
- initial mdv release, generated with cpan2dist
