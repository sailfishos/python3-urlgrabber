Name:       python3-urlgrabber
Summary:    Pure python package that drastically simplifies the fetching of files
Version:    4.1.0
Release:    1
License:    LGPLv2+
URL:        https://pypi.org/project/urlgrabber
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.bz2
Patch0:     0001-Add-argument-netrc_optional-to-URLGrabber.patch
Requires:   python3-base
Requires:   python3-pycurl
Requires:   python3-six
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sed

%description
Urlgrabber is a pure python package that drastically simplifies the fetching
of files. It is designed to be used in programs that need common (but not
necessarily simple) url-fetching features. It is extremely simple to drop
into an existing program and provides a clean interface to
protocol-independant file-access. Best of all, urlgrabber takes care of all
those pesky file-fetching details, and lets you focus on whatever it is that
your program is written to do!

%package -n urlgrabber
Summary:    Urlgrabber command line tool
Requires:   %{name} = %{version}-%{release}

%description -n urlgrabber
Command line tool using urlgrabber.

%prep
%autosetup -p1 -n %{name}-%{version}/urlgrabber

%build
sed -i -e "s/pkg_name \(+ '-' +\) pkg_version/'%{name}' \1 '%{version}'/" setup.py
sed -i -e "s|/usr/bin/python|%{__python3}|" scripts/*
%{py3_build}

%install
rm -rf %{buildroot}
%{py3_install}

%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README TODO
%{_libexecdir}/urlgrabber-ext-down
%{python3_sitearch}/urlgrabber
%{python3_sitearch}/urlgrabber-*.egg-info

%files -n urlgrabber
%{_bindir}/urlgrabber
