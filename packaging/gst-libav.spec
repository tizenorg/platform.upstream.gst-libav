Name:       gst-libav
Summary:    Libav plugin for GStreamer
Version:    1.0.7
Release:    1
Group:      Multimedia/Libraries
License:    GPL-2.0
Source0:    %{name}-%{version}.tar.gz
URL:        http://cgit.freedesktop.org/gstreamer/gst-libav
BuildRequires:  gettext
BuildRequires:  which
BuildRequires:  yasm
BuildRequires:  gst-common
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
%setup -q
rm -rf common
cp -a %{_datadir}/gst-common common
find common -exec touch {} \;

%build
./autogen.sh

export CFLAGS+=" -Wall -g -fPIC\
 -DLIBAV_RANK_MODIFICATION"

%configure  --disable-static \
	--prefix=%{_prefix} \
	--with-html-dir=/tmp/dump


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-1.0/libgstlibav.so
%{_libdir}/gstreamer-1.0/libgstavscale.so