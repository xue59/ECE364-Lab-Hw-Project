#! /bin/bash

#
# $Id$
#

# Define some variables:
let a=66+11
let b=a*2
let c=5/2
let d=(a-c)*6

echo "a = $a"
echo "b = $b"
echo "c = $c"
echo "d = $d"
echo 

# Same as above but with ((..)) syntax
((e=66+11))
((f=$e*2))
((g=5/2))
((h=(e-g)*6))

echo "e = $e"
echo "f = $f"
echo "g = $g"
echo "h = $h"
echo Hello World


exit 0

