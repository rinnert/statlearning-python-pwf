#!/bin/bash

pad=`xsetwacom list | grep "PAD" | gawk '{ id=NF-2; print($id);}'`
stylus=`xsetwacom list | grep "STYLUS" | gawk '{ id=NF-2; print($id);}'`
eraser=`xsetwacom list | grep "ERASER" | gawk '{ id=NF-2; print($id);}'`
touch=`xsetwacom list | grep "TOUCH" | gawk '{ id=NF-2; print($id);}'`

# pad
xsetwacom set ${pad} RawSample 12
xsetwacom set ${pad} Suppress 10
xsetwacom set ${pad} Button 9 "key PgUp" 
xsetwacom set ${pad} Button 8 "key PgDn"
xsetwacom set ${pad} Button 1 "key control v"
xsetwacom set ${pad} Button 3 "key control c"

# stylus
xsetwacom set ${stylus} RawSample 12
xsetwacom set ${stylus} Suppress 10
xsetwacom set ${stylus} Button 2 "key control z"
xsetwacom set ${stylus} Button 3 "key control z"

# eraser
xsetwacom set ${eraser} Suppress 10
xsetwacom set ${eraser} RawSample 12
#xsetwacom set ${eraser} Button 1 1
xsetwacom set ${eraser} Button 2 "key -"
xsetwacom set ${eraser} Button 3 "key ="

# touch
xsetwacom set ${touch} Touch off
xsetwacom set ${touch} Gesture off
