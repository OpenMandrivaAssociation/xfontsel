Summary:	Point and click selection of X11 font names
Name:		xfontsel
Version:	1.0.6
Release:	2
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)

%description
The xfontsel application provides a simple way to display the fonts known to
your X server, examine samples of each, and retrieve the X Logical Font
Description ("XLFD") full name for a font.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xfontsel
%{_datadir}/X11/app-defaults/XFontSel
%{_mandir}/man1/xfontsel.1*

