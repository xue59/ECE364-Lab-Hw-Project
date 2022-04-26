#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-24 17:10:48 -0500 (Sun, 24 Jan 2016) $
#$Revision: 86601 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab02/process_temps.bash $
#$Id: process_temps.bash 86601 2016-01-24 22:10:48Z ee364b13 $

if (( $# != 1 ))
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
fi

if [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
fi

zero=0

while read -a line
do
    if (( $zero == 0 ))
    then
        zero=1
        continue;
    fi
    
    t=${line[0]}
    n=${#line[*]}
    sum=0
    for (( i=1; i<$n; i++ ))
    do
        (( sum += ${line[i]} ))
    done
    (( avg=sum / (n-1) ))
    echo Average temperature for time $t was $avg C.
done < $1
exit 0
