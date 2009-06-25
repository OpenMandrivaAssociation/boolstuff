%define name boolstuff
%define version 0.1.12
%define api 0.1
%define major 0
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name} %{major}


Name:    %{name}
Summary: Disjunctive Normal Form boolean expression library and example
Version: %{version}
Release: %mkrel 0
License: GPLv2+
Group:   Development/C++

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: %{name}-%{version}.tar.gz
URL: http://sarrazip.com/dev/boolstuff.html


%description
This library contains an algorithm that converts a boolean expression
binary tree into the Disjunctive Normal Form. The NOT operator
is supported.
A command that calls this library is also provided.

%description -l fr
Cette librairie contient un algorithme qui convertit une expression
booléenne sous forme d'arbre binaire en sa forme normale disjonctive.
L'opérateur de négation est supporté.
Une commande appelant cette librairie est aussi fournie.


%package -n %{libname}
Summary:  Disjunctive Normal Form boolean expression library
Group:    Development/C++
Provides: %{libname_orig} = %{version}-%{release}

%description -n %{libname}
This library contains an algorithm that converts a boolean expression
binary tree into the Disjunctive Normal Form. The NOT operator
is supported.

%package -n %{develname}
Summary:  C++ header files for the boolstuff library
Group:    Development/C++
Requires: %{libname} = %{version}
Provides: %{libname_orig}-devel = %{version}-%{release}

%description -n %{develname}
C++ header files for the Disjunctive Normal Form boolean expression library.

%package -n booldnf
Summary: Converts a boolean expression to the DNF
Group:   Sciences/Computer science
Requires: %{libname}

%description -n booldnf
booldnf is a program that reads boolean expressions from its standard
input and rewrites them in Disjunctive Normal Form on its standard out‐
put. It uses the BoolStuff library.


%prep
%setup -q

%build
# Option --disable-dependency-tracking seems necessary for g++ 2.95.3.
./autogen.sh --disable-dependency-tracking --prefix=/usr
make %{?_smp_mflags}

%install
rm -fR $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

%clean
rm -fR $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/lib*.so.*
%{_mandir}/man3/boolstuff*
# do we need to redistribute the GPLv2 license? (INSTALL file)
%doc %{_defaultdocdir}/*

%files -n %{develname}
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*

%files -n booldnf
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/man1/booldnf*
