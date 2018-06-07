#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7180713BE58D1ADC
#
Name     : vlc
Version  : 3.0.3
Release  : 20
URL      : http://get.videolan.org/vlc/3.0.3/vlc-3.0.3.tar.xz
Source0  : http://get.videolan.org/vlc/3.0.3/vlc-3.0.3.tar.xz
Source99 : http://get.videolan.org/vlc/3.0.3/vlc-3.0.3.tar.xz.asc
Summary  : VLC media player external control library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 WTFPL
Requires: vlc-bin
Requires: vlc-lib
Requires: vlc-data
Requires: vlc-doc
Requires: vlc-locales
BuildRequires : SDL2_image-dev
BuildRequires : SDL_image-dev
BuildRequires : bison
BuildRequires : desktop-file-utils
BuildRequires : flac-dev
BuildRequires : flex
BuildRequires : fribidi-dev
BuildRequires : gettext
BuildRequires : libgcrypt-dev
BuildRequires : libidn-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libnotify-dev
BuildRequires : libogg-dev
BuildRequires : librsvg-dev
BuildRequires : libsamplerate-dev
BuildRequires : libtheora-dev
BuildRequires : libxml2-dev
BuildRequires : mpg123-dev
BuildRequires : opencv-dev
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
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(speexdsp)
BuildRequires : pkgconfig(udev)
BuildRequires : pkgconfig(vorbis)
BuildRequires : pkgconfig(vpx)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-keysyms)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xpm)
BuildRequires : qtbase-dev
BuildRequires : qtbase-extras
BuildRequires : samba-dev
BuildRequires : speex-dev
BuildRequires : unzip
BuildRequires : yasm
Patch1: build.patch
Patch2: 0001-qt-fix-build-against-Qt-5.11.patch

%description
===============================
VLC is a popular libre and open source media player and multimedia engine,
used by a large number of individuals, professionals, companies and
institutions. Using open source technologies and libraries, VLC has been
ported to most computing platforms, including GNU/Linux, Windows, Mac OS X,
BSD, iOS and Android.
VLC can play most multimedia files, discs, streams, allows playback from
devices, and is able to convert to or stream in various formats.
The VideoLAN project was started at the university Ãcole Centrale Paris who
relicensed VLC under the GPLv2 license in February 2001. Since then, VLC has
been downloaded close to one billion times.

%package bin
Summary: bin components for the vlc package.
Group: Binaries
Requires: vlc-data

%description bin
bin components for the vlc package.


%package data
Summary: data components for the vlc package.
Group: Data

%description data
data components for the vlc package.


%package dev
Summary: dev components for the vlc package.
Group: Development
Requires: vlc-lib
Requires: vlc-bin
Requires: vlc-data
Provides: vlc-devel

%description dev
dev components for the vlc package.


%package doc
Summary: doc components for the vlc package.
Group: Documentation

%description doc
doc components for the vlc package.


%package lib
Summary: lib components for the vlc package.
Group: Libraries
Requires: vlc-data

%description lib
lib components for the vlc package.


%package locales
Summary: locales components for the vlc package.
Group: Default

%description locales
locales components for the vlc package.


%prep
%setup -q -n vlc-3.0.3
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528410574
%configure --disable-static --disable-mad \
--disable-avcodec \
--disable-swscale \
--disable-a52 \
--disable-lua \
--disable-libgcrypt \
--enable-smbclient \
BUILDCC=/usr/bin/gcc
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1528410574
rm -rf %{buildroot}
%make_install
%find_lang vlc

%files
%defattr(-,root,root,-)
/usr/lib64/vlc/plugins/plugins.dat
/usr/lib64/vlc/vlc-cache-gen

%files bin
%defattr(-,root,root,-)
/usr/bin/cvlc
/usr/bin/nvlc
/usr/bin/qvlc
/usr/bin/rvlc
/usr/bin/vlc
/usr/bin/vlc-wrapper

