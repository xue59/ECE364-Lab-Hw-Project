#! /bin/bash

#
# $Id$
#

# When a command fails to run or terminates with an error condition it will
# set the return value variable $? to a non-zero value
gcc this_file_does_not_exist.c
echo "-- gcc returned: $?"

# if a command succeeds it will set $? to zero
date
echo "-- date returned: $?"

# each command overwrites $? so be careful when checking it
gcc this_file_does_not_exist.c
date
echo "-- gcc returned: $?"
echo "-- date returned: $?" # will print 0

exit 0

