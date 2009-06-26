Name:    boolstuff
Summary: Disjunctive Normal Form boolean expression library and example
Version: 0.1.12
Release: %mkrel 0
License: GPLv2+
Group:   Development/C++
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: %{name}-%{version}.tar.gz
URL: http://sarrazip.com/dev/boolstuff.html
Patch0: boolstuff-0.1.12-gcc44-compile-fix.patch

%description
This library contains an algorithm that converts a boolean expression
binary tree into the Disjunctive Normal Form. The NOT operator
is supported.
A command that calls this library is also provided.

%files
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/man1/booldnf*

#--------------------------------------------------------------------------#

%define soname 0
%define api 0.1
%define libname %mklibname boolstuff%{api}_ %soname

%package -n %{libname}
Summary:  Disjunctive Normal Form boolean expression library
Group:    Development/C++

%description -n %{libname}
This library contains an algorithm that converts a boolean expression
binary tree into the Disjunctive Normal Form. The NOT operator
is supported.

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/libboolstuff-%{api}.so.%{soname}*
%{_mandir}/man3/boolstuff*
# do we need to redistribute the GPLv2 license? (INSTALL file)
%doc %{_defaultdocdir}/*

#--------------------------------------------------------------------------#

%define develname %mklibname boolstuff -d

%package -n %{develname}
Summary:  C++ header files for the boolstuff library
Group:    Development/C++
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Provides: libboolstuff-devel = %{version}-%{release}

%description -n %{develname}
C++ header files for the Disjunctive Normal Form boolean expression library.

%files -n %{develname}
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*

#--------------------------------------------------------------------------#
%prep
%setup -q
%patch0 -p0 -b .compile

%build
# autoargh listao
./autogen.sh \
	--prefix %_prefix \
	--libdir=%_libdir

%make

%install
rm -fR $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -fR $RPM_BUILD_ROOT


