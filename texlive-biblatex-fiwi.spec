# revision 24913
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-fiwi
# catalog-date 2011-12-22 11:25:03 +0100
# catalog-license lppl1.3
# catalog-version 1.1d
Name:		texlive-biblatex-fiwi
Version:	1.1d
Release:	2
Summary:	Biblatex styles for use in German humanities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-fiwi
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-fiwi.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-fiwi.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a collection of styles for biblatex
(version 1.7 is required, currently). It was designed for
citations in German Humanities, especially film studies, and
offers some features that are not provided by the standard
biblatex styles. The style is highly optimized for documents
written in German, and the main documentation is only available
in German.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi-yearbeginning.bbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi.bbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi.cbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi2.bbx
%{_texmfdistdir}/tex/latex/biblatex-fiwi/fiwi2.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/README
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/biblatex-fiwi.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/biblatex-fiwi.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi-options.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi-options.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi2-options.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi2.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/example-biblatex-fiwi2.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi/examples.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
