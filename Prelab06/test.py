#! /usr/bin/env python3.4
#
#$Author$
#$Date$
#$Revision$
#$HeadURL$
#$Id$

import os
import sys
import re

input = "it is a number called 12, it is not -1.09, it is not 6, it is -10 greater than"

a = re.findall("-?(\d+).(\d+)",input)
print(a)