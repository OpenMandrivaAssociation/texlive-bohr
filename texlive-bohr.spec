%global tl_name bohr
%global tl_revision 62977

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Simple atom representation according to the Bohr model
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bohr
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bohr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bohr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides means for the creation of simple Bohr models of
atoms up to the atomic number 112. In addition, commands are provided to
convert atomic numbers to element symbols or element names and vice
versa.

