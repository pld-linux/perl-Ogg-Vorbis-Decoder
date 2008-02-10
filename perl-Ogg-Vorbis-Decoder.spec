#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Ogg
%define	pnam	Vorbis-Decoder
Summary:	Ogg::Vorbis::Decoder - An object-oriented Ogg Vorbis decoder
Summary(pl.UTF-8):	Ogg::Vorbis::Decoder - obiektowo zorientowany dekoder Ogg Vorbis
Name:		perl-Ogg-Vorbis-Decoder
Version:	0.6
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b95fa97f11fea460c8059ccb53db2bda
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides users with Decoder objects for Ogg Vorbis files.
One can read data in PCM format from the stream, seek by raw bytes,
PCM samples, or time, and gather decoding-specific information not
provided by Ogg::Vorbis::Header. Currently, we provide no support for
the callback mechanism provided by the Vorbisfile API; this may be
included in future releases.

%description -l pl.UTF-8
Ten moduł dostarcza obiekty Decoder dla plików Ogg Vorbis. Pozwala
odczytywać dane w formacie PCM ze strumienia, przemieszczać się po
surowych bajtach, próbkach PCM lub czasie i gromadzić specyficzne dla
dekodera informacje nie dostarczane przez Ogg::Vorbis::Header.
Aktualnie nie ma obsługi mechanizmu wywołań zwrotnych dostarczanego
przez API Vorbisfile - być może pojawi się ona w przyszłych wersjach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%dir %{perl_vendorarch}/auto/Ogg/Vorbis/Decoder
%{perl_vendorarch}/Ogg/Vorbis/Decoder.pm
%{perl_vendorarch}/auto/Ogg/Vorbis/Decoder/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Ogg/Vorbis/Decoder/*.so
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
