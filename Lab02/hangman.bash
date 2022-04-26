#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-26 15:56:24 -0500 (Tue, 26 Jan 2016) $
#$Revision: 86961 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Lab02/hangman.bash $
#$Id: hangman.bash 86961 2016-01-26 20:56:24Z ee364b13 $

list=(banana parsimonious sesquipedalian)

let i=$RANDOM%3
word=${list[i]}
len=$(echo "$word" | wc -c)
let len=$len-1

wordlist=(b a n a n a)
dotlist=(. . . . . .)
if (($len==14))
then
    wordlist=(s e s q u i p e d a l i a n)
    dotlist=(. . . . . . . . . . . . . .)
elif (($len==12))
then
    wordlist=(p a r s i m o n i o u s)
    dotlist=(. . . . . . . . . . . .)
fi
echo "Your word is $len letters long"
show=""
q=1
match=0
cont=0

while (( q==1 ))
do
    cont=0
    for (( j=0; j<$len; j++ ))
    do
        if [[ ${dotlist[j]} != ${wordlist[j]} ]]
        then
            cont=1
        fi
    done

    if (( cont==0 ))
    then
        echo "Congratulations! You made the guess of word $word!"
        break;
    fi

    show="Word is: "
    for (( j=0; j<$len; j++ ))
    do
        show=$(echo $show${dotlist[j]})
    done
    echo $show

    match=0
    read -p "Make a guess: " n
    for (( j=0; j<$len; j++ ))
    do 
        if [[ ${dotlist[j]} == $n ]]
        then
            match=2
        elif [[ ${wordlist[j]} == $n ]]
        then
            match=1
            dotlist[j]=$n
        fi
    done

    if (( $match==0 ))
    then
        echo "  Sorry, try again."
    elif (( $match==1 ))
    then
        echo "  Good going!"
    else
        echo "  Already got."
    fi
    echo
done
exit 0
