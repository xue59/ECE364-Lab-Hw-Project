#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-19 15:05:54 -0500 (Tue, 19 Jan 2016) $
#$Revision: 86178 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab01/getCourseStats.bash $
#$Id: getCourseStats.bash 86178 2016-01-19 20:05:54Z ee364b13 $

if [[ $# != 1 ]]
then
    echo "Usage: ./getCourseStats.bash <course name>"
    exit 1
fi

if [[ $1 != "ece364" &&  $1 != "ece337" &&  $1 != "ece468" ]]
then
    echo "Error: course $1 is not a valid option."
    exit 5
fi

for file in $(ls gradebooks/$@*.txt)
do
    getFinalScores.bash $file
    if [[ $? != 0 ]]
    then
        echo "Error while running getFinalScores.bash"
        exit 3
    fi
done

TOTALSTUDENT=0
AVERAGE=0
HIGHEST=0
WINNER=""

for outfile in $(ls gradebooks/$@*.out)
do
    exec 4<$outfile
    while read line<&4
    do
        let TOTALSTUDENT=$TOTALSTUDENT+1
        thisscore=$(echo $line | cut -d "," -f 2)
        let AVERAGE=$AVERAGE+$thisscore
        if [[ $thisscore > $HIGHEST ]]
        then
            HIGHEST=$thisscore
            WINNER=$(echo $line | cut -d "," -f 1)
        fi
    done
done

let AVERAGE=$AVERAGE/$TOTALSTUDENT
echo "Total students: $TOTALSTUDENT"
echo "Average score: $AVERAGE"
echo "$WINNER had the highest score of $HIGHEST"
exit 0
