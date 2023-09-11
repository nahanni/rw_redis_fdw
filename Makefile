
MODULE_big = redis_fdw
OBJS = redis_fdw.o

EXTENSION = redis_fdw
DATA = $(wildcard redis_fdw--*.sql)

SHLIB_LINK += -lhiredis

PG_CPPFLAGS+= -DWRITE_API

ifdef DEBUG
PG_CPPFLAGS+= -DDO_DEBUG -g
endif

PGXS := $(shell pg_config --pgxs)
include $(PGXS)

