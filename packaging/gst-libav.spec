Name:       gst-libav
Summary:    Libav plugin for GStreamer
Version:    1.6.1
Release:    2
Group:      Multimedia/Framework
License:    LGPL-2.0+
Source:     %{name}-%{version}.tar.gz
Source100:  common.tar.gz
Source101:  libav.tar.gz
URL:        http://cgit.freedesktop.org/gstreamer/gst-libav
BuildRequires:  gettext
BuildRequires:  which
BuildRequires:  yasm
BuildRequires:  bzip2-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(orc-0.4)

%description
This GStreamer plugin supports a large number of audio and video compression
formats through the use of the libav library.  The plugin contains GStreamer
elements for decoding 90+ formats (AVI, MPEG, OGG, Matroska, ASF, ...),
demuxing 30+ formats and colorspace conversion.


%prep
%setup -q -n gst-libav-%{version}
%setup -q -T -D -a 100
%setup -q -T -D -a 101

%build
NOCONFIGURE=1 ./autogen.sh

export CFLAGS+=" -Wall -g -fPIC\
 -DGST_TIZEN_MODIFICATION\
 -DLIBAV_RANK_MODIFICATION"

%configure  --disable-static \
	--enable-lgpl\
	--prefix=%{_prefix} \
	--with-html-dir=/tmp/dump\
	--with-libav-extra-configure="--disable-demuxer=mm"


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING.LIB
%{_libdir}/gstreamer-1.0/libgstlibav.so


