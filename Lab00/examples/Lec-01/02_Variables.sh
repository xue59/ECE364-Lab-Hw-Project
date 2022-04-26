#! /bin/bash

#
# $Id$
#

# Here are some basic variable definitions
var1=10
var2=3.1415
var3="EE364 is fun"
var4=$var3
var5=${var1}

echo $var1 $var2 $var3 $var4 $var5

# Sometimes you need to use curly braces to dissambiguate names when a veriable
# is embedded within a string
ten=10

# The variable $ten incorrectly includes the "s"
# $tens is never defined so it gets replaced with and empty string 
echo "There are $tens of students in this class."

# The curly braces make it clear that we only want to access the variable $ten
echo "There are ${ten}s of students in this class."

exit 0