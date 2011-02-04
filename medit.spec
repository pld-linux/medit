# TODO
# - contains modified Lua-5.1.3, try to use system?
# - gtk-doc instead of %doc doc/help
# - /usr/share/mime/* is suspicious
Summary:	Multiplatform GTK+2 text editor
Summary(pl.UTF-8):	Wieloplatformowy edytor tekstu
Name:		medit
Version:	0.9.3
Release:	0.1
License:	GPL
Group:		X11/Applications/Editors
Source0:	http://downloads.sourceforge.net/mooedit/%{name}-%{version}.tar.bz2
# Source0-md5:	24ffe177248e94795345a11a1a668741
URL:		http://mooedit.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.2.0
BuildRequires:	intltool
BuildRequires:	libxml2-devel
BuildRequires:	pcre-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	rpmbuild(find_lang) >= 1.32
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Medit is a multiplatform GTK+2 text editor. Features:
- Configurable syntax highlighting
- Configurable keyboard accelerators
- Multiplatform - works both on unix and windows

%description -l pl.UTF-8
Medit to wieloplatformowy editor tekstu. Cechy:
- Konfigurowalne podświetlanie składni
- Konfigurowalne skróty klawiszowe
- Wieloplatformowość - działa zarówno na systemie Unix jak i
  Windows

%prep
%setup -q

%build
%configure \
	--with-xml \
	--with-python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/mime/mime.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
rm -rf $RPM_BUILD_ROOT%{_docdir}/medit

%find_lang moo-gsv -o %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%update_icon_cache hicolor

%postun
%update_mime_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING.GPL INSTALL LICENSE NEWS README THANKS doc/help
%attr(755,root,root) %{_bindir}/medit
%dir %{_libdir}/moo
%{_libdir}/moo/plugins
%dir %{_datadir}/moo
%{_datadir}/moo/language-specs
%{_datadir}/moo/lua
%{_datadir}/moo/*.cfg
%{_datadir}/moo/*.xml
%dir %{_datadir}/moo/scripts
%attr(755,root,root) %{_datadir}/moo/scripts/moo-open-html-help
%attr(755,root,root) %{_datadir}/moo/scripts/xdg-email
%attr(755,root,root) %{_datadir}/moo/scripts/xdg-open

# XXX is packaging these ok?
%{_datadir}/mime/XMLnamespaces
%{_datadir}/mime/aliases
%{_datadir}/mime/globs
%{_datadir}/mime/magic
%{_datadir}/mime/packages/moo.xml
%{_datadir}/mime/subclasses
%{_datadir}/mime/text/x-automake.xml
%{_datadir}/mime/text/x-configure-in.xml
%{_datadir}/mime/text/x-copying.xml
%{_datadir}/mime/text/x-dpatch.xml
%{_datadir}/mime/text/x-gap.xml
%{_datadir}/mime/text/x-libtool.xml
%{_datadir}/mime/text/x-news.xml
%{_datadir}/mime/text/x-pkg-config.xml
%{_datadir}/mime/text/x-thanks.xml
%{_datadir}/mime/text/x-todo.xml

%{_desktopdir}/medit.desktop
%{_iconsdir}/hicolor/*/apps/medit.png
%{_pixmapsdir}/medit.png
%{_mandir}/man1/medit*
