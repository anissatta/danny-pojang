set term pngcairo size 800,140
set output "killtonda.png" 

unset ytics
set ylabel "INBOUND" rotate by 90

set style data histogram
set style histogram rowstacked
set style fill solid border -1
set boxwidth 0.75 
set xtics rotate by -90

unset key                          # Hide the legend if not needed
#set key left top
set yrange [0:*]                   # Ensure the y-axis starts at 0
plot 'killtonda.dat' using 2:xtic(1) title "YNA" lc rgb "navy" \
    ,'' using 3 title "Newsis" lc rgb "steelblue" \
    ,'' using 4 title "Other" lc rgb "dark-plum"

