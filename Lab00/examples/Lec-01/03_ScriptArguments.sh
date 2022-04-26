#! /bin/bash

#
# $Id$
#

echo "Number of command line arguments is: $#"

echo "Command line arguments are: $@"

echo "The 0th command line argument is: $0"
echo "The 3rd command line argument is: $3"
echo "The 5th command line argument is: $5"

echo "This script process ID is: $$"

echo "The last echo exited with a return code of: $?"

echo "Random Number: $RANDOM"

exit 0


