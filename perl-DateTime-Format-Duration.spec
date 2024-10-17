%define upstream_name	 DateTime-Format-Duration
%define upstream_version 1.03a

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Format and parse DateTime::Durations 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{upstream_name}-%{upstream_version}.tgz

BuildRequires:	perl-devel
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Duration)

BuildArch:	noarch

%description
This module formats and parses DateTime::Duration objects as well as other
durations representations.

%prep
%setup -q -n %{upstream_name}-1.03
# fix perms
chmod 644 LICENSE README Changes

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc LICENSE README Changes
%{perl_vendorlib}/DateTime
%{_mandir}/*/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.30.0a-2mdv2011.0
+ Revision: 681390
- mass rebuild

* Sun Nov 08 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0a-1mdv2011.0
+ Revision: 463043
- adding missing buildrequires:
- update to 1.03a
  really, it's 1.03 with $VERSION set correctly, which author forgot to
  bump in 1.03... so he thought issuing 1.03a would be better than 1.04,
  really screwing packagers and making them deal with that manually...
  as if version numbers were expensive. hate, hate, hate!

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 395153
- update to 1.03 for real this time
- using %%perl_convert_version
- fixed license field
- update to 1.03

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.02-6mdv2009.0
+ Revision: 256498
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.02-4mdv2008.1
+ Revision: 135833
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-4mdv2008.0
+ Revision: 46973
- rebuild


* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-3mdv2007.0
- Rebuild

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-2mdk 
- don't ship useless empty dirs
- make test in %%check
- disabled test, something is broken
- fix doc files perms

* Sat Feb 12 2005 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-1mdk 
- first mdk release

