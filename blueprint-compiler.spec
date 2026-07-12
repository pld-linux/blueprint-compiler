Summary:	Markup language for GTK user interface files
Summary(pl.UTF-8):	Język znaczników dla plików interfejsów użytkownika GTK
Name:		blueprint-compiler
Version:	0.22.1
Release:	1
License:	LGPL v3+
Group:		Development/Tools
# if not released with gnome downloads:
##Source0Download: https://gitlab.gnome.org/GNOME/blueprint-compiler/-/releases
#Source0:	https://gitlab.gnome.org/GNOME/blueprint-compiler/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source0:	https://download.gnome.org/sources/blueprint-compiler/0.22/%{name}-%{version}.tar.xz
# Source0-md5:	373d8c064de8af7d09f2fa03a044fc9f
URL:		https://gnome.pages.gitlab.gnome.org/blueprint-compiler/
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	python3 >= 1:3.9
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gobject-introspection
Requires:	python3-pygobject3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkBuilder XML format is quite verbose, and many app developers don't
like using WYSIWYG editors for creating UIs. Blueprint files are
intended to be a concise, easy-to-read format that makes it easier to
create and edit GTK UIs.

Internally, it compiles to GtkBuilder XML as part of an app's build
system. It adds no new features, just makes the features that exist
more accessible.

%description -l pl.UTF-8
Format GtkBuilder XML jest dosyć szczegółowy, a programiści wielu
aplikacji nie lubią korzystać z edytorów WYSIWYG do tworzenia
interfejsów użytkownika. Pliki Blueprint są z założenia zwięzłym,
łatwym do czytania formatem, ułatwiającym tworzenie i edycję
interfejsów użytkownika GTK.

Wewnętrznie program kompiluje do formatu GtkBuilderXML XML jako część
systemu budowania aplikacji. Nie dodaje nowych możliwości, po prostu
ułatwia dostęp do istniejących.

%prep
%setup -q

%build
%meson \
	-Ddocs=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS.md README.md
%attr(755,root,root) %{_bindir}/blueprint-compiler
%{py3_sitescriptdir}/blueprintcompiler
%{_npkgconfigdir}/blueprint-compiler.pc
