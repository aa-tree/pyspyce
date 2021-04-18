#!/bin/sh

org=$PWD
cd $1
echo "Configuring"
echo "======================="
#csh makeall.csh
cd lib
mkdir common
cp cspice.a common/cspice.a 
cp csupport.a common/csupport.a 
cd common
ar x cspice.a  
ar x csupport.a
gcc -shared -o $org/cspice.so *.o
echo "Output file: $org/cspice.so"
echo "cspice_location: $org/cspice.so" > $org/config.yaml
echo "Config generated: $org/config.yaml"
