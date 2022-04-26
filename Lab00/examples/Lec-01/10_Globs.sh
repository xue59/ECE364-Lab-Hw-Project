#! /bin/bash

#
# $Id$
#

# Some basic globs used with the ls command
echo "ls *"
ls *
echo 

echo "ls *.foo"
ls *.foo
echo 

echo "ls ee364*"
ls ee364*
echo 

echo "ls *bar*"
ls *bar*
echo 

echo "ls *.[ch]"
ls *.[ch]
echo 

# Globs are expanded before the command is executed
echo "echo FK[0-9]???"
echo JK[0-9]???
echo 

# Multiple sets of globs and fixed values can be used also
echo "./03_ScriptArguments.sh fixed1 ??[0-9]??? *.foo fixed2"
./03_ScriptArguments.sh fixed1 ??[0-9]??? *.foo fixed2
echo 

# Globs can be mixed with brace expansion
echo "echo ECE364/{labs,prelabs}/ee*1/p[1-2]"
echo ECE364/{labs,prelabs}/ee*1/p[1-2]
echo

exit 0

