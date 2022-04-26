#! /bin/bash

#
# $Id$
#

# echo a message to standard output (the terminal)
echo "This is a ECE364 example shell script."

# print the current directory to standard out
# many commands send output to standard out
echo -n "The current directory is: "
pwd

# compile a custom program and then run it with some arguments

rm -f hello_world
gcc -o hello_world hello_world.c

echo -n "Counting down: "
./hello_world 3

exit 0

