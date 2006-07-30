#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filesys
%define		pnam	Virtual
Summary:	perl(Filesys::Virtual) − Perl extension to provide a framework for a virtual filesystem
Name:		perl-Filesys-Virtual
Version:	0.05
Release:	0.1
# note if it is "same as perl"
License:	same as perl
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
#BuildRequires:	perl-
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a base class for virtual filesystems.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# next one could be moved to perl-modules if more things
# nod dependin on this module will require that directory
%dir %{perl_vendorlib}/Filesys
# modules using this one puts them under next dir, 
%dir %{perl_vendorlib}/Filesys/Virtual
%{perl_vendorlib}/Filesys/Virtual.pm
%{_mandir}/man3/*
