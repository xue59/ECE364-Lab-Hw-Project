#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-18 01:53:47 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85455 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab01/exist.bash $
#$Id: exist.bash 85455 2016-01-18 06:53:47Z ee364b13 $

for arg in $@
do
    if [[ -r $arg ]]
    then
	echo "File $arg is readable"
    elif [[ ! -r $arg && ! -e $arg ]]
    then
	touch $arg
    fi
done
exit 0
