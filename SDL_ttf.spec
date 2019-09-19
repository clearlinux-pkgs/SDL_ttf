#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL_ttf
Version  : 2.0.11
Release  : 14
URL      : https://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-2.0.11.tar.gz
Source0  : https://www.libsdl.org/projects/SDL_ttf/release/SDL_ttf-2.0.11.tar.gz
Summary  : Simple DirectMedia Layer - Sample TrueType Font Library
Group    : Development/Tools
License  : FTL Zlib
Requires: SDL_ttf-lib = %{version}-%{release}
Requires: SDL_ttf-license = %{version}-%{release}
BuildRequires : SDL-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32freetype2)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(freetype2)

%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package dev
Summary: dev components for the SDL_ttf package.
Group: Development
Requires: SDL_ttf-lib = %{version}-%{release}
Provides: SDL_ttf-devel = %{version}-%{release}
Requires: SDL_ttf = %{version}-%{release}

%description dev
dev components for the SDL_ttf package.


%package dev32
Summary: dev32 components for the SDL_ttf package.
Group: Default
Requires: SDL_ttf-lib32 = %{version}-%{release}
Requires: SDL_ttf-dev = %{version}-%{release}

%description dev32
dev32 components for the SDL_ttf package.


%package lib
Summary: lib components for the SDL_ttf package.
Group: Libraries
Requires: SDL_ttf-license = %{version}-%{release}

%description lib
lib components for the SDL_ttf package.


%package lib32
Summary: lib32 components for the SDL_ttf package.
Group: Default
Requires: SDL_ttf-license = %{version}-%{release}

%description lib32
lib32 components for the SDL_ttf package.


%package license
Summary: license components for the SDL_ttf package.
Group: Default

%description license
license components for the SDL_ttf package.


%prep
%setup -q -n SDL_ttf-2.0.11
pushd ..
cp -a SDL_ttf-2.0.11 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568877211
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1568877211
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL_ttf
cp COPYING %{buildroot}/usr/share/package-licenses/SDL_ttf/COPYING
cp VisualC/external/lib/x64/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x64_LICENSE.freetype.txt
cp VisualC/external/lib/x64/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x64_LICENSE.zlib.txt
cp VisualC/external/lib/x86/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x86_LICENSE.freetype.txt
cp VisualC/external/lib/x86/LICENSE.zlib.txt %{buildroot}/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x86_LICENSE.zlib.txt
cp Xcode/Frameworks/FreeType.framework/LICENSE.freetype.txt %{buildroot}/usr/share/package-licenses/SDL_ttf/Xcode_Frameworks_FreeType.framework_LICENSE.freetype.txt
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL_ttf/COPYING
/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x64_LICENSE.freetype.txt
/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x64_LICENSE.zlib.txt
/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x86_LICENSE.freetype.txt
/usr/share/package-licenses/SDL_ttf/VisualC_external_lib_x86_LICENSE.zlib.txt
/usr/share/package-licenses/SDL_ttf/Xcode_Frameworks_FreeType.framework_LICENSE.freetype.txt
