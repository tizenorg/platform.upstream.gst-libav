Name:       gst-ffmpeg
Summary:    FFmpeg plugin for GStreamer
Version:    0.10.11
Release:    1
Group:      TO_BE/FILLED_IN
License:    LGPLv2+
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/gst-ffmpeg.manifest 

BuildRequires:  gettext
BuildRequires:  which
BuildRequires:  prelink
BuildRequires:  gstreamer-tools
BuildRequires:  gst-plugins-base-devel  
BuildRequires:  pkgconfig(gstreamer-0.10) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(liboil-0.3)
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

%build
cp %{SOURCE1001} .
./autogen.sh 
%configure  --disable-static \
	--disable-nls \
	--enable-swscale \
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
