#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL_ttf
Version  : 2.0.11
Release  : 7
URL      : https://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-2.0.11.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-2.0.11.tar.gz
Summary  : Simple DirectMedia Layer - Sample TrueType Font Library
Group    : Development/Tools
License  : FTL Zlib
Requires: SDL_ttf-lib
BuildRequires : SDL-dev
BuildRequires : SDL-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : mesa-dev
BuildRequires : mesa-dev32
BuildRequires : pkgconfig(32freetype2)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(ice)

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package dev
Summary: dev components for the SDL_ttf package.
Group: Development
Requires: SDL_ttf-lib
Provides: SDL_ttf-devel

%description dev
dev components for the SDL_ttf package.


%package dev32
Summary: dev32 components for the SDL_ttf package.
Group: Default
Requires: SDL_ttf-lib32
Requires: SDL_ttf-dev

%description dev32
dev32 components for the SDL_ttf package.


%package lib
Summary: lib components for the SDL_ttf package.
Group: Libraries

%description lib
lib components for the SDL_ttf package.


%package lib32
Summary: lib32 components for the SDL_ttf package.
Group: Default

%description lib32
lib32 components for the SDL_ttf package.


%prep
%setup -q -n SDL_ttf-2.0.11
pushd ..
cp -a SDL_ttf-2.0.11 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/SDL/SDL_ttf.h
/usr/lib64/libSDL_ttf.so
/usr/lib64/pkgconfig/SDL_ttf.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libSDL_ttf.so
/usr/lib32/pkgconfig/32SDL_ttf.pc
/usr/lib32/pkgconfig/SDL_ttf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL_ttf-2.0.so.0
/usr/lib64/libSDL_ttf-2.0.so.0.10.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL_ttf-2.0.so.0
/usr/lib32/libSDL_ttf-2.0.so.0.10.1
