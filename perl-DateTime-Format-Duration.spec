%define module	DateTime-Format-Duration
%define name	perl-%{module}
%define version 1.02
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Format and parse DateTime::Durations 
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/DateTime/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch:	noarch

%description
This module formats and parses DateTime::Duration objects as well as other
durations representations.

%prep
%setup -q -n %{module}-%{version}
# fix perms
chmod 644 LICENSE README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
#%make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc LICENSE README Changes
%{perl_vendorlib}/DateTime
%{_mandir}/*/*

