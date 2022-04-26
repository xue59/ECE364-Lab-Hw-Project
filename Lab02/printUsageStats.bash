#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-26 15:13:47 -0500 (Tue, 26 Jan 2016) $
#$Revision: 86921 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab02/printUsageStats.bash $
#$Id: printUsageStats.bash 86921 2016-01-26 20:13:47Z ee364b13 $

if (( $# != 1 ))
then
    echo "Usage: ./printUsageStats.bash <filename>"
    exit 1
fi

if [[ ! -r $1 || ! -e $1 ]]
then
    echo "$1 does not exist."
    exit 2
fi

timestamp=$(cat $1 | head -n1 | cut -d" " -f3)
echo "Parsing file \"$1\". Timestamp: $timestamp"
echo "Your choices are:"
echo "1) Active user IDs"
echo "2) N Highest CPU usages"
echo "3) N Highest mem usages"
echo "4) Top 3 longest running processes"
echo "5) All processes by a specific user"
echo "6) Exit"

i=1
j=0
linenum=$(wc $1 -l | cut -d" " -f1)
((linenum=$linenum-7))
while ((i==1))
do
    echo " "
    read -p "Please enter your choice: " choice
    if [[ $choice != 1 && $choice != 2 && $choice != 3 && $choice != 4 && $choice != 5 && $choice != 6 ]]
    then
        echo "Please choose between 1 to 6"
    elif (($choice == 1))
    then
        active=$(cat $1 | head -n1 | cut -d" " -f8)
        echo "Total number of active user IDs: $active"
    elif (($choice == 2))
    then
        read -p "Enter a value for N: " value2
        r2=($(tail $1 -n $linenum | sort -k9rn | head -n$value2 | cut -d" " -f2,9))
        let value2=$value2*2
        for ((j=0; j<$value2; j=$j+2))
        do
            let k=$j+1
            echo "User ${r2[j]} is utilizing CPU resources at ${r2[k]}%"
        done
    elif (($choice == 3))
    then
        read -p "Enter a value for N: " value3
        r3=($(tail $1 -n $linenum | sort -k10,10rn | head -n$value3 | cut -d" " -f2,10))
        let value3=$value3*2
        for ((j=0; j<$value3; j=$j+2))
        do
            let k=$j+1
            echo "User ${r3[j]} is utilizing mem resources at ${r3[k]}%"
        done
    elif (($choice == 4))
    then
        r4=($(sort -k11,11rn $1| head -n3 | cut -d" " -f1,12))
        echo "PID: ${r4[0]}, cmd: ${r4[1]}"
        echo "PID: ${r4[2]}, cmd: ${r4[3]}"
        echo "PID: ${r4[4]}, cmd: ${r4[5]}"
    elif (($choice == 5))
    then
        read -p "Please enter a valid username: " username
        match=$(tail $1 -n $linenum | cut -d" " -f2 | grep -w $username | wc -l)
        if (( $match==0 ))
        then
           echo "No match found"
        else
            r5=($(tail $1 -n $linenum | grep -w $username | cut -d" " -f9,12))
            let value5=$match*2
            for ((j=0; j<$value5; j=$j+2))
            do
                let k=$j+1
                echo ${r5[j]} ${r5[k]}
            done
        fi
    elif (($choice == 6))
    then
        break
    fi
done

exit 0
