#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v12
# autospec commit: fbcebd0
#
# Source0 file verified with key 0x7180713BE58D1ADC
#
Name     : vlc
Version  : 3.0.21
Release  : 159
URL      : https://get.videolan.org/vlc/3.0.21/vlc-3.0.21.tar.xz
Source0  : https://get.videolan.org/vlc/3.0.21/vlc-3.0.21.tar.xz
Source1  : https://get.videolan.org/vlc/3.0.21/vlc-3.0.21.tar.xz.asc
Source2  : 7180713BE58D1ADC.pkey
Summary  : VLC media player external control library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 WTFPL
BuildRequires : SDL2_image-dev
BuildRequires : SDL_image-dev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : buildreq-kde
BuildRequires : desktop-file-utils
BuildRequires : file
BuildRequires : flac-dev
BuildRequires : flex
BuildRequires : fluidsynth-dev
BuildRequires : fribidi-dev
BuildRequires : gnupg
BuildRequires : libXinerama-dev
BuildRequires : libarchive-dev
BuildRequires : libgcrypt-dev
BuildRequires : libidn-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libnotify-dev
BuildRequires : libogg-dev
BuildRequires : libplacebo-dev
BuildRequires : librsvg-dev
BuildRequires : libsamplerate-dev
BuildRequires : libsecret-dev
BuildRequires : libtheora-dev
BuildRequires : libva-dev
BuildRequires : libxml2-dev
BuildRequires : llvm
BuildRequires : mediasdk-dev
BuildRequires : mpc-dev
BuildRequires : mpg123-dev
BuildRequires : not-ffmpeg-dev
BuildRequires : opus-dev
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Svg)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : pkgconfig(Qt5X11Extras)
BuildRequires : pkgconfig(SDL_image)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(fribidi)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(gstreamer-app-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libass)
BuildRequires : pkgconfig(libavcodec)
BuildRequires : pkgconfig(libavformat)
BuildRequires : pkgconfig(libavutil)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : pkgconfig(taglib)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vpx)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xpm)
BuildRequires : protobuf-dev
BuildRequires : qtbase-extras
BuildRequires : samba-dev
BuildRequires : sox-dev
BuildRequires : speex-dev
BuildRequires : unzip
BuildRequires : yasm
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: build.patch

%description
===============================
VLC is a popular libre and open source media player and multimedia engine,
used by a large number of individuals, professionals, companies and
institutions. Using open source technologies and libraries, VLC has been
ported to most computing platforms, including GNU/Linux, Windows, Mac OS X,
BSD, iOS and Android.
VLC can play most multimedia files, discs, streams, allows playback from
devices, and is able to convert to or stream in various formats.
The VideoLAN project was started at the university École Centrale Paris who
relicensed VLC under the GPLv2 license in February 2001. Since then, VLC has
been downloaded close to one billion times.

%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 7180713BE58D1ADC' gpg.status
%setup -q -n vlc-3.0.21
cd %{_builddir}/vlc-3.0.21
%patch -P 1 -p1
pushd ..
cp -a vlc-3.0.21 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718382456
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-mad \
--disable-a52 \
--disable-lua \
--disable-libgcrypt \
--disable-opencv \
--disable-postproc \
--enable-avcodec \
--enable-merge-ffmpeg \
--disable-libva \
--enable-gst-decode \
--enable-wayland \
--enable-shared \
--enable-smbclient \
--disable-libplacebo \
BUILDCC=/usr/bin/gcc
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-mad \
--disable-a52 \
--disable-lua \
--disable-libgcrypt \
--disable-opencv \
--disable-postproc \
--enable-avcodec \
--enable-merge-ffmpeg \
--disable-libva \
--enable-gst-decode \
--enable-wayland \
--enable-shared \
--enable-smbclient \
--disable-libplacebo \
BUILDCC=/usr/bin/gcc
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1718382456
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vlc
cp %{_builddir}/vlc-%{version}/COPYING %{buildroot}/usr/share/package-licenses/vlc/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/vlc-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/vlc/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/vlc-%{version}/doc/libvlc/QtPlayer/LICENSE %{buildroot}/usr/share/package-licenses/vlc/6f86a73e06b7329f05554e65f2ae5cfa18cade0f || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/lib64/vlc/plugins/plugins.dat
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
