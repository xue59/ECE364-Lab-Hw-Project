#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-18 01:41:57 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85451 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab01/line_num.bash $
#$Id: line_num.bash 85451 2016-01-18 06:41:57Z ee364b13 $

if [[ $# == 0 ]]
then
    echo "Usage: line_num.bash <filename>"
    exit 1
elif [[ $# > 1 ]]
then
    echo "Please just provide one file name"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Cannot read $1"
    exit 1
fi

exec 4<$1
line=1
while read text<&4
do
    echo "$line:$text"
    let line=$line+1
done
exit 0
