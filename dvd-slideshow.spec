%define		vmajor 0.8.4
%define		vminor 2

Summary:	Makes a DVD slideshow video
Name:		dvd-slideshow
Version:	%{vmajor}.%{vminor}
Release:	%mkrel 1
License:	GPLv2+
Group:		Video
URL:		http://dvd-slideshow.sourceforge.net/
Source0:	http://dl.sourceforge.net/dvd-slideshow/%{name}-%{vmajor}-%{vminor}.tar.gz
Requires:	imagemagick
Requires:	dvdauthor >= 0.6.13
Requires:	mjpegtools
Requires:	sox >= 14.0
Requires:	ffmpeg
Suggests:	lame
Suggests:	oggdec
BuildArch:	noarch

%description
dvd-slideshow makes a DVD slideshow video with menus from a text
file listing of pictures, effects, and audio tracks. You can add
some nice effects like fades, crops, scrolls, or Ken Burns effects.
It will hopefully become a command-line clone of imovie.

%prep
%setup -q -n %{name}-%{vmajor}-%{vminor}

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




%changelog
* Wed Jan 11 2012 Andrey Bondrov <abondrov@mandriva.org> 0.8.4.2-1mdv2012.0
+ Revision: 759690
- New version 0.8.4.2, update Requires and Suggests

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.2.2-2mdv2011.0
+ Revision: 610315
- rebuild

* Tue Feb 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.8.2.2-1mdv2010.1
+ Revision: 509975
- fix version

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 333174
- 0.8.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.8.0-4mdv2009.0
+ Revision: 244572
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.8.0-2mdv2008.1
+ Revision: 168487
- rebuild
- fix summary

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.8.0-1mdv2008.1
+ Revision: 140722
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.8.0-1mdv2007.0
+ Revision: 118390
- Import dvd-slideshow

