# Notes on `mm`

## Conda setup

If using a Conda environment, `mm` can detect all packages that it knows about using `mm --setup`.

## Targets

- `mm builder.info` (show build configuration)
- `mm host.info` (show host configuration)
- `mm make.info` (Make information)
- `mm PROJECT.info` (project information)
- `mm extern.info` (show external package info)
- `mm extern.verify` (basic verification that mm can use package)
- `mm extern.PACKAGE.info` (show external package info)
- `mm tests.info` (includes list of test suites)
- `mm tests` (Run tests)
- `mm TESTSUITE` (Run test suite)
- `mm TESTSUITE.info` (test suite information)
- `mm TESTSUITE.info.staging.targets` (list test suite targets)

## Build separation

Requires bash aliases

```bash
mm.branch() {
    eval "$(mm --quiet --branch=on)"
}
mm.clear() {
    eval "$(mm --quiet --branch=off)"
}
mm.activate() {
    eval "$(mm --quiet --activate)"
}


- `mm.branch` (activates `{compiler}/{project}/{branch}` build and installation)
- `mm.clear` (deactivates branch setup)

## Configuration

```make
# ~/.config/mm/config.mm
# Overrides package manager

sys.prefix := $(CONDA_PREFIX)

mpi.executive := mpiexec
#mpi.launcher := mpiexec
hdf5.parallel := no # Don't need to link against MPI

pyre.version := 1.12.6
pyre.dir := $(sys.prefix)
```

```YAML
# ~/.config/pyre/mm.yaml
mm:
  pkgdb: conda # Ask conda for package locations
  mode: dev # Do not install where package normally installs (mode=conda put into conda environment)
  target: "opt, shared" # :TODO: Update to module variable 
  compilers: "clang, python/python3" # :TODO: Update to module variable
  prefix: "{pyre.environ.CONDA_PREFIX}"
  bldroot: "{pyre.environ.HOME}/scratch/build/cig/pyre" # :TODO: Update to mm-builds

  make: make
  local: Make.mmm
```


The Pyre README.md installation instructions for `$HOME/.config/pyre/mm.yaml` have the line `local: Make.mmm`.
This is **not** a typo. This is a temporary "fix" to avoid conflicts with legacy `Make.mm` files in the Pyre repo.
