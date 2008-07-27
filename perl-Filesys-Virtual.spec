#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Filesys
%define		pnam	Virtual
Summary:	Filesys::Virtual - Perl extension to provide a framework for a virtual filesystem
Summary(pl.UTF-8):	Filesys::Virtual - szkielet dla wirtualnych systemów plików
Name:		perl-Filesys-Virtual
Version:	0.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	825f02140a699cd11d23ebce178746fb
URL:		http://search.cpan.org/dist/Filesys-Virtual/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements a base class for virtual filesystems.

%description -l pl.UTF-8
Ten moduł implementuje klasę bazową dla wirtualnych systemów plików.

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
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Filesys/Virtual

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
# next one could be moved to perl-modules if more things
# not depending on this module will require that directory
%dir %{perl_vendorlib}/Filesys
# modules using this one puts them under next dir
%dir %{perl_vendorlib}/Filesys/Virtual
%{perl_vendorlib}/Filesys/Virtual.pm
%{_mandir}/man3/*
