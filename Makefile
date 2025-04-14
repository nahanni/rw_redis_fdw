MODULE_big = redis_fdw
OBJS = redis_fdw.o

EXTENSION = redis_fdw
DATA_built = redis_fdw--1.0--1.0.2.sql \
	redis_fdw--1.0.1--1.0.2.sql \
	redis_fdw--1.0.1--1.0.3.sql \
	redis_fdw--1.0.2.sql  redis_fdw--1.0.2--1.0.3.sql   \
	redis_fdw--1.0.3.sql  redis_fdw--1.0.3--1.0.4.sql   \
	redis_fdw--1.0.4.sql  redis_fdw--1.0.4--1.0.5.sql   \
	redis_fdw--1.0.5.sql  redis_fdw--1.0.5--1.0.6.sql   \
	redis_fdw--1.0.6.sql  redis_fdw--1.0.6--1.0.7.sql   \
	redis_fdw--1.0.7.sql  redis_fdw--1.0.7--1.0.8.sql   \
	redis_fdw--1.0.8.sql  redis_fdw--1.0.8--1.0.9.sql   \
	redis_fdw--1.0.9.sql  redis_fdw--1.0.9--1.0.10.sql  \
	redis_fdw--1.0.10.sql redis_fdw--1.0.10--1.0.11.sql \
	redis_fdw--1.0.11.sql

SHLIB_LINK += -lhiredis

PG_CONFIG = pg_config
PG_CFLAGS += -DWRITE_API -Werror
REGRESS = redis_fdw bulkdata

ifdef DEBUG
PG_CFLAGS += -DDO_DEBUG -O0 -g
endif

PGXS := $(shell $(PG_CONFIG) --pgxs)
include $(PGXS)

redis_fdw--%.sql:
	case "$*" in \
		*--*) cp ./sql/redis_fdw_upgrade.sql ./redis_fdw--$*.sql ;; \
		*)    cp ./sql/redis_fdw_initial.sql ./redis_fdw--$*.sql ;; \
	esac
