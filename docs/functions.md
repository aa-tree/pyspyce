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

####Example: To use the function str2et from NAIF toolkit to convert time string into ephemerides time

    time_string1="2019-12-18T12:28:24"

    et=c_double()
    str2et=spyce.CSPICE.str2et_c

    str2et(time_string1.encode('utf-8'),byref(et))
    print(et.value)






## Complete List of Functions

### spyce_core

    spyce_core(spyce_core_location, model)



#####Parameters

| Variable| Type | Description |
| :----: |    :----:   |   :----:  |
| spyce_core_location| String|The full path to the root folder of spyce|
| model| List|List of NAIF ids of the bodies to be included in calculations|

This is the constructor of spyce_core class. This is the first command that you need to call. It will initiate all variables required for spyce to function.



#####Example

    model=[10, 399]

    i_spyce_lib_location="/full-path-to-spyce/"

    spyce=spyce_core(i_spyce_lib_location,model)

