# revision 27839
# category Package
# catalog-ctan /macros/latex/contrib/bohr
# catalog-date 2012-09-27 15:23:41 +0200
# catalog-license lppl1.3
# catalog-version 0.2b
Name:		texlive-bohr
Version:	0.2b
Release:	2
Summary:	Simple atom representation according to the Bohr model
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bohr
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bohr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bohr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides means for the creation of simple Bohr
models of atoms up to the atomic number 112. In addition,
commands are provided to convert atomic numbers to element
symbols or element names and vice versa.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bohr/bohr.sty
%{_texmfdistdir}/tex/latex/bohr/bohr_elements_english.def
%{_texmfdistdir}/tex/latex/bohr/bohr_elements_german.def
%doc %{_texmfdistdir}/doc/latex/bohr/README
%doc %{_texmfdistdir}/doc/latex/bohr/bohr_en.pdf
%doc %{_texmfdistdir}/doc/latex/bohr/bohr_en.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
