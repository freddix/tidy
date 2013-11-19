Summary:	Utility to clean up and pretty print HTML files
Name:		tidy
Version:	1.46
Release:	1
License:	distributable
Group:		Applications/Text
# manual download http://tidy.cvs.sourceforge.net/viewvc/tidy/tidy/?view=tar
Source0:	%{name}.tar
# Source0-md5:	c5f63236be371b1f2d9d06ab01a7a74e
URL:		http://tidy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tidy is utility for cleaning and pretty printing HTML files. It can
help in keeping your WWW sources in unified format (case of tags) and
proper encoding of different character sets.

%package libs
Summary:	Tidy library
Group:		Libraries

%description libs
Tidy library.

%package devel
Summary:	Tidy header files
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Tidy header files.

%prep
%setup -qn %{name}

%build
cp -af build/gnuauto/* .
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc htmldoc/*
%attr(755,root,root) %{_bindir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h

