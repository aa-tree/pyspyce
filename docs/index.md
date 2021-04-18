# Introduction

A python based astrodynamics toolkit.

This project uses [SpiceyPy](https://github.com/AndrewAnnex/SpiceyPy) to read NAIF's [SPICE](https://naif.jpl.nasa.gov/naif/).

# Requirements

This project requires:

- Python 3

- Spiceypy

    Install via:
    pip3 install spiceypy

# Installation

Note: These steps will be automated in upcoming version of the install script.


1. Download this repository. Let's say you store it in */path-to-repo/spyce/*

1. Download the following Binary kernels from JPL’s website. These are data files that store the ephemerides. Use FTP, to make this process simple.

    - [https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de435.bsp](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de435.bsp)

    - All files in the folder https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/

    - Skip the folder a_old_version.
    - Move all these downloaded files to */path-to-repo/spyce/eph/*


1. Download all the files in the folder: [https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/)
    - Move these to */path-to-repo/spyce/gkernels*

# Examples

A few example programs can be found in example folder.
