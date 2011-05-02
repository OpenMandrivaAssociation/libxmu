%define libname %mklibname xmu 6
%define develname %mklibname xmu -d
%define staticname %mklibname xmu -s -d

Name: libxmu
Summary: Xmu Library
Version: 1.1.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.3.0

%description
Xmu Library

#-----------------------------------------------------------

%package -n %{libname}
Summary: Xmu Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
Xmu Library

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Requires: libx11-devel >= 1.0.0
Requires: libxt-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Provides: libxmu-devel = %{version}-%{release}
Provides: libxmu6-devel = %{version}-%{release}
Obsoletes: %{mklibname xmu 6 -d}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libXmuu.so
%{_libdir}/libXmu.so
%{_libdir}/libXmuu.la
%{_libdir}/libXmu.la
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

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}-%{release}
Provides: libxmu-static-devel = %{version}-%{release}
Provides: libxmu6-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xmu 6 -s -d}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXmu.a
%{_libdir}/libXmuu.a

#-----------------------------------------------------------

%prep
%setup -q -n libXmu-%{version}

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libXmu.so.6
%{_libdir}/libXmu.so.6.2.0
%{_libdir}/libXmuu.so.1
%{_libdir}/libXmuu.so.1.0.0
