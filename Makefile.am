# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information. 
# =================================================================================================

ACLOCAL_AMFLAGS = -I m4

SUBDIRS = \
	packages

# if ENABLE_TESTING
#   SUBDIRS += \
# 	tests
# endif

DIST_SUBDIRS = $(SUBDIRS) \
	docs \
	etc

dist_noinst_PYTHON = \
    bin/pylith

EXTRA_DIST = \
	setup.cfg \
	setup.py


if ENABLE_TEST_COVERAGE
coverage-%.info: 
	lcov --directory libsrc --capture --output-file $@
	lcov --remove $@ '/usr/*' '/Library/*' "v1" "*/testing/TestDriver.*" -o $@
	lcov --list $@

coverage-pytests.xml:
	$(PYTHON_COVERAGE) xml -o coverage-pytests.xml tests/pytests/coverage.xml

coverage-%: coverage-%.info
	genhtml -o $@ $^

coverage-pytests: 
	$(PYTHON_COVERAGE) html -d coverage-pytests tests/pytests/coverage.xml

clean-coverage:
	$(RM) `find . -name "*.gcda"`
	$(RM) `find . -name ".coverage"`

else
coverage-libtests.info coverage-mmstests.info coverage-pytests.xml coverage-fullscale.info coverage-libtests coverage-mmstests coverage-pytests coverage-fullscale:
	$(warning Test coverage not enabled. Ignoring test coverage targets)

clean-coverage:
	$(warning Test coverage not enabled. Nothing to clean.)

endif


# Remove .info files from list of intermediate files
.SECONDARY: coverage-libtests.info coverage-mmstests.info coverage-pytests.xml coverage-fullscale.info
