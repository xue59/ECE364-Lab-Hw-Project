#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-02-16 15:19:33 -0500 (Tue, 16 Feb 2016) $
#$Revision: 88257 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab05/scheduler.bash $
#$Id: scheduler.bash 88257 2016-02-16 20:19:33Z ee364b13 $

if (( $# != 1 ))
then
    echo "Usage: ./scheduler.bash <filename>"
    exit 1
fi

if [[ ! -r $1 || ! -e $1 ]]
then
    echo "$1 does not exist."
    exit 2
fi

outname="schedule.out"
if [[ -e $outname ]]
then
	echo "$outname already exists."
	exit 3
fi
touch $outname
exec 4>>$outname
first="  	07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00"
echo  "		" $first>&4

alllist=(07:00 08:00 09:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00)
while read -a line
do
	name=$(echo $line | cut -d" " -f 1)
	time=$(echo $line | cut -d" " -f 2)
	ind=0
	for i in $time
	do
		if [[ $i=="," ]]
		then
			time[ind]=" "
		fi
		((ind=ind+1))
	done
	little=($time)
	for slot in ${alllist[*]}
	do
		
		echo $name>&4
	done
	
done < $1
exit 0

