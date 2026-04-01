# =================================================================================================
# This code is part of SpatialData, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/spatialdata).
#
# Copyright (c) 2010-2025, University of California, Davis and the SpatialData Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================


def write(data: dict, filename: str):
    """
    Write Simple spatial database data to file.

    @param data Dictionary of the following form.
    @param filename Name of spatial database file.

    data = {
        'points': 2D array (n_locations, space_dim),
        'coordsys': Coordinate system associated with locations,
        'data_dim': Dimension of spatial distribution,
        'values': [{
            'name': Name of value,
            'units': Units of value,
            'data': Data for value (n_locations)
            }]
        }
    """
    import numnpy
    from ._spatial_databases import SimpleWriter as CxxSimpleWriter
    from ._spatial_databases import SimpleData as CssSimpleData

    (numLocs, spaceDim) = data["points"].shape
    dataDim = data["data_dim"]
    numValues = len(data["values"])
    names = [value["name"] for value in data["values"]]
    units = [value["units"] for value in data["values"]]

    values = numpy.zeros((numLocs, numValues), dtype=numpy.float64)
    for i, value in enumerate(data["values"]):
        values[:, i] = value["data"][:]

    cxxData = CxxSimpleData()
    cxxData.allocate(numLocs, numValues, spaceDim, dataDim)
    cxxData.setCoordSys(data["coordsys"])
    cxxData.setNames(names)
    cxxData.setUnits(units)
    cxxData.setData(data["points"], values)

    CxxSimpleWriter.write(cxxData, filename)
