%global tl_name biblatex-fiwi
%global tl_revision 45876

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	BibLaTeX styles for use in German humanities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-fiwi
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-fiwi.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-fiwi.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a collection of styles for BibLaTeX (version 3.5 is
required, currently). It was designed for citations in German
Humanities, especially film studies, and offers some features that are
not provided by the standard BibLaTeX styles. The style is highly
optimized for documents written in German, and the main documentation is
only available in German.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-fiwi
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/biblatex-fiwi.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/biblatex-fiwi.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/diss.xdy
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/dissff.xdy
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi-options.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi-options.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi-xindy.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi-xindy.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi2-options.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/example-biblatex-fiwi2-options.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-fiwi/examples.bib
%{_datadir}/texmf-dist/tex/latex/biblatex-fiwi/fiwi-yearbeginning.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-fiwi/fiwi.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-fiwi/fiwi.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-fiwi/fiwi.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-fiwi/fiwi2.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-fiwi/fiwi2.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-fiwi/fiwi2.dbx
