#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-19 15:05:54 -0500 (Tue, 19 Jan 2016) $
#$Revision: 86178 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab01/getFinalScores.bash $
#$Id: getFinalScores.bash 86178 2016-01-19 20:05:54Z ee364b13 $

if [[ $# != 1 ]]
then
    echo "Usage: ./getFinalScores.bash <filename>"
    exit 1
fi

FILE=$@
if [[ ! -e $FILE ]]
then
    echo "Error reading input file: $FILE"
    exit 2
fi

OUTPUT=$(echo $FILE | cut -d "." -f 1)
FOUT="$OUTPUT.out"
if [[ -e $FOUT ]]
then
    echo "Output file $FOUT already exists"
    exit 3
fi

touch $FOUT

exec 4<$FILE
exec 5>$FOUT

while read line<&4
do
    name=$(echo $line | cut -d "," -f 1)
    assignment=$(echo $line | cut -d "," -f 2)
    midterm1=$(echo $line | cut -d "," -f 3)
    midterm2=$(echo $line | cut -d "," -f 4)
    project=$(echo $line | cut -d "," -f 5)
    let final=$assignment*15/100+$midterm1*30/100+$midterm2*30/100+$project*25/100
    echo "$name,$final" >&5
done
exit 0
