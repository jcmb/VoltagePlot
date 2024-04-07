
set datafile separator ","
set terminal png size 900,600 noenhanced font '/usr/share/fonts/msttcorefonts/arial.ttf' 10
set xtics border mirror
set grid xtics mxtics ytics
set mxtics 5

set key outside

set style data lines
set xdata time
set timefmt "%s"
set format x "%H:%M"

Local_Time_Offset=3600*Local_TZ
#Local_Time_Offset=0
Local_Hours=Local_Time_Offset/3600

set ylabel "Voltage"

set y2tics
set y2label "Source in use"



if (Local_Time_Offset == 0) {
    set xlabel "GPS Time"
} else {
    set xlabel "Local Time TimeZone ".Local_Hours
    }


set title name."Voltage over time"
set output "Voltage.png"
plot \
     'file' using ($1+Local_Time_Offset):($2) title "External 1",\
     'file' using ($1+Local_Time_Offset):($3) title "External 2",\
     'file' using ($1+Local_Time_Offset):($4) title "USB",\
     'file' using ($1+Local_Time_Offset):($5) title "Battery 1",\
     'file' using ($1+Local_Time_Offset):($6) title "Battery 2",\
     'file' using ($1+Local_Time_Offset):($7) title "Source" axis x1y2

set title name." Voltage & Temp"
set output "VoltTemp.png"

set y2tics
set y2label "Temperature (celsius)"


plot \
     'file' using ($1+Local_Time_Offset):($2) title "External 1",\
     'file' using ($1+Local_Time_Offset):($3) title "External 2",\
     'file' using ($1+Local_Time_Offset):($4) title "USB",\
     'file' using ($1+Local_Time_Offset):($5) title "Battery 1",\
     'file' using ($1+Local_Time_Offset):($6) title "Battery 2",\
     'file' using ($1+Local_Time_Offset):($8) title "Internal Temperature" axis x1y2

set title name." Temperatures"
set output "Temp.png"

set ylabel "Temperature (celsius)"

unset y2tics
unset y2label



plot \
     'file' using ($1+Local_Time_Offset):($8) title "Internal Temperature",\
     'file' using ($1+Local_Time_Offset):($9) title "Radio Temperature",\
     'file' using ($1+Local_Time_Offset):($10) title "Cell Temperature"


quit
