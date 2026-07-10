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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a collection of styles for BibLaTeX (version 3.5 is
required, currently). It was designed for citations in German
Humanities, especially film studies, and offers some features that are
not provided by the standard BibLaTeX styles. The style is highly
optimized for documents written in German, and the main documentation is
only available in German.

