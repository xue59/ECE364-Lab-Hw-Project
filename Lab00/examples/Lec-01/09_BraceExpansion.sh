#! /bin/bash

#
# $Id$
#

# Some very basic brace expansions
echo "{1..10} -> " {1..10}
echo "{a..e} -> " {a..e}
echo "{a..z}{1..3} -> " {a..z}{1..3}
echo "ee364{a..c}{1..3} -> " ee364{a..c}{1..3}
echo "a{b,C,5}f -> " a{b,C,5}f
echo "{1,2}x{a..b} -> " {1,2}x{a..b}

echo 
echo

# More complicated sequences can be constructed:
# Under each directory we want to have a directory for each student account 
# Under each student account directory we want to have folders for each problem
# 
#                          ECE364
#                            |
#        prelabs ---------- labs ---------- results
#          |                 |               |
#         ...     ee364a1 ....... ee364c3   ...
#                    |               |
#               p1 p2 p3 p4           ...
#

# This will be a lot of directories
echo ECE364/{prelabs,labs,results}/ee364{a..c}{1..3}/p{1..4}

# We can actually create all of these with a simgle mkdir
# The p flag tells mkdir to create any non-existant directory along a path
# Note: you will need write permissions to run this command
mkdir -p ECE364/{prelabs,labs,results}/ee364{a..c}{1..3}/p{1..4}

exit 0