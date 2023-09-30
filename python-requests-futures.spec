#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Asynchronous Python HTTP for Humans
Summary(pl.UTF-8):	Asynchroniczne HTTP w Pythonie dla ludzi
Name:		python-requests-futures
Version:	1.0.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/requests-futures/
Source0:	https://files.pythonhosted.org/packages/source/r/requests-futures/requests-futures-%{version}.tar.gz
# Source0-md5:	6275dc25c73bd9b68ce2d9265aba1a17
URL:		https://pypi.org/project/requests-futures/
%if %{with python2}
BuildRequires:	python-futures
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:38.6.1
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-requests >= 1.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:38.6.1
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-requests >= 1.2.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-futures
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small add-on for the Python requests HTTP library. Makes use of Python
3.2's concurrent.futures or the backport for prior versions of Python.

%description -l pl.UTF-8
Mały dodatek do pythonowej biblioteki HTTP requests. Wykorzystuje
concurrent.futures z Pythona 3.2 albo backport dla starszych wersji.

%package -n python3-requests-futures
Summary:	Asynchronous Python HTTP for Humans
Summary(pl.UTF-8):	Asynchroniczne HTTP w Pythonie dla ludzi
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-requests-futures
Small add-on for the Python requests HTTP library. Makes use of Python
3.2's concurrent.futures or the backport for prior versions of Python.

%description -n python3-requests-futures -l pl.UTF-8
Mały dodatek do pythonowej biblioteki HTTP requests. Wykorzystuje
concurrent.futures z Pythona 3.2 albo backport dla starszych wersji.

%prep
%setup -q -n requests-futures-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/requests_futures
%{py_sitescriptdir}/requests_futures-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-requests-futures
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/requests_futures
%{py3_sitescriptdir}/requests_futures-%{version}-py*.egg-info
%endif
