Name:		texlive-biblatex-fiwi
Version:	45876
Release:	1
Summary:	Biblatex styles for use in German humanities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-fiwi
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-fiwi.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-fiwi.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/biblatex-fiwi
%doc %{_texmfdistdir}/doc/latex/biblatex-fiwi

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
