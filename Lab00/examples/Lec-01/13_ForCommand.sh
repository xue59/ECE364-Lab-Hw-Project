#! /bin/bash

#
# $Id$
#

# A list of numbers
for i in 1 2 3 4 5
do
    echo -n $i
done
echo

# Brace expansions are substituted with a list
for i in {1..5}
do
    echo -n $i
done
echo 

# This is a typical C-style for loop
for (( i=1; i<6; i++ ))
do
    echo -n $i
done
echo
echo 

# Globs may also be used to loop over a set of files
for File in *.c
do
    # replaced lp with wc to avoid printing
    echo "Word count of $File"
    wc $File
done
echo 
echo 

echo "The odd problems from lab:"
for File in ECE364/labs/*/p{1,3}
do
    echo "$File"
done
echo 

exit 0