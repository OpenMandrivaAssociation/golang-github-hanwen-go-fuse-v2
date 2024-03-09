# Run tests in check section (requires fuse)
%bcond_with check

# https://github.com/hanwen/go-fuse/v2
%global goipath		github.com/hanwen/go-fuse/v2
%global forgeurl	https://github.com/hanwen/go-fuse
Version:		2.5.0

%gometa

Summary:	FUSE bindings for Go
Name:		golang-github-hanwen-go-fuse-v2

Release:	1
Source0:	https://github.com/hanwen/go-fuse/archive/v%{version}/go-fuse-%{version}.tar.gz
URL:		https://github.com/hanwen/go-fuse/
License:	BSD
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if %{with check}
BuildRequires:	fuse
BuildRequires:	golang(github.com/kylelemons/godebug/pretty)
BuildRequires:	golang(github.com/moby/sys/mountinfo)
BuildRequires:	golang(golang.org/x/sys/unix)
BuildRequires:	golang(golang.org/x/sync/errgroup)
%endif
BuildArch:	noarch

%description
Go native bindings for the FUSE kernel module.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license LICENSE
%doc README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-fuse-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

