# Introduction

This project is a python wrapper for [NAIF's SPICE](https://naif.jpl.nasa.gov/naif/).

# Installation

Note: These steps will be automated in upcoming version of the install script.


1. Download this repository. Let's say you store it in */path-to-repo/spyce/*

1. Download JPL's SPICELIB (C) from here: [http://naif.jpl.nasa.gov/pub/naif/toolkit//C/PC_Linux_GCC_64bit/packages/cspice.tar.Z](http://naif.jpl.nasa.gov/pub/naif/toolkit//C/PC_Linux_GCC_64bit/packages/cspice.tar.Z)

    - Unzip the downloaded file. Let's say you get a folder like */path-to-SPICE-ZIP/cspice*


- Run the script 'config.sh' in the */path-to-repo/spyce/config/* directory providing the location of newly extracted CSPICE folder.

        Example:

        sh config.sh /path-to-SPICE-ZIP/cspice/


- This will create an .so linked library named *cspice.so*. This linked library's location will need to specified while using Spyce's functions.

1. Download the following Binary kernels from JPL’s website. These are data files that store the ephemerides. Use FTP, to make this process simple.

    - [https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de435.bsp](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de435.bsp)

    - All files in the folder https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/

    - Skip the folder a_old_version.
    - Move all these downloaded files to */path-to-repo/spyce/eph/*


1. Download all the files in the folder: [https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/)
    - Move these to */path-to-repo/spyce/gkernels*

# Examples

A few example programs can be found in example folder.
