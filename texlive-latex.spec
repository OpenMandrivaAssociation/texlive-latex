Name:		texlive-latex
Version:	20180529
Release:	1
Summary:	A TeX macro package that defines LaTeX
Group:		Publishing
URL:		http://tug.org/texlive
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-luatex
Requires:	texlive-pdftex
Requires:	texlive-latexconfig
Requires:	texlive-latex-fonts

%description
LaTeX is a widely-used macro package for TeX, providing many
basic document formating commands extended by a wide range of
packages. It is a development of Leslie Lamport's LaTeX 2.09,
and superseded the older system in June 1994. The basic
distribution is catalogued separately, at latex-base; apart
from a large set of contributed packages and third-party
documentation (elsewhere on the archive), the distribution
includes: - a bunch of required packages, which LaTeX authors
are "entitled to assume" will be present on any system running
LaTeX; and - a minimal set of documentation detailing
differences from the 'old' version of LaTeX in the areas of
user commands, font selection and control, class and package
writing, font encodings, configuration options and modification
of LaTeX. For downloading details, see the linked catalogue
entries above.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/latex
%{_texmfdistdir}/tex/latex
%doc %{_texmfdistdir}/doc/latex
#- source
%doc %{_texmfdistdir}/source/latex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
