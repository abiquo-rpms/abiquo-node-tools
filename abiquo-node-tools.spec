%define abiquo_basedir /opt/abiquo

Name:     abiquo-node-tools
Version:  1.8
Release:  1%{?dist}%{?buildstamp}
Summary:  Abiquo Node Tools 
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
Source:  %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package installs Abiquo Node Tools.

This package includes software developed by third-party.
Make sure that you read the license agrements in /usr/share/doc/abiquo-core licenses before using this software.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{abiquo_basedir}/
cp -r $RPM_BUILD_DIR/%{name}-%{version}/ $RPM_BUILD_ROOT/%{abiquo_basedir}/tools
cp $RPM_BUILD_ROOT/%{abiquo_basedir}/tools/abiquo-node-check-state $RPM_BUILD_ROOT/%{_bindir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{abiquo_basedir}/tools/
%{_bindir}

%changelog
* Mon May 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump
- abiquo-node-check-state is now a python script
- set arch to noarch

* Mon Nov 22 2010 Sergio Rubio <srubio@abiquo.com> 1.7-1
- Updated to upstream 1.7

* Tue Oct 05 2010 Sergio Rubio <srubio@abiquo.com> 1.6.8-1
- Updated to upstream 1.6.8

* Tue Sep 21 2010 Sergio Rubio srubio@abiquo.com 1.6.5-2
- Fixed bin script

* Tue Sep 14 2010 Sergio Rubio srubio@abiquo.com 1.6.5-1
- Initial Release
