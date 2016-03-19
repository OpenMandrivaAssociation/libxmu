%define major 6
%define u_major 1
%define libname %mklibname xmu %{major}
%define libu %mklibname xmuu %{u_major}
%define devname %mklibname xmu -d

Summary:	Xmu Library
Name:		libxmu
Version:	1.1.2
Release:	10
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXmu-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xt)

%description
Xmu Library.

%package -n %{libname}
Summary:	Xmu Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

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
Provides:	libxmu-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXmu-%{version}
autoreconf -ifs

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

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
%{_datadir}/doc/libXmu

