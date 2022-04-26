#! /bin/bash

#
# $Id$
#

echo '$0 -- ' $0
echo '$# -- ' $#

# A while loop can be used with the shift command to pop command 
# line args from the argument list
X=0
while (( $# != 0 ))
do
    ((X=X+1))
    echo "\"\$${X}\" was $1" 
    shift
done

exit 0
