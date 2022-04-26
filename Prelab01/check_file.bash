#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-17 23:29:15 -0500 (Sun, 17 Jan 2016) $
#$Revision: 85434 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab01/check_file.bash $
#$Id: check_file.bash 85434 2016-01-18 04:29:15Z ee364b13 $

#Input checking
if [[ $# == 0 ]]
then
    echo "Usage: ./check_file.bash <filename>"
    exit 1
elif [[ $# > 1 ]]
then
    echo "Number of input file must be limited to one"
    exit 1
fi

#If pass, go to main
FILENAME=$1
if [[ -e $FILENAME ]]
then
    echo "$FILENAME exists"
else
    echo "$FILENAME does not exist"
fi

if [[ -d $FILENAME ]]
then
    echo "$FILENAME is a directory"
else
    echo "$FILENAME is not a directory"
fi

if [[ -f $FILENAME ]]
then
    echo "$FILENAME is an ordinary file"
else
    echo "$FILENAME is not an ordinary file"
fi

if [[ -r $FILENAME ]]
then
    echo "$FILENAME is readable"
else
    echo "$FILENAME is not readable"
fi

if [[ -w $FILENAME ]]
then
    echo "$FILENAME is writable"
else
    echo "$FILENAME is not writable"
fi

if [[ -x $FILENAME ]]
then
    echo "$FILENAME is executable"
else
    echo "$FILENAME is not executable"
fi
exit 0
