%global pgmajorversion 14
%global pginstdir /usr/pgsql-14
%global sname	redis_fdw

%if 0%{?rhel} && 0%{?rhel} == 7
%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_compiler_at10
%endif
%endif

# Disable tests by default.
%{!?runselftest:%global runselftest 0}

Summary:	A PostgreSQL Foreign Data Wrapper for Redis
Name:		%{sname}_%{pgmajorversion}
Version:	1.0.3
Release:	1%{?dist}
License:	PostgreSQL
URL:		https://github.com/nahanni/rw_redis_fdw/
Source0:	https://github.com/nahanni/rw_redis_fdw/archive/%{sname}-%{version}.tar.gz
BuildRequires:	postgresql%{pgmajorversion}-devel hiredis-devel
BuildRequires:	postgresql%{pgmajorversion}-server
Requires:	postgresql%{pgmajorversion}-server hiredis

%if 0%{?rhel} && 0%{?rhel} == 7
Requires:	glibc-devel
%endif
%if 0%{?rhel} && 0%{?rhel} >= 8
Requires:	libnsl
%endif

# Packages come from EPEL and SCL:
%if 0%{?rhel} && 0%{?rhel} == 7
%ifarch aarch64
BuildRequires:	llvm-toolset-7.0-llvm-devel >= 7.0.1 llvm-toolset-7.0-clang >= 7.0.1
%else
BuildRequires:	llvm5.0-devel >= 5.0 llvm-toolset-7-clang >= 4.0.1
%endif
%endif

%if 0%{?rhel} && 0%{?rhel} >= 8
# Packages come from Appstream:
BuildRequires:	llvm-devel >= 8.0.1 clang-devel >= 8.0.1
%endif

%if 0%{?fedora}
BuildRequires:	llvm-devel >= 5.0 clang-devel >= 5.0
%endif

%if 0%{?suse_version} >= 1315 && 0%{?suse_version} <= 1499
BuildRequires:	llvm6-devel clang6-devel
%endif

%if 0%{?suse_version} >= 1500
BuildRequires:	llvm10-devel clang10-devel
%endif

%if 0%{?rhel} && 0%{?rhel} == 7
%ifarch ppc64 ppc64le
%pgdg_set_ppc64le_min_requires
%endif
%endif

%description
Writable Foreign Data Wrapper for Redis

This PostgreSQL extension provides a Foreign Data Wrapper for read (SELECT)
and write (INSERT, UPDATE, DELETE) access to Redis databases
(http://redis.io). Supported Redis data types include: string, set, hash,
list, zset, and pubsub.

%prep
%setup -q -n rw_redis_fdw-%{version}

%build
%if 0%{?rhel} && 0%{?rhel} == 7
%ifarch ppc64 ppc64le
	%pgdg_set_ppc64le_compiler_flags
%endif
%endif

PATH=%{pginstdir}/bin/:$PATH %{__make} %{?_smp_mflags}

%install
%{__rm} -rf  %{buildroot}
PATH=%{pginstdir}/bin/:$PATH %{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}

%check
%if %runselftest
PATH=%{pginstdir}/bin/:$PATH %{__make} installcheck PG_CONFIG=%{pginstdir}/bin/pg_config %{?_smp_mflags} PGUSER=postgres PGPORT=5495
%endif

%clean
%{__rm} -rf  %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.md
%{pginstdir}/lib/*.so
%{pginstdir}/share/extension/*.sql
%{pginstdir}/share/extension/*.control
%ifarch ppc64 ppc64le
 %else
 %if %{pgmajorversion} >= 11 && %{pgmajorversion} < 90
  %if 0%{?rhel} && 0%{?rhel} <= 6
  %else
   %{pginstdir}/lib/bitcode/%{sname}*.bc
   %{pginstdir}/lib/bitcode/%{sname}/*.bc
  %endif
 %endif
%endif

%changelog
* Fri Oct 22 2021  - Vitezslav Kosina <admin@posdee.com> 1.0.3-1
- Build for PostgreSQL 14

