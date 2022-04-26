#! /bin/bash

#
# $Id$
#

x=10
y=6
z=3

# Just some examples of numeric tests

(( $x == $y ))
echo "(( $x == $y )) result: \$? =" $?

(( $x != $y ))
echo "(( $x != $y )) result: \$? =" $?

(( $x <= $y ))
echo "(( $x <= $y )) result: \$? =" $?

(( $x >= $y ))
echo "(( $x >= $y )) result: \$? =" $?

(( $x < $y ))
echo "(( $x < $y )) result: \$? =" $?

(( $x > $y ))
echo "(( $x > $y )) result: \$? =" $?

(( $x != $z && $x > $y ))
echo "(( $x != $z && $x > $y )) result: \$? =" $?

(( $x == $z || $y <= $z ))
echo "(( $x == $z || $y <= $z )) result: \$? =" $?

# Arithmetic expressions can also be used:
(( $x < $y + $z ))
echo "(( $x < $y + $z )) result: \$? =" $?

(( $x > 10 + $y || 3 == $z ))
echo "(( $x > 10 + $y || 3 == $z )) result: \$? =" $?

exit 0