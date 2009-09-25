%define libxmu %mklibname xmu 6
Name: libxmu
Summary: Xmu Library
Version: 1.0.5
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xmu Library

#-----------------------------------------------------------

%package -n %{libxmu}
Summary: Xmu Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxmu}
Xmu Library

#-----------------------------------------------------------

%package -n %{libxmu}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxmu} = %{version}
Requires: libx11-devel >= 1.0.0
Requires: libxt-devel >= 1.0.0
Requires: x11-proto-devel >= 1.0.0
Provides: libxmu-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxmu}-devel
Development files for %{name}

%pre -n %{libxmu}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxmu}-devel
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

#-----------------------------------------------------------

%package -n %{libxmu}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxmu}-devel = %{version}
Provides: libxmu-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxmu}-static-devel
Static development files for %{name}

%files -n %{libxmu}-static-devel
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

%files -n %{libxmu}
%defattr(-,root,root)
%{_libdir}/libXmu.so.6
%{_libdir}/libXmu.so.6.2.0
%{_libdir}/libXmuu.so.1
%{_libdir}/libXmuu.so.1.0.0
