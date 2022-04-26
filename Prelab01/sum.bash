#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-18 01:40:59 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85450 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab01/sum.bash $
#$Id: sum.bash 85450 2016-01-18 06:40:59Z ee364b13 $

i=0
for arg in $@
do
    let i+=$1
    shift
done
echo $i
exit 0
