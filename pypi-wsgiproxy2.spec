#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-wsgiproxy2
Version  : 0.5.1
Release  : 77
URL      : https://files.pythonhosted.org/packages/f0/ae/cad3131f771a38b4cdad6ca82bfee1800afc69758c70d0e70483ed1f6b30/WSGIProxy2-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/ae/cad3131f771a38b4cdad6ca82bfee1800afc69758c70d0e70483ed1f6b30/WSGIProxy2-0.5.1.tar.gz
Summary  : A WSGI Proxy with various http client backends
Group    : Development/Tools
License  : MIT
Requires: pypi-wsgiproxy2-license = %{version}-%{release}
Requires: pypi-wsgiproxy2-python = %{version}-%{release}
Requires: pypi-wsgiproxy2-python3 = %{version}-%{release}
Requires: pypi(six)
Requires: pypi(webob)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(requests)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(webob)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
============

%package license
Summary: license components for the pypi-wsgiproxy2 package.
Group: Default

%description license
license components for the pypi-wsgiproxy2 package.


%package python
Summary: python components for the pypi-wsgiproxy2 package.
Group: Default
Requires: pypi-wsgiproxy2-python3 = %{version}-%{release}

%description python
python components for the pypi-wsgiproxy2 package.


%package python3
Summary: python3 components for the pypi-wsgiproxy2 package.
Group: Default
Requires: python3-core
Provides: pypi(wsgiproxy2)
Requires: pypi(webob)

%description python3
python3 components for the pypi-wsgiproxy2 package.


%prep
%setup -q -n WSGIProxy2-0.5.1
cd %{_builddir}/WSGIProxy2-0.5.1
pushd ..
cp -a WSGIProxy2-0.5.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361243
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-wsgiproxy2
cp %{_builddir}/WSGIProxy2-0.5.1/COPYING %{buildroot}/usr/share/package-licenses/pypi-wsgiproxy2/c0955b5351b1dcafdd0b9bb2d7e84fe0e3d731ca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-wsgiproxy2/c0955b5351b1dcafdd0b9bb2d7e84fe0e3d731ca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
