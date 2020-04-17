a=$1
head -n 1 $a/364253dFlat.csv > $a/totalFlat.csv 
tail -q -n +2 $a/3*Flat.csv >> $a/totalFlat.csv
tail -q -n +2 $a/4*Flat.csv >> $a/totalFlat.csv
