#!/bin/bash
x=$(($(wc $1 | awk '{print $1}' | tail -n 1)))
y=$(($(wc bwa.sam | awk '{print $1}')))
echo "CHIMERIC:"
echo $x
echo "TOTAL READS:"
echo $y
echo "FREQUENCY OF CHIMERA:"
printf '%.10f\n' $(echo "$x/$y" | bc -l)
