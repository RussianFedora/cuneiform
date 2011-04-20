Name:           cuneiform
Version:        1.1.0
Release:        1%{?dist}.R
Summary:        Multi-language OCR system

Group:          User Interface/Desktops
License:        BSD
URL:            https://launchpad.net/cuneiform-linux
Source0:        http://launchpad.net/cuneiform-linux/1.1/1.1/+download/cuneiform-linux-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake
BuildRequires:  ImageMagick-devel
BuildRequires:  ImageMagick-c++-devel



%description
Cuneiform is an multi-language OCR system originally developed
and open sourced by Cognitive Technologies. Cuneiform was
originally a Windows program, which was ported to Linux
by Jussi Pakkanen.


%package devel
Summary:        Static library and header files for the %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}


%description devel
The %{name}-devel package contains API documentation for
developing developing plugins for %{name}.


%prep
%setup -q -n %{name}-linux-%{version}


%build
mkdir builddir
cd builddir
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd builddir
make install DESTDIR=$RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc readme.txt issues.txt cuneiform_src/Addfiles/license.txt
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/cuneiform/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/*.so


%changelog
* Wed Apr 20 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 1.1.0-1.R
- update to 1.1.0

* Wed Nov  3 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.0.0-2
- rebuilt against new ImageMagick

* Mon Jul  5 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 1.0.0-1
- update to 1.0.0

* Wed Sep 16 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 0.8.0-1
- update to 0.8.0

* Mon Jun  1 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7-1
- update to 0.7

* Tue May  5 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 0.6-1
- update to 0.6

* Wed Sep 11 2008 Denis Frolov <d.frolov81 AT mail.ru> 0.4-1
- Initial build for Red Hat Club Repository
