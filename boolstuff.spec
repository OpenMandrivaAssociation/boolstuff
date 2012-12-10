Name:		boolstuff
Summary:	Disjunctive Normal Form boolean expression library and example
Version:	0.1.13
Release:	3
License:	GPLv2+
Group:		Development/C++
Source:		%{name}-%{version}.tar.gz
URL:		http://sarrazip.com/dev/boolstuff.html

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
%{_libdir}/pkgconfig/*

#--------------------------------------------------------------------------#
%prep
%setup -q

%build
# autoargh listao
./autogen.sh \
	--prefix %_prefix \
	--libdir=%_libdir

%make

%install
%makeinstall_std





%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.13-2mdv2011.0
+ Revision: 610084
- rebuild

* Fri Mar 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.1.13-1mdv2010.1
+ Revision: 514391
- use tab in spec
- update to 1.1.13
- drop old patch that it was apply upstream

* Fri Jun 26 2009 Helio Chissini de Castro <helio@mandriva.com> 0.1.12-0mdv2010.0
+ Revision: 389502
- Added compilation patch for gcc 4.4
- Fixed build and library soname

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - Improve .spec file (by heliocastro)
    - imported package boolstuff


