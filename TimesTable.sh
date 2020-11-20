#!/bin/bash

#Simple Script to create a Multiplcation Table
#creates the TimesTable.csv in your PWD 

#setting reused variables
a=$(seq 1 40) #change the sequence range for different kind of tables
file=$PWD/TimesTable.csv

#function for top line of the table
xAxis()	{
echo X, | tr -d '\n' > $file
for b in $a
do
	echo $b, | tr -d '\n' >> $file
done 
echo  >> $file
}

#function for the side line and the actual table 
yAxis_table()	{
for x in $a  
do 
	echo $x, | tr -d '\n' >> $file
	for y in $a
	do 
		z=$((x*y))
		echo $z, | tr -d '\n' >> $file
	done
	echo  >> $file
done
}

xAxis
yAxis_table
