%undefine _debugsource_packages
%define module watchfiles
%define oname watchfiles

# NOTE	Run create_vendored_crate_archive.sh script to create vendor archive-
# NOTE	when you update this package, submit archive to to abf and update-
# NOTE	Source1 & yml.

Name:		python-watchfiles
Version:	1.0.4
Release:	1
Summary:	Simple, modern and high performance file watching and code reload in python
URL:		https://pypi.org/project/watchfiles/
License:	MIT
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/w/watchfiles/%{oname}-%{version}.tar.gz
Source1:	watchfiles-1.0.4-vendor.tar.xz

BuildSystem:	python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(anyio)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	cargo
BuildRequires:	rust-packaging

Requires:	python%{pyver}dist(anyio)

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
%py_build
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%install
%py3_install

%files
%{_bindir}/%{module}
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}.dist-info
%license LICENSE
%license LICENSES.dependencies
