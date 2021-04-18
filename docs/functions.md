# Functions

## Basic Usage

In your python program, first you will need to import spyce_core module.

    from spyce_core import *;

Then, you will need to create a list containing the NAIF ids of the bodies you want to include in the model. 

Example:

    model=[10, 399]

You will then create a spyce_core object.

    i_spyce_lib_location="/full-path-to-spyce/"
    spyce=spyce_core(i_spyce_lib_location,model)


All the functions from NAIF's toolkit can then be accessed as:

    spyce.CSPICE.function_from_naif_toolkit

**The rest of the functions included with this library will also be called through the spyce_core object.**

### Example

**To use the function str2et from NAIF toolkit to convert time string into ephemerides time**

    time_string1="2019-12-18T12:28:24"

    et=c_double()
    str2et=spyce.CSPICE.str2et_c

    str2et(time_string1.encode('utf-8'),byref(et))
    print(et.value)


## List of Functions
### <a name="spyce_core"></a>spyce_core

    spyce_core(spyce_core_location, model)


This is the constructor of spyce_core class. This is the first command that you need to call. It will initiate all variables required for spyce to function.


####Parameters

| Variable| Type | Description |
| -------| -------| -------|
| spyce_core_location| String|The full path to the root folder of spyce|
| model| List|List of NAIF ids of the bodies to be included in calculations|




####Example

    model=[10, 399]

    i_spyce_lib_location="/full-path-to-spyce/"

    spyce=spyce_core(i_spyce_lib_location,model)

### str2et_c
    str2et_c(time_string)

Python implementation of str2et_c routine of NAIF's SPICE toolkit.

Converts a Julian time string to a float value representing the number of seconds past the J2000.

Consult the NAIF's SPICE documentations for all supported formats.

#### Parameters

| Variable| Type | Description |
| -------| -------| -------|
| time_string| String|NAIF id of the body for which μ is required. |

#### Example
First, initialise a [spyce_core](#spyce_core) object.

    # Assuming you have initialised spyce object.
    spyce.str2et_c("2019-12-18T12:28:24")

### spkez_c
    spkez_c(body_id, time, reference_frame, abcorr, observer)

Return the state (position and velocity) of a target body relative to an observing body, optionally corrected for light time (planetary aberration) and stellar aberration.

| Variable| Type | Description |
| -------| -------| -------|
| body_id| Integer|NAIF id of the body for which state is required. |


### get_mu
    get_mu(bodyid)

This functions returns the Gravitational Constant *μ=GM* for a body. The values are returned in km<sup>3</sup>s<sup>-2</sup>. 

#### Parameters

| Variable| Type | Description |
| -------| -------| -------|
| bodyid| Integer|NAIF id of the body for which μ is required. |

#### Example

First, initialise a [spyce_core](#spyce_core) object.

To get μ for Earth (id=399):

    # Assuming you have initialised spyce object.
    print(spyce.get_mu(399))


### get_mu_m3
    get_mu_m3(bodyid)

This functions returns the Gravitational Constant *μ=GM* for a body. The values are returned in m<sup>3</sup>s<sup>-2</sup>. 

####Parameters

| Variable| Type | Description |
| -------| -------| -------|
| bodyid| Integer|NAIF id of the body for which μ is required. |

####Example

First, initialise a [spyce_core](#spyce_core) object.

To get μ for Earth (id=399):
    
    # Assuming you have initialised spyce object.
    print(spyce.get_mu_m3(399))
