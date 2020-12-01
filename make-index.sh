#!/bin/bash

echo "<html>" > index.html
echo "<head><meta charset=\"utf-8\"/></head>" >> index.html
echo "<body>" >> index.html
echo "<h3>Quantm-chemical calculations of diazonium salts</h3>" >> index.html
echo "<h4><a href=\"https://alexanderbondarev.github.io/DS-Scan-CN/\">Scanning the surface of potential energy when changing the C<sup>1</sup>-N<sup>1</sup> distance for diazonium salts</a></h4>" >> index.html
echo "<h4><a href=\"https://alexanderbondarev.github.io/DS-Scan-CH/\">Scanning the surface of potential energy when changing the C<sup>2</sup>-H distance for diazonium salts (DFT B3LYP 6-31G(d,p))</a></h4>" >> index.html
echo "<h4><a href=\"https://alexanderbondarev.github.io/DS-Scan-NX/\">Scanning the surface of potential energy when changing the N<sup>2</sup>-X distance for diazonium salts (DFT B3LYP 6-31G(d,p))</a></h4>" >> index.html
echo "<h4><a href=\"DC/index.html\">Diazonium cations ant other</a></h4>" >> index.html
echo "<h4><a href=\"DS/index.html\">Structures of diazonium salts</a></h4>" >> index.html
echo "<h4><a href=\"TS/index.html\">Transition state of the de-diazonation reaction of diazonium salts</a></h4>" >> index.html
echo "<h4><a href=\"DS-Cluster/index.html\">Structures of cluster DS in LC-MS experiment</a></h4>" >> index.html
echo "<h4><a href=\"DS-Calorim/index.html\">Thermodinamics of desctruction DS</a></h4>" >> index.html
echo "<h4><a href=\"https://zenodo.org/record/1473203\">Molecular-Orbitals-Tracer</a> <a href=\"https://www.youtube.com/playlist?list=PL5qseqn2svhL9RDIxBpQfJB_fO2m6-anu\">Video</h4>" >> index.html

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
