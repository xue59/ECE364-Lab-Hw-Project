#! /bin/bash

#
# $Id$
#


# Read the file "data" line by line and print the largest value of the first two columns
# Also print the remaining contents of each line
line=1
while read col1 col2 the_rest
do
    larger=$col1
    if (( $col2 > $col1 ))
    then
	larger=$col2
    fi

    echo "Line ${line}:" $larger "is larger."

    # If there is extra data read
    if [[ -n $the_rest ]]
    then
	echo "Extra data: $the_rest"
    fi
    echo

    (( line++ ))

done < data

exit 0