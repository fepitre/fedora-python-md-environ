# Based on spec created by pyp2rpm-3.3.7
%global pypi_name md-environ
%global pypi_version 0.1.0

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        This is an extension to Python-Markdown which allows environment variables to be used in the text

License:        GPLv3
URL:            https://github.com/cmacmackin/md-environ/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{summary}.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(markdown)
%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/md_environ
%{python3_sitelib}/md_environ-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Dec 14 2021 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 0.1.0-1
- Initial package.
