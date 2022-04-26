#! /bin/bash

# A C-style while loop:
i=0
while (( i < 10 ))
do
    echo -n "$i "
    ((i++))
done
echo

# While loops can be used to execute a command over and over again until it exits with a non-zero value
# Rand will exit with 1 if it generates the number 4
amt=1000000
while rand.sh
do
    echo "Still no luck. Try again..."
    ((amt=amt/2))
done
echo "You win \$${amt}!"
echo 

# using break and continue to control loops:
i=0
j=0
while (( i < 100 ))
do
    ((i++))
    if (( i == 5 ))
    then
	continue
    fi
    
    if (( i == 10 ))
    then
	break
    fi

    ((j++))    
done

echo "i = $i, j = $j"


exit 0