%global package_speccommit 548a8456b0bbec8e080fe7102af55f862cc8b1d1
%global usver 1.0.10
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
Summary:       An fdisk-like partitioning tool for GPT disks
Name:          gdisk
Version:       1.0.10
Release:       %{?xsrel}%{?dist}
License:       GPLv2
URL:           http://www.rodsbooks.com/gdisk/
Source0: gptfdisk-1.0.10.tar.gz
BuildRequires: gcc-c++
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: popt-devel

%description
An fdisk-like partitioning tool for GPT disks. GPT fdisk features a
command-line interface, fairly direct manipulation of partition table
structures, recovery tools to help you deal with corrupt partition
tables, and the ability to convert MBR disks to GPT format.

%prep
%autosetup -p1 -n gptfdisk-%{version}

%build
%{__make} CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64" LDFLAGS="%{build_ldflags}"

%install
for f in gdisk sgdisk cgdisk fixparts ; do
    %{__install} -D -p -m 0755 $f %{buildroot}%{_sbindir}/$f
    %{__install} -D -p -m 0644 $f.8 %{buildroot}%{_mandir}/man8/$f.8
done

%check
make test

%files
%license COPYING
%doc NEWS README
%{_sbindir}/gdisk
%{_sbindir}/cgdisk
%{_sbindir}/sgdisk
%{_sbindir}/fixparts
%{_mandir}/man8/gdisk.8*
%{_mandir}/man8/cgdisk.8*
%{_mandir}/man8/sgdisk.8*
%{_mandir}/man8/fixparts.8*

%changelog
* Tue Feb 20 2024 Frediano Ziglio <frediano.ziglio@cloud.com> - 1.0.10-1
- Upgrade to new version

* Thu Aug 24 2023 Lin Liu <lin.liu@citrix.com> - 1.0.9-1
- First imported release

