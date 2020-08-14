#!/bin/bash

echo "<html>" > index.html
echo "<head><meta charset=\"utf-8\"/></head>" >> index.html
echo "<body>" >> index.html
echo "<h3>Quantm-chemical calculations of diazonium salts</h3>" >> index.html
echo "<h4><a href=\"DS/index.html\">Structures of diazonium salts</a></h4>" >> index.html
echo "<h4><a href=\"TS/index.html\">Transition state of the de-diazonation reaction of diazonium salts</a></h4>" >> index.html
echo "<h4><a href=\"DS-Cluster/index.html\">Structures of cluster DS in LC-MS experiment</a></h4>" >> index.html

#echo "<ul>" >> index.html
list=`find . -maxdepth 1 -mindepth 1 -type d -printf "%f\n" | sort`
for i in $list
do
#  echo " <li><a href=\"$i\">$i</a></li>" >> index.html
  cd $i
  ./make-index.sh
  cd ..
done
#echo "</ul>" >> index.html

echo "</body>" >> index.html
echo "</html>" >> index.html
