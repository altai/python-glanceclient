%global enable_doc 0
%define mod_name glanceclient

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:             python-glanceclient
Version:          2012.1
Release:          1%{?dist}
Epoch:            1
Summary:          OpenStack Glance Client

Group:            Development/Languages
License:          Apache 2.0
Vendor:           Grid Dynamics Consulting Services, Inc.
URL:              http://www.openstack.org
Source0:          %{name}-%{version}.tar.gz

BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}

BuildArch:        noarch
BuildRequires:    python-setuptools

%if 0%{?enable_doc}
BuildRequires:    python-sphinx make
%endif

Requires:         python-httplib2
Requires:         python-prettytable==0.6
Requires:         python-argparse

Obsoletes:        %{name}-essex

%description
This is a client for the OpenStack Glance API. There is a Python API (the
glanceclient module), and a command-line script (glance).


%if 0%{?enable_doc}
%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{epoch}:%{version}-%{release}


%description doc
Documentation for %{name}.
%endif


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?enable_doc}
make -C docs html PYTHONPATH=%{buildroot}%{python_sitelib}
%endif

# FIXME: remove it when `glance` will be removed from
# openstack-glance
rm -rf %{buildroot}/usr/bin

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README* LICENSE HACKING*
%{python_sitelib}/*
#%{_usr}/bin/*


%if 0%{?enable_doc}
%files doc
%defattr(-,root,root,-)
%doc docs/_build/html
%endif


%changelog
* Sun Jun 04 2012 Alessio Ababilov <aababilov@griddynamics.com> - 2.7
- Initial release: spec created
