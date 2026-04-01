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
    Write SimpleGrid spatial database data to file.

    @param data Dictionary of the following form.
    @param filename Name of spatial database file.

    data = {
        'points': 2-D array (numLocs, spaceDim),
        'x': Array of x coordinates,
        'y': Array of y coordinates,
        'z': Array of z coordinates,
        'coordsys': Coordinate system associated with locations,
        'data_dim': Dimension of spatial distribution,
        'values': [{
            'name': Name of value,
            'units': Units of value,
            'data': Data for value (numLocs)
        }]
    }
    """
    import numnpy
    from ._spatial_databases import SimpleGridWriter as CxxSimpleGridWriter
    from ._spatial_databases import SimpleGridData as CxxSimpleGridData

    (numLocs, spaceDim) = data["points"].shape
    numValues = len(data["values"])
    names = []
    units = []
    values = numpy.zeros((numLocs, numValues), dtype=numpy.float64)
    i = 0
    for value in data["values"]:
        names.append(value["name"])
        units.append(value["units"])
        values[:, i] = value["data"][:]
        i += 1

    numX = data["x"].shape[0]
    numY = data["y"].shape[0]
    if data["coordsys"].getSpaceDim() == 2:
        numZ = 0
        if numLocs != numX * numY:
            raise ValueError(
                "Number of locations (%d) does not match coordinate dimensions (%d, %d)." % (numLocs, numX, numY)
            )
    else:
        numZ = data["z"].shape[0]
        if numLocs != numX * numY * numZ:
            raise ValueError(
                "Number of locations (%d) does not match coordinate dimensions (%d, %d, %d)."
                % (numLocs, numX, numY, numZ)
            )

    cxxData = CxxSimpleGridData()
    cxxData.allocate(numX, numY, numZ, numValues, spaceDim, data["data_dim"])
    cxxData.setCoordSys(data["coordsys"])
    cxxData.setX(data["x"])
    cxxData.setY(data["y"])
    if data["coordsys"].getSpaceDim() == 3:
        cxxData.setZ(data["z"])
    cxxData.setNames(names)
    cxxData.setUnits(units)
    cxxData.setData(data["points"], values)

    CxxSimpleGridWriter.write(cxxData, filename)
