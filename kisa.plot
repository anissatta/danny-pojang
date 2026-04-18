set term pngcairo size 800,340
set output "kisa.png" 

set ylabel "OLD: -90 min" rotate by 90
#unset ytics

set style data histogram
set style histogram clustered gap 1
set style fill solid border -1
set boxwidth 0.75 
set xtics rotate by -90

unset key                          # Hide the legend if not needed
set yrange [0:*]                   # Ensure the y-axis starts at 0
plot 'kisa.dat' using 2:xtic(1) title "articles" lc rgb "black" 

