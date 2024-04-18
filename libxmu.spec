# libXmu is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 6
%define u_major 1
%define libname %mklibname xmu %{major}
%define libu %mklibname xmuu %{u_major}
%define devname %mklibname xmu -d

%if %{with compat32}
%define lib32name libxmu%{major}
%define lib32u libxmuu%{u_major}
%define dev32name libxmu-devel
%endif

Summary:	Xmu Library
Name:		libxmu
Version:	1.2.1
Release:	1
Group:		Development/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.xz

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xt)
%if %{with compat32}
BuildRequires:	libc6
BuildRequires:	devel(libuuid)
BuildRequires:	devel(libX11)
BuildRequires:	devel(libXext)
BuildRequires:	devel(libXt)
BuildRequires:	devel(libxcb)
BuildRequires:	devel(libXau)
BuildRequires:	devel(libXdmcp)
BuildRequires:	devel(libICE)
BuildRequires:	devel(libSM)
%endif

%description
Xmu Library.

%package -n %{libname}
Summary:	Xmu Library
Group:		Development/X11

%description -n %{libname}
Xmu Library.

%package -n %{libu}
Summary:	Xmuu Library
Group:		Development/X11
Conflicts:	%{libname} < 1.1.0-4

%description -n %{libu}
Xmuu Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libu} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Xmu Library (32-bit)
Group:		Development/X11

%description -n %{lib32name}
Xmu Library.

%package -n %{lib32u}
Summary:	Xmuu Library (32-bit)
Group:		Development/X11

%description -n %{lib32u}
Xmuu Library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}-%{release}
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{lib32u} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXmu-%{version} -p1
autoreconf -ifs
export CONFIGURE_TOP="$(pwd)"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXmu.so.%{major}*

%files -n %{libu}
%{_libdir}/libXmuu.so.%{u_major}*

%files -n %{devname}
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
%doc %{_datadir}/doc/libXmu

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXmu.so.%{major}*

%files -n %{lib32u}
%{_prefix}/lib/libXmuu.so.%{u_major}*

%files -n %{dev32name}
%{_prefix}/lib/libXmuu.so
%{_prefix}/lib/libXmu.so
%{_prefix}/lib/pkgconfig/xmuu.pc
%{_prefix}/lib/pkgconfig/xmu.pc
%endif
