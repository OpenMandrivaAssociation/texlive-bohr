Name:		texlive-bohr
Version:	62977
Release:	2
Summary:	Simple atom representation according to the Bohr model
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bohr
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bohr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bohr.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/bohr
%doc %{_texmfdistdir}/doc/latex/bohr

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
