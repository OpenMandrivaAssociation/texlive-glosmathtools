Name:		texlive-glosmathtools
Version:	55920
Release:	2
Summary:	Mathematical nomenclature tools based on the glossaries package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/glosmathtools
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glosmathtools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glosmathtools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can be used to generate a mathematical
nomenclature (also called "list of symbols" or "notation"). It
is based on the glossaries package. Its main features are:
symbol categories (e.g.: latin, greek) automatic but
customizable symbol sorting easy subscript management easy
accentuation management abbreviation support (with first use
definition) bilingual nomenclatures (for bilingual documents)
bilingual abbreviations The documentation is based on the
ulthese class. The package itself depends on glossaries,
amsmath, amsfonts, and etoolbox.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/glosmathtools
%doc %{_texmfdistdir}/doc/latex/glosmathtools

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
