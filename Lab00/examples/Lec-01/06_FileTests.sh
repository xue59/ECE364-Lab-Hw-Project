#! /bin/bash

#
# $Id$
#

# The file name is passed as the 1st command line argument
# Recall that $? will be 0 when the test is TRUE!

# Does the file exist?
[[ -e $1 ]]
echo "[[ -e $1 ]] result: \$? =" $?

# is the file an ordinary file?
[[ -f $1 ]]
echo "[[ -f $1 ]] result: \$? =" $?

# is the file a directory?
[[ -d $1 ]]
echo "[[ -d $1 ]] result: \$? =" $?

# does the current user have read permissions?
[[ -r $1 ]]
echo "[[ -r $1 ]] result: \$? =" $?

# does the current user have write permissions?
[[ -w $1 ]]
echo "[[ -w $1 ]] result: \$? =" $?

# does the current user have execute permissions?
[[ -x $1 ]]
echo "[[ -x $1 ]] result: \$? =" $?

# is the file exist and not empty?
[[ -s $1 ]]
echo "[[ -s $1 ]] result: \$? =" $?

# is the file and ordinary file and executable?
[[ -f $1 && -x $1 ]]
echo "[[ -e $1 && -x $1 ]] result: \$? =" $?

# is the path stored in the $HOME varialbe a directory and writeable?
[[ -d $HOME && -w $HOME ]]
echo "[[ -d $HOME && -w $HOME ]] result: \$? =" $?

# is the path not a directory and empty?
[[ ! -d $1 && ! -s $1 ]]
echo "[[ ! -d $1 && ! -s $1 ]] result: \$? =" $?

exit 0