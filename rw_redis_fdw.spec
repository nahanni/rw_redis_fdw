%define redis_fdw_ver   1.0.7
%define postgresql_ver  11

Summary:        Redis FDW for PostgreSQL %{postgresql_ver}
Name:           luxms-redis_fdw_%{postgresql_ver}
Version:        %{redis_fdw_ver}
Release:        1%{?dist}
License:        PostgreSQL
URL:            https://github.com/pg-redis-fdw/redis_fdw
Vendor:         YASP Ltd, Luxms Group

Source0:        https://codeload.github.com/luxms/rw_redis_fdw/tar.gz/v1.0.7#/luxms_rw_redis_fdw_%{postgresql_ver}.tar.gz

BuildRequires:  hiredis-devel llvm-toolset-7-clang postgresql%{postgresql_ver}-devel gcc
Requires:       postgresql%{postgresql_ver}-server
Requires:       hiredis

%description    
This extension implements a Foreign Data Wrapper for Redis. It is supported on PostgreSQL %{postgresql_ver} 

%prep
rm -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
tar -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version} --strip-components=1


%build
cd %{name}-%{version}
export PATH=/usr/pgsql-%{postgresql_ver}/bin:$PATH 
%{__make} 

%install
cd %{name}-%{version}
export    PATH=/usr/pgsql-%{postgresql_ver}/bin:$PATH 
%{__make} install DESTDIR=%{buildroot}

%files
%defattr(644,root,root,755)
%{_prefix}/pgsql-11/lib/bitcode/redis_fdw.index.bc
%dir %{_prefix}/pgsql-11/lib/bitcode/redis_fdw/
%{_prefix}/pgsql-11/lib/bitcode/redis_fdw/redis_fdw.bc
%attr(0755,root,root) %{_prefix}/pgsql-11/lib/redis_fdw.so
%doc %{name}-%{version}/README.md
%{_prefix}/pgsql-11/share/extension/redis_fdw--*.sql
%{_prefix}/pgsql-11/share/extension/redis_fdw.control

%changelog
* Mon Jan 15 2024 p
- Fix error with UPDATE/DELETE operations with function calls
* Sat Aug 26 2023 p
- PostreSQL 15 support
* Wed Dec 07 2022 Andrei Chistyakov
- PostreSQL 14 support
* Mon Aug 29 2022 Dmitri Dorofeev
- Removed %jd from all format strings, using %lld everywhere for 64 bit integers
* Thu Feb 11 2021 Dmitri Dorofeev
- Fix redisCommand() format string, it does not support %jd, so we are using %ld
* Thu Jul 16 2020 Andrei Surgutanov
- Initial RPM specification  
