%define major 6
%define u_major 1
%define libname %mklibname xmu %{major}
%define libu %mklibname xmuu %{u_major}
%define develname %mklibname xmu -d

Name:		libxmu
Summary:	Xmu Library
Version:	1.1.1
Release:	4
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xt)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.3.0

%description
Xmu Library.

%package -n %{libname}
Summary:	Xmu Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
Xmu Library.

%package -n %{libu}
Summary:	Xmuu Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Conflicts:	%{libname} < 1.1.0-4

%description -n %{libu}
Xmuu Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libu} = %{version}-%{release}
Provides:	libxmu-devel = %{version}-%{release}
Obsoletes:	%{_lib}xmu6-devel < 1.1.1
Obsoletes:	%{_lib}xmu-static-devel < 1.1.1
Conflicts:	libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}.

%prep
%setup -qn libXmu-%{version}

%build
autoreconf -ifs
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXmu.so.%{major}*

%files -n %{libu}
%{_libdir}/libXmuu.so.%{u_major}*

%files -n %{develname}
%{_libdir}/libXmuu.so
%{_libdir}/libXmu.so
%{_libdir}/pkgconfig/xmuu.pc
%{_libdir}/pkgconfig/xmu.pc
%{_includedir}/X11/Xmu/CloseHook.h
%{_includedir}/X11/Xmu/Xct.h
%{_includedir}/X11/Xmu/Xmu.h
%{_includedir}/X11/Xmu/WidgetNode.h
%{_includedir}/X11/Xmu/Atoms.h
%{_includedir}/X11/Xmu/Misc.h
%{_includedir}/X11/Xmu/Converters.h
%{_includedir}/X11/Xmu/StdCmap.h
%{_includedir}/X11/Xmu/ExtAgent.h
%{_includedir}/X11/Xmu/StdSel.h
%{_includedir}/X11/Xmu/WinUtil.h
%{_includedir}/X11/Xmu/DisplayQue.h
%{_includedir}/X11/Xmu/Initer.h
%{_includedir}/X11/Xmu/Lookup.h
%{_includedir}/X11/Xmu/SysUtil.h
%{_includedir}/X11/Xmu/Drawing.h
%{_includedir}/X11/Xmu/Error.h
%{_includedir}/X11/Xmu/EditresP.h
%{_includedir}/X11/Xmu/CvtCache.h
%{_includedir}/X11/Xmu/Editres.h
%{_includedir}/X11/Xmu/CurUtil.h
%{_includedir}/X11/Xmu/CharSet.h
%{_includedir}/X11/Xmu/WhitePoint.h
%{_datadir}/doc/libXmu

%changelog
* Fri Mar 09 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.1-3
+ Revision: 783462
- rebuild without scriptlet dependencies

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Wed Mar 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 783201
- version update 1.1.1

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-5
+ Revision: 745634
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Wed Dec 14 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-4
+ Revision: 741187
- missing catch all for DSO lib
- rebuild
- split out libxmuu lib
- removed .la files
- removed pre 200900 scriptlets
- cleaned up spec

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3
+ Revision: 662426
- mass rebuild

* Fri Feb 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-2
+ Revision: 638527
- dropped major from devel and static pkg
- added proper provides and obsoletes

* Sat Oct 30 2010 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 590466
- update file list

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.5-2mdv2010.1
+ Revision: 464041
- Fix BuildRequires

  + Thierry Vignaud <tv@mandriva.org>
    - new release

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-5mdv2010.0
+ Revision: 425930
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2009.0
+ Revision: 229748
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Feb 13 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-2mdv2008.1
+ Revision: 166863
- Revert build requires and upstream tarball

* Wed Jan 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-1mdv2008.1
+ Revision: 153708
- Update to version 1.0.4.
  Also changed to use mandriva git mirror to generate tarball with
  "git-archive --format=tar" command.
  This is exactly upstream version as there are no Mandriva specific patches.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 151892
- Update BuildRequires and rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.3-1mdv2007.0
+ Revision: 85955
- new release

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - X11R7.1
    - increment release
    - fixed more dependencies
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

