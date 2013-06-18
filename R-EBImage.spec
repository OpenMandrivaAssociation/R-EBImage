%global packname  EBImage
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          3.10.0
Release:          2
Summary:          Image processing toolbox for R
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-graphics R-stats R-utils R-abind 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-graphics R-stats R-utils R-abind
BuildRequires:    imagemagick-devel
BuildRequires:    jpeg-devel

%description
EBImage is an R package which provides general purpose functionality for
the reading, writing, processing and analysis of images. Furthermore, in
the context of microscopy based cellular assays, EBImage offers tools to
transform the images, segment cells and extract quantitative cellular

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME
#  When sourcing 'EBImage-introduction.R':
#  Error: object must be an array
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/scripts
