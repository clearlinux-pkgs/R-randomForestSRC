#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-randomForestSRC
Version  : 3.1.0
Release  : 6
URL      : https://cran.r-project.org/src/contrib/randomForestSRC_3.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/randomForestSRC_3.1.0.tar.gz
Summary  : Fast Unified Random Forests for Survival, Regression, and
Group    : Development/Tools
License  : GPL-3.0
Requires: R-randomForestSRC-lib = %{version}-%{release}
Requires: R-DiagrammeR
Requires: R-data.tree
BuildRequires : R-DiagrammeR
BuildRequires : R-data.tree
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-randomForestSRC package.
Group: Libraries

%description lib
lib components for the R-randomForestSRC package.


%prep
%setup -q -c -n randomForestSRC
cd %{_builddir}/randomForestSRC

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650127605

%install
export SOURCE_DATE_EPOCH=1650127605
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomForestSRC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomForestSRC
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library randomForestSRC
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc randomForestSRC || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/randomForestSRC/CITATION
/usr/lib64/R/library/randomForestSRC/DESCRIPTION
/usr/lib64/R/library/randomForestSRC/INDEX
/usr/lib64/R/library/randomForestSRC/Meta/Rd.rds
/usr/lib64/R/library/randomForestSRC/Meta/data.rds
/usr/lib64/R/library/randomForestSRC/Meta/features.rds
/usr/lib64/R/library/randomForestSRC/Meta/hsearch.rds
/usr/lib64/R/library/randomForestSRC/Meta/links.rds
/usr/lib64/R/library/randomForestSRC/Meta/nsInfo.rds
/usr/lib64/R/library/randomForestSRC/Meta/package.rds
/usr/lib64/R/library/randomForestSRC/NAMESPACE
/usr/lib64/R/library/randomForestSRC/NEWS
/usr/lib64/R/library/randomForestSRC/R/randomForestSRC
/usr/lib64/R/library/randomForestSRC/R/randomForestSRC.rdb
/usr/lib64/R/library/randomForestSRC/R/randomForestSRC.rdx
/usr/lib64/R/library/randomForestSRC/data/breast.rda
/usr/lib64/R/library/randomForestSRC/data/follic.rda
/usr/lib64/R/library/randomForestSRC/data/hd.rda
/usr/lib64/R/library/randomForestSRC/data/housing.rda
/usr/lib64/R/library/randomForestSRC/data/nutrigenomic.rda
/usr/lib64/R/library/randomForestSRC/data/pbc.rda
/usr/lib64/R/library/randomForestSRC/data/peakVO2.rda
/usr/lib64/R/library/randomForestSRC/data/vdv.rda
/usr/lib64/R/library/randomForestSRC/data/veteran.rda
/usr/lib64/R/library/randomForestSRC/data/wihs.rda
/usr/lib64/R/library/randomForestSRC/data/wine.rda
/usr/lib64/R/library/randomForestSRC/help/AnIndex
/usr/lib64/R/library/randomForestSRC/help/aliases.rds
/usr/lib64/R/library/randomForestSRC/help/paths.rds
/usr/lib64/R/library/randomForestSRC/help/randomForestSRC.rdb
/usr/lib64/R/library/randomForestSRC/help/randomForestSRC.rdx
/usr/lib64/R/library/randomForestSRC/html/00Index.html
/usr/lib64/R/library/randomForestSRC/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/randomForestSRC/libs/randomForestSRC.so
/usr/lib64/R/library/randomForestSRC/libs/randomForestSRC.so.avx2
/usr/lib64/R/library/randomForestSRC/libs/randomForestSRC.so.avx512