%files data
%defattr(-,root,root,-)
/usr/share/applications/vlc.desktop
/usr/share/icons/hicolor/128x128/apps/vlc-kb.png
/usr/share/icons/hicolor/128x128/apps/vlc-xmas.png
/usr/share/icons/hicolor/128x128/apps/vlc.png
/usr/share/icons/hicolor/16x16/apps/vlc.png
/usr/share/icons/hicolor/16x16/apps/vlc.xpm
/usr/share/icons/hicolor/256x256/apps/vlc.png
/usr/share/icons/hicolor/32x32/apps/vlc-xmas.xpm
/usr/share/icons/hicolor/32x32/apps/vlc.png
/usr/share/icons/hicolor/32x32/apps/vlc.xpm
/usr/share/icons/hicolor/48x48/apps/vlc-xmas.png
/usr/share/icons/hicolor/48x48/apps/vlc.png
/usr/share/kde4/apps/solid/actions/vlc-openbd.desktop
/usr/share/kde4/apps/solid/actions/vlc-opencda.desktop
/usr/share/kde4/apps/solid/actions/vlc-opendvd.desktop
/usr/share/kde4/apps/solid/actions/vlc-openvcd.desktop
/usr/share/metainfo/vlc.appdata.xml
/usr/share/vlc/utils/audio-vlc-default.sh
/usr/share/vlc/utils/gnome-vlc-default.sh
/usr/share/vlc/utils/video-vlc-default.sh
/usr/share/vlc/vlc.ico

