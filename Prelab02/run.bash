#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-24 16:29:17 -0500 (Sun, 24 Jan 2016) $
#$Revision: 86593 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab02/run.bash $
#$Id: run.bash 86593 2016-01-24 21:29:17Z ee364b13 $

if (($# != 2))
then
    echo "Usage: run.bash <.c filename> <output filename>"
    exit 1
fi

if ! gcc $1 -o quick_sim
then
    echo "error: quick_sim could not be compiled!"
    exit 2
fi

filename=$2
while [[ -e $filename ]]
do
    read -p "$filename exists. Would you like to delete it? " yn
    if [[ $yn == "y" || $yn == "yes" ]]
    then
        rm $filename 2>/dev/null
    elif [[ $yn == "n" || $yn == "no" ]]
    then
        read -p "Enter a new filename: " filename
    fi
done

touch $filename
caches=(1 2 4 8 16 32)
issues=(1 2 4 8 16)
fast=99999999

exec 7>$filename

for c in ${caches[*]}
do
    for i in ${issues[*]}
    do
        cpi=$(quick_sim $c $i a | cut -d ":" -f8)
        exe=$(quick_sim $c $i a | cut -d ":" -f10)
        if (( $exe < $fast ))
        then
            f_p="AMD Opteron"
            f_c=$c
            f_i=$i
            fast=$exe
        fi
        echo "AMD Opteron:$c:$i:$cpi:$exe">&7
        
        cpi=$(quick_sim $c $i i | cut -d ":" -f8)
        exe=$(quick_sim $c $i i | cut -d ":" -f10)
        if (( $exe < $fast ))
        then
            f_p="Intel Core i7"
            f_c=$c
            f_i=$i
            fast=$exe
        fi
        echo "Intel Core i7:$c:$i:$cpi:$exe">&7
    done
done
echo "Fastest run time achieved by $f_p with cache size $f_c and issue width $f_i was $fast"
exit 0
