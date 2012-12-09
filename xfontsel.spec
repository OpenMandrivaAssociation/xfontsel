Name: xfontsel
Version: 1.0.4
Release: %mkrel 1
Summary: Point and click selection of X11 font names
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xfontsel application provides a simple way to display the fonts known to
your X server, examine samples of each, and retrieve the X Logical Font
Description ("XLFD") full name for a font.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xfontsel
%{_datadir}/X11/app-defaults/XFontSel
%{_mandir}/man1/xfontsel.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 671312
- mass rebuild

* Mon Sep 27 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 581413
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdv2010.1
+ Revision: 524443
- rebuilt for 2010.1

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.2-5mdv2009.1
+ Revision: 366634
- no more autoconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 226038
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 154751
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 130180
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode lzma extension!!!

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.


* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2007.0
+ Revision: 116221
- new upstream release: 1.0.3

* Sat Sep 02 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-5mdv2007.0
+ Revision: 59439
- rebuild to fix libXaw.so.8 dependency
- rebuild to fix cooker uploading
- rebuild against new libXaw package\n- fixed description and summary
- increment release
- Adding X.org 7.0 to the repository

  + Thierry Vignaud <tvignaud@mandriva.com>
    - better description

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

