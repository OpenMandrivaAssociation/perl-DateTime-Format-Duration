%define upstream_name	 DateTime-Format-Duration
%define upstream_version 1.03a

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Format and parse DateTime::Durations 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tgz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildrequires: perl(DateTime)
Buildrequires: perl(DateTime::Duration)

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module formats and parses DateTime::Duration objects as well as other
durations representations.

%prep
%setup -q -n %{upstream_name}-1.03
# fix perms
chmod 644 LICENSE README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc LICENSE README Changes
%{perl_vendorlib}/DateTime
%{_mandir}/*/*

