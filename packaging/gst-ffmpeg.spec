#sbs-git:slp/pkgs/g/gstreamer0.10-ffmpeg gst-ffmpeg 0.10.11 eab91d2292960a6c9af3b27ca939ad65a4418984
Name:       gst-ffmpeg
Summary:    FFmpeg plugin for GStreamer
Version:    0.10.11
Release:    18
Group:      Application/Multimedia
License:    LGPLv2+
Source0:    %{name}-%{version}.tar.gz
#Patch0:     gst-ffmpeg-autotools.patch
#Patch1:     gst-ffmpeg-ffmux-ehancement.patch
#Patch2:     gst-ffmpeg-swscale-pc.patch
BuildRequires:  gettext
BuildRequires:  which
BuildRequires:  gstreamer-tools
BuildRequires:  gst-plugins-base-devel  
BuildRequires:  pkgconfig(gstreamer-0.10) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(theora)

%description
This GStreamer plugin supports a large number of audio and video compression
formats through the use of the FFmpeg library.  The plugin contains GStreamer
elements for decoding 90+ formats (AVI, MPEG, OGG, Matroska, ASF, ...),
demuxing 30+ formats and colorspace conversion.


%prep
%setup -q 
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
./autogen.sh 

export CFLAGS+=" -Wall -g -fPIC\
 -DFFDEC_RANK_MODIFICATION"

%configure  --disable-static \
	--disable-nls \
	--prefix=%{_prefix} \
	--with-html-dir=/tmp/dump


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%files
%manifest gst-ffmpeg.manifest
%defattr(-,root,root,-)
/usr/lib/gstreamer-0.10/libgstffmpeg.so
