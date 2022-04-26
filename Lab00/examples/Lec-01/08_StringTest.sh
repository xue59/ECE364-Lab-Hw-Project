#! /bin/bash

#
# $Id$
#

# The third string will come from the 1st command line argument
str1="foo"
str2="bar"
str3=$1

[[ -z $str3 ]]
echo "[[ -z \"$str3\" ]] result: \$? =" $? 

[[ -n $str3 ]]
echo "[[ -n \"$str3\" ]] result: \$? =" $? 

[[ $str1 = $str2 ]]
echo "[[ \"$str1\" = \"$str2\" ]] result \$? =" $?

[[ $str1 != $str2 ]]
echo "[[ \"$str1\" != \"$str2\" ]] result \$? =" $?

[[ $str1 < $str2 ]]
echo "[[ \"$str1\" < \"$str2\" ]] result \$? =" $?

[[ $str1 > $str2 ]]
echo "[[ \"$str1\" > \"$str2\" ]] result \$? =" $?

[[ ! -z $str1 && ! -z $str3  ]]
echo "[[ ! -z \"$str1\" && ! -z \"$str3\" ]] result \$? =" $?

exit 0