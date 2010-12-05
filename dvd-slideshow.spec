Summary:	Makes a DVD slideshow video
Name:		dvd-slideshow
Version:	0.8.2.2
Release:	%mkrel 2
License:	GPLv2+
Group:		Video
URL:		http://dvd-slideshow.sourceforge.net/
Source0:	http://dl.sourceforge.net/dvd-slideshow/%{name}-%{version}.tar.gz
Requires:	imagemagick
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
%setup -q -n %{name}-%{version}

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
%doc *.txt doc/*.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*


