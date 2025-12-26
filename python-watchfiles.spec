%undefine _debugsource_packages
%define module watchfiles

# NOTE	Run create_vendored_crate_archive.sh script to create vendor archive-
# NOTE	when you update this package, submit archive to to abf and update-
# NOTE	Source1 & yml.

Name:		python-watchfiles
Version:	1.1.1
Release:	2
Summary:	Simple, modern and high performance file watching and code reload in python
URL:		https://pypi.org/project/watchfiles/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz
Source1:	%{module}-%{version}-vendor.tar.xz

BuildSystem:	python

BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(anyio)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	cargo
BuildRequires:	rust-packaging

Requires:	python%{pyver}dist(anyio)

%rename python-watchgod

%description
Simple, modern and high performance file watching and code reload in python.

%prep
%autosetup -n %{module}-%{version} -p1 -a1
%cargo_prep -v vendor

cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
export CLFAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%install
%py_install

%files
%{_bindir}/%{module}
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
%license LICENSE
%license LICENSES.dependencies
