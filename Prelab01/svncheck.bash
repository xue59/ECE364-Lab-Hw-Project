#! /bin/bash
#
#$Author: ee364b13 $
#$Date: 2016-01-18 01:49:24 -0500 (Mon, 18 Jan 2016) $
#$Revision: 85452 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364b13/Prelab01/svncheck.bash $
#$Id: svncheck.bash 85452 2016-01-18 06:49:24Z ee364b13 $

exec 4<file_list
while read filename<&4
do
    echo "$filename: checking..."
    SVN=$(svn status $filename | head -c 1) #"" if it is in svn or not exists
    #file not in svn but exists
    if [[ $SVN == '?' && -e $filename ]]
    then
        if [[ ! -x $filename ]]
        then
            echo "Would you like to make it executable?[y/n]"
            read ans
            if [[ $ans == 'y' ]]
            then
                chmod +x $filename
            fi
        fi
        svn add $filename
    #file in svn but not executable
    elif [[ $SVN == "" && -e $filename && ! -x $filename ]]
    then
        svn propset svn:executable ON $filename
    #file not in svn and does not exist
    elif [[ $SVN == "" && ! -e $filename ]]
    then
        echo "Error: File $filename appears to not exist here or in svn"
        exit 1
    fi
done
echo "Auto-committing code"
svn commit
exit 0