%files dev
%defattr(-,root,root,-)
/usr/include/vlc/deprecated.h
/usr/include/vlc/libvlc.h
/usr/include/vlc/libvlc_dialog.h
/usr/include/vlc/libvlc_events.h
/usr/include/vlc/libvlc_media.h
/usr/include/vlc/libvlc_media_discoverer.h
/usr/include/vlc/libvlc_media_library.h
/usr/include/vlc/libvlc_media_list.h
/usr/include/vlc/libvlc_media_list_player.h
/usr/include/vlc/libvlc_media_player.h
/usr/include/vlc/libvlc_renderer_discoverer.h
/usr/include/vlc/libvlc_version.h
/usr/include/vlc/libvlc_vlm.h
/usr/include/vlc/plugins/vlc_about.h
/usr/include/vlc/plugins/vlc_access.h
/usr/include/vlc/plugins/vlc_actions.h
/usr/include/vlc/plugins/vlc_addons.h
/usr/include/vlc/plugins/vlc_aout.h
/usr/include/vlc/plugins/vlc_aout_volume.h
/usr/include/vlc/plugins/vlc_arrays.h
/usr/include/vlc/plugins/vlc_atomic.h
/usr/include/vlc/plugins/vlc_avcodec.h
/usr/include/vlc/plugins/vlc_bits.h
/usr/include/vlc/plugins/vlc_block.h
/usr/include/vlc/plugins/vlc_block_helper.h
/usr/include/vlc/plugins/vlc_boxes.h
/usr/include/vlc/plugins/vlc_charset.h
/usr/include/vlc/plugins/vlc_codec.h
/usr/include/vlc/plugins/vlc_common.h
/usr/include/vlc/plugins/vlc_config.h
/usr/include/vlc/plugins/vlc_config_cat.h
/usr/include/vlc/plugins/vlc_configuration.h
/usr/include/vlc/plugins/vlc_cpu.h
/usr/include/vlc/plugins/vlc_demux.h
/usr/include/vlc/plugins/vlc_dialog.h
/usr/include/vlc/plugins/vlc_epg.h
/usr/include/vlc/plugins/vlc_es.h
/usr/include/vlc/plugins/vlc_es_out.h
/usr/include/vlc/plugins/vlc_events.h
/usr/include/vlc/plugins/vlc_filter.h
/usr/include/vlc/plugins/vlc_fingerprinter.h
/usr/include/vlc/plugins/vlc_fourcc.h
/usr/include/vlc/plugins/vlc_fs.h
/usr/include/vlc/plugins/vlc_gcrypt.h
/usr/include/vlc/plugins/vlc_http.h
/usr/include/vlc/plugins/vlc_httpd.h
/usr/include/vlc/plugins/vlc_image.h
/usr/include/vlc/plugins/vlc_inhibit.h
/usr/include/vlc/plugins/vlc_input.h
/usr/include/vlc/plugins/vlc_input_item.h
/usr/include/vlc/plugins/vlc_interface.h
/usr/include/vlc/plugins/vlc_interrupt.h
/usr/include/vlc/plugins/vlc_keystore.h
/usr/include/vlc/plugins/vlc_main.h
/usr/include/vlc/plugins/vlc_md5.h
/usr/include/vlc/plugins/vlc_media_library.h
/usr/include/vlc/plugins/vlc_memstream.h
/usr/include/vlc/plugins/vlc_messages.h
/usr/include/vlc/plugins/vlc_meta.h
/usr/include/vlc/plugins/vlc_meta_fetcher.h
/usr/include/vlc/plugins/vlc_mime.h
/usr/include/vlc/plugins/vlc_modules.h
/usr/include/vlc/plugins/vlc_mouse.h
/usr/include/vlc/plugins/vlc_mtime.h
/usr/include/vlc/plugins/vlc_network.h
/usr/include/vlc/plugins/vlc_objects.h
/usr/include/vlc/plugins/vlc_opengl.h
/usr/include/vlc/plugins/vlc_picture.h
/usr/include/vlc/plugins/vlc_picture_fifo.h
/usr/include/vlc/plugins/vlc_picture_pool.h
/usr/include/vlc/plugins/vlc_playlist.h
/usr/include/vlc/plugins/vlc_plugin.h
/usr/include/vlc/plugins/vlc_probe.h
/usr/include/vlc/plugins/vlc_rand.h
/usr/include/vlc/plugins/vlc_renderer_discovery.h
/usr/include/vlc/plugins/vlc_services_discovery.h
/usr/include/vlc/plugins/vlc_sout.h
/usr/include/vlc/plugins/vlc_spu.h
/usr/include/vlc/plugins/vlc_stream.h
/usr/include/vlc/plugins/vlc_stream_extractor.h
/usr/include/vlc/plugins/vlc_strings.h
/usr/include/vlc/plugins/vlc_subpicture.h
/usr/include/vlc/plugins/vlc_text_style.h
/usr/include/vlc/plugins/vlc_threads.h
/usr/include/vlc/plugins/vlc_timestamp_helper.h
/usr/include/vlc/plugins/vlc_tls.h
/usr/include/vlc/plugins/vlc_url.h
/usr/include/vlc/plugins/vlc_variables.h
/usr/include/vlc/plugins/vlc_video_splitter.h
/usr/include/vlc/plugins/vlc_viewpoint.h
/usr/include/vlc/plugins/vlc_vlm.h
/usr/include/vlc/plugins/vlc_vout.h
/usr/include/vlc/plugins/vlc_vout_display.h
/usr/include/vlc/plugins/vlc_vout_osd.h
/usr/include/vlc/plugins/vlc_vout_window.h
/usr/include/vlc/plugins/vlc_xlib.h
/usr/include/vlc/plugins/vlc_xml.h
/usr/include/vlc/vlc.h
/usr/lib64/libvlc.so
/usr/lib64/libvlccore.so
/usr/lib64/pkgconfig/libvlc.pc
/usr/lib64/pkgconfig/vlc-plugin.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/vlc/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvlc.so.5
/usr/lib64/libvlc.so.5.6.0
/usr/lib64/libvlccore.so.9
/usr/lib64/libvlccore.so.9.0.0
/usr/lib64/vlc/libvlc_pulse.so
/usr/lib64/vlc/libvlc_pulse.so.0
/usr/lib64/vlc/libvlc_pulse.so.0.0.0
/usr/lib64/vlc/libvlc_xcb_events.so
/usr/lib64/vlc/libvlc_xcb_events.so.0
/usr/lib64/vlc/libvlc_xcb_events.so.0.0.0
/usr/lib64/vlc/plugins/access/libaccess_alsa_plugin.so
/usr/lib64/vlc/plugins/access/libaccess_concat_plugin.so
/usr/lib64/vlc/plugins/access/libaccess_imem_plugin.so
/usr/lib64/vlc/plugins/access/libaccess_mms_plugin.so
/usr/lib64/vlc/plugins/access/libattachment_plugin.so
/usr/lib64/vlc/plugins/access/libcdda_plugin.so
/usr/lib64/vlc/plugins/access/libdtv_plugin.so
/usr/lib64/vlc/plugins/access/libfilesystem_plugin.so
/usr/lib64/vlc/plugins/access/libftp_plugin.so
/usr/lib64/vlc/plugins/access/libhttp_plugin.so
/usr/lib64/vlc/plugins/access/libhttps_plugin.so
/usr/lib64/vlc/plugins/access/libidummy_plugin.so
/usr/lib64/vlc/plugins/access/libimem_plugin.so
/usr/lib64/vlc/plugins/access/liblinsys_hdsdi_plugin.so
/usr/lib64/vlc/plugins/access/libpulsesrc_plugin.so
/usr/lib64/vlc/plugins/access/librtp_plugin.so
/usr/lib64/vlc/plugins/access/libsatip_plugin.so
/usr/lib64/vlc/plugins/access/libsdp_plugin.so
/usr/lib64/vlc/plugins/access/libshm_plugin.so
/usr/lib64/vlc/plugins/access/libsmb_plugin.so
/usr/lib64/vlc/plugins/access/libtcp_plugin.so
/usr/lib64/vlc/plugins/access/libtimecode_plugin.so
/usr/lib64/vlc/plugins/access/libudp_plugin.so
/usr/lib64/vlc/plugins/access/libv4l2_plugin.so
/usr/lib64/vlc/plugins/access/libvcd_plugin.so
/usr/lib64/vlc/plugins/access/libvdr_plugin.so
/usr/lib64/vlc/plugins/access/libxcb_screen_plugin.so
/usr/lib64/vlc/plugins/access_output/libaccess_output_dummy_plugin.so
/usr/lib64/vlc/plugins/access_output/libaccess_output_file_plugin.so
/usr/lib64/vlc/plugins/access_output/libaccess_output_http_plugin.so
/usr/lib64/vlc/plugins/access_output/libaccess_output_udp_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libaudio_format_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libaudiobargraph_a_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libchorus_flanger_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libcompressor_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libdolby_surround_decoder_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libequalizer_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libgain_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libheadphone_channel_mixer_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libkaraoke_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libmono_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libnormvol_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libparam_eq_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libremap_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libsamplerate_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libscaletempo_pitch_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libscaletempo_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libsimple_channel_mixer_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libspatializer_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libspeex_resampler_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libstereo_widen_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libtospdif_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libtrivial_channel_mixer_plugin.so
/usr/lib64/vlc/plugins/audio_filter/libugly_resampler_plugin.so
/usr/lib64/vlc/plugins/audio_mixer/libfloat_mixer_plugin.so
/usr/lib64/vlc/plugins/audio_mixer/libinteger_mixer_plugin.so
/usr/lib64/vlc/plugins/audio_output/libadummy_plugin.so
/usr/lib64/vlc/plugins/audio_output/libafile_plugin.so
/usr/lib64/vlc/plugins/audio_output/libalsa_plugin.so
/usr/lib64/vlc/plugins/audio_output/libamem_plugin.so
/usr/lib64/vlc/plugins/audio_output/libpulse_plugin.so
/usr/lib64/vlc/plugins/codec/libadpcm_plugin.so
/usr/lib64/vlc/plugins/codec/libaes3_plugin.so
/usr/lib64/vlc/plugins/codec/libaraw_plugin.so
/usr/lib64/vlc/plugins/codec/libcc_plugin.so
/usr/lib64/vlc/plugins/codec/libcdg_plugin.so
/usr/lib64/vlc/plugins/codec/libcvdsub_plugin.so
/usr/lib64/vlc/plugins/codec/libddummy_plugin.so
/usr/lib64/vlc/plugins/codec/libdvbsub_plugin.so
/usr/lib64/vlc/plugins/codec/libedummy_plugin.so
/usr/lib64/vlc/plugins/codec/libflac_plugin.so
/usr/lib64/vlc/plugins/codec/libg711_plugin.so
/usr/lib64/vlc/plugins/codec/libgstdecode_plugin.so
/usr/lib64/vlc/plugins/codec/libjpeg_plugin.so
/usr/lib64/vlc/plugins/codec/liblpcm_plugin.so
/usr/lib64/vlc/plugins/codec/libmpg123_plugin.so
/usr/lib64/vlc/plugins/codec/liboggspots_plugin.so
/usr/lib64/vlc/plugins/codec/libopus_plugin.so
/usr/lib64/vlc/plugins/codec/libpng_plugin.so
/usr/lib64/vlc/plugins/codec/librawvideo_plugin.so
/usr/lib64/vlc/plugins/codec/librtpvideo_plugin.so
/usr/lib64/vlc/plugins/codec/libscte18_plugin.so
/usr/lib64/vlc/plugins/codec/libscte27_plugin.so
/usr/lib64/vlc/plugins/codec/libsdl_image_plugin.so
/usr/lib64/vlc/plugins/codec/libspdif_plugin.so
/usr/lib64/vlc/plugins/codec/libspeex_plugin.so
/usr/lib64/vlc/plugins/codec/libspudec_plugin.so
/usr/lib64/vlc/plugins/codec/libstl_plugin.so
/usr/lib64/vlc/plugins/codec/libsubsdec_plugin.so
/usr/lib64/vlc/plugins/codec/libsubstx3g_plugin.so
/usr/lib64/vlc/plugins/codec/libsubsusf_plugin.so
/usr/lib64/vlc/plugins/codec/libsvcdsub_plugin.so
/usr/lib64/vlc/plugins/codec/libsvgdec_plugin.so
/usr/lib64/vlc/plugins/codec/libt140_plugin.so
/usr/lib64/vlc/plugins/codec/libtelx_plugin.so
/usr/lib64/vlc/plugins/codec/libtextst_plugin.so
/usr/lib64/vlc/plugins/codec/libtheora_plugin.so
/usr/lib64/vlc/plugins/codec/libttml_plugin.so
/usr/lib64/vlc/plugins/codec/libuleaddvaudio_plugin.so
/usr/lib64/vlc/plugins/codec/libvorbis_plugin.so
/usr/lib64/vlc/plugins/codec/libvpx_plugin.so
/usr/lib64/vlc/plugins/codec/libwebvtt_plugin.so
/usr/lib64/vlc/plugins/codec/libxwd_plugin.so
/usr/lib64/vlc/plugins/control/libdbus_plugin.so
/usr/lib64/vlc/plugins/control/libdummy_plugin.so
/usr/lib64/vlc/plugins/control/libgestures_plugin.so
/usr/lib64/vlc/plugins/control/libhotkeys_plugin.so
/usr/lib64/vlc/plugins/control/libmotion_plugin.so
/usr/lib64/vlc/plugins/control/libnetsync_plugin.so
/usr/lib64/vlc/plugins/control/liboldrc_plugin.so
/usr/lib64/vlc/plugins/control/libxcb_hotkeys_plugin.so
/usr/lib64/vlc/plugins/demux/libadaptive_plugin.so
/usr/lib64/vlc/plugins/demux/libaiff_plugin.so
/usr/lib64/vlc/plugins/demux/libasf_plugin.so
/usr/lib64/vlc/plugins/demux/libau_plugin.so
/usr/lib64/vlc/plugins/demux/libavi_plugin.so
/usr/lib64/vlc/plugins/demux/libcaf_plugin.so
/usr/lib64/vlc/plugins/demux/libdemux_cdg_plugin.so
/usr/lib64/vlc/plugins/demux/libdemux_stl_plugin.so
/usr/lib64/vlc/plugins/demux/libdemuxdump_plugin.so
/usr/lib64/vlc/plugins/demux/libdiracsys_plugin.so
/usr/lib64/vlc/plugins/demux/libdirectory_demux_plugin.so
/usr/lib64/vlc/plugins/demux/libes_plugin.so
/usr/lib64/vlc/plugins/demux/libflacsys_plugin.so
/usr/lib64/vlc/plugins/demux/libh26x_plugin.so
/usr/lib64/vlc/plugins/demux/libimage_plugin.so
/usr/lib64/vlc/plugins/demux/libmjpeg_plugin.so
/usr/lib64/vlc/plugins/demux/libmp4_plugin.so
/usr/lib64/vlc/plugins/demux/libmpgv_plugin.so
/usr/lib64/vlc/plugins/demux/libnoseek_plugin.so
/usr/lib64/vlc/plugins/demux/libnsc_plugin.so
/usr/lib64/vlc/plugins/demux/libnsv_plugin.so
/usr/lib64/vlc/plugins/demux/libnuv_plugin.so
/usr/lib64/vlc/plugins/demux/libogg_plugin.so
/usr/lib64/vlc/plugins/demux/libplaylist_plugin.so
/usr/lib64/vlc/plugins/demux/libps_plugin.so
/usr/lib64/vlc/plugins/demux/libpva_plugin.so
/usr/lib64/vlc/plugins/demux/librawaud_plugin.so
/usr/lib64/vlc/plugins/demux/librawdv_plugin.so
/usr/lib64/vlc/plugins/demux/librawvid_plugin.so
/usr/lib64/vlc/plugins/demux/libreal_plugin.so
/usr/lib64/vlc/plugins/demux/libsmf_plugin.so
/usr/lib64/vlc/plugins/demux/libsubtitle_plugin.so
/usr/lib64/vlc/plugins/demux/libtta_plugin.so
/usr/lib64/vlc/plugins/demux/libty_plugin.so
/usr/lib64/vlc/plugins/demux/libvc1_plugin.so
/usr/lib64/vlc/plugins/demux/libvobsub_plugin.so
/usr/lib64/vlc/plugins/demux/libvoc_plugin.so
/usr/lib64/vlc/plugins/demux/libwav_plugin.so
/usr/lib64/vlc/plugins/demux/libxa_plugin.so
/usr/lib64/vlc/plugins/gui/libncurses_plugin.so
/usr/lib64/vlc/plugins/gui/libqt_plugin.so
/usr/lib64/vlc/plugins/keystore/libfile_keystore_plugin.so
/usr/lib64/vlc/plugins/keystore/libkwallet_plugin.so
/usr/lib64/vlc/plugins/keystore/libmemory_keystore_plugin.so
/usr/lib64/vlc/plugins/logger/libconsole_logger_plugin.so
/usr/lib64/vlc/plugins/logger/libfile_logger_plugin.so
/usr/lib64/vlc/plugins/logger/libsd_journal_plugin.so
/usr/lib64/vlc/plugins/logger/libsyslog_plugin.so
/usr/lib64/vlc/plugins/meta_engine/libfolder_plugin.so
/usr/lib64/vlc/plugins/misc/libaddonsfsstorage_plugin.so
/usr/lib64/vlc/plugins/misc/libaddonsvorepository_plugin.so
/usr/lib64/vlc/plugins/misc/libaudioscrobbler_plugin.so
/usr/lib64/vlc/plugins/misc/libdbus_screensaver_plugin.so
/usr/lib64/vlc/plugins/misc/libexport_plugin.so
/usr/lib64/vlc/plugins/misc/libfingerprinter_plugin.so
/usr/lib64/vlc/plugins/misc/libgnutls_plugin.so
/usr/lib64/vlc/plugins/misc/liblogger_plugin.so
/usr/lib64/vlc/plugins/misc/libstats_plugin.so
/usr/lib64/vlc/plugins/misc/libvod_rtsp_plugin.so
/usr/lib64/vlc/plugins/misc/libxdg_screensaver_plugin.so
/usr/lib64/vlc/plugins/misc/libxml_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_asf_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_avi_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_dummy_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_mp4_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_mpjpeg_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_ogg_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_ps_plugin.so
/usr/lib64/vlc/plugins/mux/libmux_wav_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_a52_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_copy_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_dirac_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_dts_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_flac_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_h264_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_hevc_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_mlp_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_mpeg4audio_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_mpeg4video_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_mpegaudio_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_mpegvideo_plugin.so
/usr/lib64/vlc/plugins/packetizer/libpacketizer_vc1_plugin.so
/usr/lib64/vlc/plugins/services_discovery/libmediadirs_plugin.so
/usr/lib64/vlc/plugins/services_discovery/libpodcast_plugin.so
/usr/lib64/vlc/plugins/services_discovery/libpulselist_plugin.so
/usr/lib64/vlc/plugins/services_discovery/libsap_plugin.so
/usr/lib64/vlc/plugins/services_discovery/libudev_plugin.so
/usr/lib64/vlc/plugins/services_discovery/libxcb_apps_plugin.so
/usr/lib64/vlc/plugins/spu/libaudiobargraph_v_plugin.so
/usr/lib64/vlc/plugins/spu/libdynamicoverlay_plugin.so
/usr/lib64/vlc/plugins/spu/liblogo_plugin.so
/usr/lib64/vlc/plugins/spu/libmarq_plugin.so
/usr/lib64/vlc/plugins/spu/libmosaic_plugin.so
/usr/lib64/vlc/plugins/spu/librss_plugin.so
/usr/lib64/vlc/plugins/spu/libsubsdelay_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libadf_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libcache_block_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libcache_read_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libdecomp_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libhds_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libinflate_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libprefetch_plugin.so
/usr/lib64/vlc/plugins/stream_filter/librecord_plugin.so
/usr/lib64/vlc/plugins/stream_filter/libskiptags_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_autodel_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_bridge_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_cycle_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_delay_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_description_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_display_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_dummy_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_duplicate_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_es_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_gather_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_mosaic_bridge_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_record_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_rtp_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_setid_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_smem_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_standard_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_stats_plugin.so
/usr/lib64/vlc/plugins/stream_out/libstream_out_transcode_plugin.so
/usr/lib64/vlc/plugins/text_renderer/libfreetype_plugin.so
/usr/lib64/vlc/plugins/text_renderer/libsvg_plugin.so
/usr/lib64/vlc/plugins/text_renderer/libtdummy_plugin.so
/usr/lib64/vlc/plugins/vaapi/libvaapi_filters_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libchain_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libgrey_yuv_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_10_p010_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_nv12_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_rgb_mmx_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_rgb_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_rgb_sse2_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_yuy2_mmx_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_yuy2_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi420_yuy2_sse2_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi422_i420_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi422_yuy2_mmx_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi422_yuy2_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libi422_yuy2_sse2_plugin.so
/usr/lib64/vlc/plugins/video_chroma/librv32_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libyuvp_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libyuy2_i420_plugin.so
/usr/lib64/vlc/plugins/video_chroma/libyuy2_i422_plugin.so
/usr/lib64/vlc/plugins/video_filter/libadjust_plugin.so
/usr/lib64/vlc/plugins/video_filter/libalphamask_plugin.so
/usr/lib64/vlc/plugins/video_filter/libanaglyph_plugin.so
/usr/lib64/vlc/plugins/video_filter/libantiflicker_plugin.so
/usr/lib64/vlc/plugins/video_filter/libball_plugin.so
/usr/lib64/vlc/plugins/video_filter/libblend_plugin.so
/usr/lib64/vlc/plugins/video_filter/libblendbench_plugin.so
/usr/lib64/vlc/plugins/video_filter/libbluescreen_plugin.so
/usr/lib64/vlc/plugins/video_filter/libcanvas_plugin.so
/usr/lib64/vlc/plugins/video_filter/libcolorthres_plugin.so
/usr/lib64/vlc/plugins/video_filter/libcroppadd_plugin.so
/usr/lib64/vlc/plugins/video_filter/libdeinterlace_plugin.so
/usr/lib64/vlc/plugins/video_filter/libedgedetection_plugin.so
/usr/lib64/vlc/plugins/video_filter/liberase_plugin.so
/usr/lib64/vlc/plugins/video_filter/libextract_plugin.so
/usr/lib64/vlc/plugins/video_filter/libfps_plugin.so
/usr/lib64/vlc/plugins/video_filter/libfreeze_plugin.so
/usr/lib64/vlc/plugins/video_filter/libgaussianblur_plugin.so
/usr/lib64/vlc/plugins/video_filter/libgradfun_plugin.so
/usr/lib64/vlc/plugins/video_filter/libgradient_plugin.so
/usr/lib64/vlc/plugins/video_filter/libgrain_plugin.so
/usr/lib64/vlc/plugins/video_filter/libhqdn3d_plugin.so
/usr/lib64/vlc/plugins/video_filter/libinvert_plugin.so
/usr/lib64/vlc/plugins/video_filter/libmagnify_plugin.so
/usr/lib64/vlc/plugins/video_filter/libmirror_plugin.so
/usr/lib64/vlc/plugins/video_filter/libmotionblur_plugin.so
/usr/lib64/vlc/plugins/video_filter/libmotiondetect_plugin.so
/usr/lib64/vlc/plugins/video_filter/liboldmovie_plugin.so
/usr/lib64/vlc/plugins/video_filter/libopencv_example_plugin.so
/usr/lib64/vlc/plugins/video_filter/libopencv_wrapper_plugin.so
/usr/lib64/vlc/plugins/video_filter/libposterize_plugin.so
/usr/lib64/vlc/plugins/video_filter/libpsychedelic_plugin.so
/usr/lib64/vlc/plugins/video_filter/libpuzzle_plugin.so
/usr/lib64/vlc/plugins/video_filter/libripple_plugin.so
/usr/lib64/vlc/plugins/video_filter/librotate_plugin.so
/usr/lib64/vlc/plugins/video_filter/libscale_plugin.so
/usr/lib64/vlc/plugins/video_filter/libscene_plugin.so
/usr/lib64/vlc/plugins/video_filter/libsepia_plugin.so
/usr/lib64/vlc/plugins/video_filter/libsharpen_plugin.so
/usr/lib64/vlc/plugins/video_filter/libtransform_plugin.so
/usr/lib64/vlc/plugins/video_filter/libvhs_plugin.so
/usr/lib64/vlc/plugins/video_filter/libwave_plugin.so
/usr/lib64/vlc/plugins/video_output/libegl_wl_plugin.so
/usr/lib64/vlc/plugins/video_output/libegl_x11_plugin.so
/usr/lib64/vlc/plugins/video_output/libfb_plugin.so
/usr/lib64/vlc/plugins/video_output/libflaschen_plugin.so
/usr/lib64/vlc/plugins/video_output/libgl_plugin.so
/usr/lib64/vlc/plugins/video_output/libglconv_vaapi_drm_plugin.so
/usr/lib64/vlc/plugins/video_output/libglconv_vaapi_wl_plugin.so
/usr/lib64/vlc/plugins/video_output/libglconv_vaapi_x11_plugin.so
/usr/lib64/vlc/plugins/video_output/libglx_plugin.so
/usr/lib64/vlc/plugins/video_output/libvdummy_plugin.so
/usr/lib64/vlc/plugins/video_output/libvmem_plugin.so
/usr/lib64/vlc/plugins/video_output/libwl_shell_plugin.so
/usr/lib64/vlc/plugins/video_output/libwl_shm_plugin.so
/usr/lib64/vlc/plugins/video_output/libxcb_window_plugin.so
/usr/lib64/vlc/plugins/video_output/libxcb_x11_plugin.so
/usr/lib64/vlc/plugins/video_output/libxcb_xv_plugin.so
/usr/lib64/vlc/plugins/video_output/libxdg_shell_plugin.so
/usr/lib64/vlc/plugins/video_output/libyuv_plugin.so
/usr/lib64/vlc/plugins/video_splitter/libclone_plugin.so
/usr/lib64/vlc/plugins/video_splitter/libpanoramix_plugin.so
/usr/lib64/vlc/plugins/video_splitter/libwall_plugin.so
/usr/lib64/vlc/plugins/visualization/libglspectrum_plugin.so
/usr/lib64/vlc/plugins/visualization/libvisual_plugin.so

%files locales -f vlc.lang
%defattr(-,root,root,-)

