set terminal epslatex color
set output "temp.eps"
set xlabel '{\Large $\alpha$}'
set ylabel '{\Large $\beta$}'
set label 1 '{\Large (b)}' at -2.8,0.9
set key at 3,-0.5
plot [-pi:pi][-1.1:1.1] sin(x) title "{{/Symbol g}=1}", sin(x)**2 title "{{/Symbol g}=2}", sin(x)**3 title "{{/Symbol g}=3}" lt 5 lc rgb "blue"
quit