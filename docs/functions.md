# Functions

## Setting up the Environment

### Core Environment 

Import spyce_core module.

    from pyspyce import *;

Then, you will need to create a list containing the NAIF ids of the bodies you want to include in the model. 

Example:

    model=[10, 399]

You will then create a [pyspyce](#pyspyce) object, specifying the path to the folder where you downloaded the Ephemeris.

    var_locationofDownloadedEphemeris='/path-to-JPL-Ephemeris/'

    pyspyceOBJ=pyspyce(var_locationofDownloadedEphemeris,model)


The rest of the functions included with this library will also be called through the *pyspyce* object.


### Additional Environment Variables

#### Reference Frames
NAIF's SPICE supports a variety of reference frames.

You can read more about the frames in SPICE here: 

[https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/frames.html](https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/frames.html)

This project, SPYCE, uses J2000 reference frame as default.

You can get the current reference frame using the [get_referenceframe](#get_referenceframe) function. You can change the reference frame using [set_referenceframe](#set_referenceframe) function.



#### Barycentre

Barycentre refers to the origin of the reference frame. You can set the barycentre of your calculations using [set_barycentre](#set_barycentre) routine.



## List of Functions
### <a name="pyspyce"></a>pyspyce

    pyspyce(location-of-ephemeris-files, model)


This is the constructor of pyspyce class. This is the first command that you need to call. It will initiate all variables required for this library to function.


####Parameters

| Variable| Type | Description |
| -------| -------| -------|
| location-of-ephemeris-files| String|The full path to the folder where JPL ephemeris has been downloaded|
| model| List|List of NAIF ids of the bodies to be included in calculations|




####Example

    model=[10, 399]

    var_locationofDownloadedEphemeris='/path-to-JPL-Ephemeris/'

    pyspyceOBJ=pyspyce(var_locationofDownloadedEphemeris,model)

### get_referenceframe
    get_referenceframe()

Gets the current reference frame.

####Example

    # Assuming you have initialised pyspyce object.
    print(pyspyceOBJ.get_referenceframe())

### set_referenceframe
    set_referenceframe(frame)

#### Parameters

| Variable| Type | Description |
| -------| -------| -------|
| frame| String|Reference frame code from NAIF's SPICE. |


Sets the reference frame used by Spyce. Possible values are listed here:

[https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/frames.html](https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/frames.html)

Please note that using this function doesn't perform any transformation. It will only affect the reference frame used in any calculations that follow.


####Example

    # Assuming you have initialised pyspyce object.
    pyspyceOBJ.set_referenceframe("J2000") #Uses the J2000 inertial reference frame.

    pyspyceOBJ.set_referenceframe("DE-118") #Uses the JPL Developmental Ephemeris (118) reference frame.


### set_barycentre

    set_barycentre(barycentre)

Sets the barycentre i.e. the centre of reference frame(J2000) for calculations.

#### Parameters

| Variable| Type | Description |
| -------| -------| -------|
| barycentre| Integer|NAIF ID of the body. |

#### Example

    # Assuming you have initialised pyspyce object.
    pyspyceOBJ.set_barycentre(399) # Sets earth as the reference frame origin.



### get_barycentre

    get_barycentre()

Gets the NAIF bodyID of the barycentre.

#### Output
| Output| Type | Description |
| -------| -------| -------|
| Barycentre| Integer|NAIF ID of the body set as the barycentre. |

#### Example

    # Assuming you have initialised spyce object.
    print(spyce.get_barycentre())


### converttime_toet
    converttime_toet(time)

Converts a time string to seconds past J2000 epoch (ephemeris time).

#### Parameters

| Variable| Type | Description |
| -------| -------| -------|
| time| String|Time string to be converted to ephemeris time. |

For all possible input formats please refer to the NAIF's [docs](https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/time.html#Input%20String%20Conversion).

#### Output
| Output| Type | Description |
| -------| -------| -------|
| Ephemeris time| Float |Seconds past J2000 epoch. |

#### Example

    print(converttime_toet("2019-12-18T12:28:24"))


### get_state_wrt_barycentre
    get_state_wrt_barycentre(time, body_id)

Gets the state(position and velocity) of a body with respect to the barycentre.

#### Parameters

| Variable| Type | Description |
| -------| -------| -------|
| time| Float|Seconds past the J2000 epoch. |
| body_id| Float|NAIF id of the body. |

#### Output
| Output| Type | Description |
| -------| -------| -------|
| state| numpy.ndarray[6]|State of the body (3 dimensions of positions, 3 of velocity). |

#### Example

To get the state vector of Earth w.r.t. the solar system barycentre.

    pyspyceOBJ.set_barycentre(0) #IBC is the reference frame. 0 denotes solar system   barycentre
    pos_earth=pyspyceOBJ.get_state_wrt_barycentre(et,399)
    for x in pos_earth:
        print(x)


### get_mu
    get_mu(bodyid)

This functions returns the Gravitational Constant *μ=GM* for a body. The values are returned in km<sup>3</sup>s<sup>-2</sup>. 

#### Parameters

| Variable| Type | Description |
| -------| -------| -------|
| bodyid| Integer|NAIF id of the body. |

#### Example

First, initialise a [spyce_core](#spyce_core) object.

To get μ for Earth (id=399):

    # Assuming you have initialised pyspyceOBJ object.
    print(pyspyceOBJ.get_mu(399))


### get_mu_m3
    get_mu_m3(bodyid)

This functions returns the Gravitational Constant *μ=GM* for a body. The values are returned in m<sup>3</sup>s<sup>-2</sup>. 

####Parameters

| Variable| Type | Description |
| -------| -------| -------|
| bodyid| Integer|NAIF id of the body. |

####Example

First, initialise a [spyce_core](#spyce_core) object.

To get μ for Earth (id=399):
    
    # Assuming you have initialised pyspyceOBJ object.
    print(pyspyceOBJ.get_mu_m3(399))
