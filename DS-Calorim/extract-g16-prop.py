#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re

def get_gaussian_td(fname) :
#    f = open('%s/%s.td' % (fname, fname), 'r')
    f = open('%s.td' % (fname), 'r')
    E0 = 0.0
    H = 0.0
    S = 0.0
    G = 0.0
    for line in f :
	s = line.rstrip('\r\n')
	if 'Sum of electronic and zero-point Energies=' in s :
	    i = s.index("=")+1
	    E0 = float(s[i:])
	if 'Sum of electronic and thermal Enthalpies=' in s :
	    i = s.index("=")+1
	    H = float(s[i:])
	if 'Sum of electronic and thermal Free Energies=' in s :
	    i = s.index("=")+1
	    G = float(s[i:])
	    S = G - H
###	    print 'E0=%.8f  H=%.8f  S=%.8f  G=%.8f ' % (E0, H, S, G)
	    break
    return (E0, H, S, G)


def get_gaussian_wiberg(fname) :
    mr = []
    mfreq = []
    f = open('%s' % (fname), 'r')
    line = f.readline()
    flag = False
    NAtoms = 0
    while line:
#	print line
	line = f.readline()
	s = line.rstrip('\r\n')
	if ' NAtoms=' in s : 
		NAtoms = int(re.split(r'\s+', s)[2])
#	if 'E(B3LYP)' in s : print s[1:]
#	if 'E(UB3LYP)' in s : print s[1:]
#	if 'Zero-point correction=' in s : print s[1:]
#	if 'Thermal correction to Energy=' in s : print s[1:]
#	if 'Thermal correction to Enthalpy=' in s : print s[1:]
#	if 'Thermal correction to Gibbs Free Energy=' in s : print s[1:]
	if 'Sum of electronic and zero-point Energies=' in s : print s[1:]
	if 'Sum of electronic and thermal Energies=' in s : print s[1:]
	if 'Sum of electronic and thermal Enthalpies=' in s : print s[1:]
	if 'Sum of electronic and thermal Free Energies=' in s : print s[1:]
#	print s
	if ' Wiberg bond index matrix in the NAO basis:' in s :
	    f.readline()
	    f.readline()
	    f.readline()
	    flag = True
	    mw = []
	    for i in range(NAtoms) : mw.append([])
#	    print ' *** init ', mw
	    continue
	if 'Wiberg bond index, Totals by atom:' in s :
	    flag = False
#	    print ' *** Wiberg\n', mw
	    mr.append(mw)
	    continue
	if flag and len(s)<2 : continue
	if flag and 'Atom' in s : continue
	if flag and '----' in s : continue
	if flag :
	    i = int(re.split(r'\s+', s)[1][:-1])
	    m = list(map(float, re.split(r'\s+', s)[3:]))
#	    print ' ***', i, mw[i-1], type(mw[i-1])
	    mw[i-1].extend(m)
#	    print ' ***', i, mw[i-1]
	if ' Frequencies --' in s :
	    freq = list(map(float, re.split(r'\s+', s[16:])[1:]))
#	    print 'freq: ', freq, re.split(r'\s+', s[16:])
	    mfreq.extend(freq)
	    continue
    f.close()
    return mr[-3], mfreq


mw, mfreq = get_gaussian_wiberg(sys.argv[1])

#print mw
#print mfreq

print '\nWiberg:'
for lst in mw :
    for w in lst:
	print '%8.4f' % (w),
    print ''

print '\nFreq:'
for freq in mfreq :
    print '%10.4f' % (freq),
print ''


# Wiberg bond index matrix in the NAO basis:                                    
#
#     Atom    1       2       3       4       5
#     ---- ------  ------  ------  ------  ------
#   1.  C  0.0000  1.7840  1.0450  0.0050  0.9055
#   2.  O  1.7840  0.0000  0.1664  0.0096  0.0535
#   3.  O  1.0450  0.1664  0.0000  0.7179  0.0123
#   4.  H  0.0050  0.0096  0.7179  0.0000  0.0177
#   5.  H  0.9055  0.0535  0.0123  0.0177  0.0000

# Frequencies --    622.5210               677.2119              1045.6598

#E(B3LYP)= -1235.94645964
#Zero-point correction= 0.229019
#Thermal correction to Energy= 0.247022
#Thermal correction to Enthalpy= 0.247966
#Thermal correction to Gibbs Free Energy= 0.177937
#Sum of electronic and zero-point Energies= -1235.717441
#Sum of electronic and thermal Energies= -1235.699438
#Sum of electronic and thermal Enthalpies= -1235.698494
#Sum of electronic and thermal Free Energies= -1235.768523

# NAtoms=     19