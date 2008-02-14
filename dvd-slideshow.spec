%define _rel	-1
Summary:	Makes a DVD slideshow video
Name:		dvd-slideshow
Version:	0.8.0
Release:	%mkrel 1
License:	GPL
Group:		Video
URL:		http://dvd-slideshow.sourceforge.net/
Source0:	http://dl.sourceforge.net/dvd-slideshow/%{name}-%{version}%{_rel}.tar.bz2
Requires:	ImageMagick
Requires:	dvdauthor	>= 0.6.13
Requires:	mjpegtools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
dvd-slideshow makes a DVD slideshow video with menus from a text
file listing of pictures, effects, and audio tracks. You can add
some nice effects like fades, crops, scrolls, or Ken Burns effects.
It will hopefully become a command-line clone of imovie.

%prep
%setup -q -n %{name}-%{version}%{_rel}

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install -d  %{buildroot}{%{_bindir},%{_mandir}/man1}

install dir2slideshow %{buildroot}%{_bindir}
install dvd-menu %{buildroot}%{_bindir}
install dvd-slideshow %{buildroot}%{_bindir}
install gallery1-to-slideshow %{buildroot}%{_bindir}
install jigl2slideshow %{buildroot}%{_bindir}
install man/* %{buildroot}%{_mandir}/man1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc *.txt *.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*


