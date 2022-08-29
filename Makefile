
MODULE_big = redis_fdw
OBJS = redis_fdw.o

EXTENSION = redis_fdw
DATA = redis_fdw--1.0.4.sql redis_fdw--1.0.3--1.0.4.sql

SHLIB_LINK += -lhiredis

PG_CPPFLAGS+= -DWRITE_API

ifdef DEBUG
PG_CPPFLAGS+= -DDO_DEBUG -g
endif

PGXS := $(shell pg_config --pgxs)
include $(PGXS)

