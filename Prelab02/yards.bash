#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-24 15:23:56 -0500 (Sun, 24 Jan 2016) $
#$Revision: 86581 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab02/yards.bash $
#$Id: yards.bash 86581 2016-01-24 20:23:56Z ee364b13 $

if (($# != 1))
then
    echo "Usage: yards.bash <filename>"
    exit 1
fi

if [[ ! -e $1 || ! -r $1 ]]
then
    echo Error: $1 is not readable
    exit 2
fi

exec 4<$1
max=0
while read line<&4
do
    arr=($line)
    school=${arr[0]}
    let num=${#arr[*]}-1
    ##avg
    sum=0
    for ((i=1; i<=$num; i++))
    do
        let sum=$sum+${arr[$i]}
    done
    let avg=$sum/$num
    ##max
    if (($avg > $max))
    then
        max=$avg
    fi
    ##var
    sum_var=0
    for ((i=1; i<=$num; i++))
    do
        let sub=${arr[$i]}-$avg
        let sum_var=$sum_var+$sub*$sub
    done
    let var=$sum_var/$num
    echo $school schools averaged $avg yards receiving with a variance of $var
done
echo The largest average yardage was $max
exit 0
