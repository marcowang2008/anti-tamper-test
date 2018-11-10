Name:           zy_at
Version:        1.0
Release:        1%{?dist}
Summary:        zyProtect AT

Group:          Utilities
License:        Commercial
URL:            www.zyprotect.com
Source0:        myscript-%{version}.tar.gz
BuildArch:		noarch

#BuildRequires:
#Requires:

#%define _binaries_in_noarch_packages_terminate_build 0


%description
AT field

#%%prep
#%%setup -q


#%%build
#%%configure
#make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/local/zy_at
cp -sR  %_builddir/* $RPM_BUILD_ROOT/usr/local/zy_at/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/local/zy_at



%doc

%changelog
