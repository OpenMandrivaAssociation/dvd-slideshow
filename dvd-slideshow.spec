%define		vmajor 0.8.4
%define		vminor 2

Summary:	Makes a DVD slideshow video
Name:		dvd-slideshow
Version:	%{vmajor}.%{vminor}
Release:	9
License:	GPLv2+
Group:		Video
Url:		http://dvd-slideshow.sourceforge.net/
Source0:	http://dl.sourceforge.net/dvd-slideshow/%{name}-%{vmajor}-%{vminor}.tar.gz
BuildArch:	noarch

Requires:	dvdauthor >= 0.6.13
Requires:	ffmpeg
Requires:	imagemagick
Requires:	mjpegtools
Requires:	sox >= 14.0
Suggests:	lame
Suggests:	oggdec

%description
dvd-slideshow makes a DVD slideshow video with menus from a text
file listing of pictures, effects, and audio tracks. You can add
some nice effects like fades, crops, scrolls, or Ken Burns effects.
It will hopefully become a command-line clone of imovie.

%prep
%setup -qn %{name}-%{vmajor}-%{vminor}

%install
install -d  %{buildroot}{%{_bindir},%{_mandir}/man1}

install dir2slideshow %{buildroot}%{_bindir}
install dvd-menu %{buildroot}%{_bindir}
install dvd-slideshow %{buildroot}%{_bindir}
install gallery1-to-slideshow %{buildroot}%{_bindir}
install jigl2slideshow %{buildroot}%{_bindir}
install man/* %{buildroot}%{_mandir}/man1

%files
%doc *.txt doc/*.html
%{_bindir}/*
%{_mandir}/man1/*

