%define upstream_name    DateTime-Event-Recurrence
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    DateTime::Set extension for create basic recurrence sets
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DateTime)
BuildRequires: perl(DateTime::Set)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides convenience methods that let you easily create
'DateTime::Set' objects for various recurrences, such as "once a month" or
"every day". You can also create more complicated recurrences, such as
"every Monday, Wednesday and Thursday at 10:00 AM and 2:00 PM".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


