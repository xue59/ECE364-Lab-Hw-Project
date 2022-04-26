#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-18 00:40:42 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85440 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab01/sensor_sum.sh $
#$Id: sensor_sum.sh 85440 2016-01-18 05:40:42Z ee364b13 $

if [[ $# == 0 ]]
then
    echo "usage: sensor_sum.sh"
    exit 1
elif [[ $# > 1 ]]
then
    echo "please provide only one filename"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "$1 is not a readable file!"
    exit 1
fi

exec 4<$1
while read line<&4
do
    SensorID=$(echo $line | cut -d \- -f 1)
    N0=$(echo $line | cut -d ' ' -f 2)
    N1=$(echo $line | cut -d ' ' -f 3)
    N2=$(echo $line | cut -d ' ' -f 4)
    ((SUM=$N0+$N1+$N2))
    echo "$SensorID $SUM"
done
exit 0
