#!/bin/bash

echo "<html>" > index.html
echo "<head><meta charset=\"utf-8\"/></head>" >> index.html
echo "<body>" >> index.html
echo "<h3><a href="../index.html">Quantm-chemical calculations of diazonium salts</a></h3>" >> index.html
echo "<h4>Transition state of the de-diazonation reaction of diazonium salts:</h4>" >> index.html

echo "<ul>" >> index.html
list=`find . -maxdepth 1 -mindepth 1 -type d -printf "%f\n" | sort`
for i in $list
do
  echo " <li><a href=\"$i\">$i</a></li>" >> index.html
  cd $i
  ./make-index.sh
  cd ..
done
echo "</ul>" >> index.html

echo "<ul>" >> index.html
list=`ls *.out`
for i in $list
do
  name=`basename $i .out`
  echo " <li>$name <a href=\"$name.out\">out</a> <a href=\"$name.xyz\">xyz</a> <a href=\"$name.prop\">property</a> </li>" >> index.html
done
echo "</ul>" >> index.html

echo "</body>" >> index.html
echo "</html>" >> index.html
