#!/bin/env python
# -*- coding: utf-8 -*-
import argparse

def skriv(str, verbosity, nl=True):
  if verbosity:
    if nl:
      print str
    else:
      print str,

parser = argparse.ArgumentParser(description="Enkel kalkulator (multiplisering av heltall)")
parser.add_argument('faktorer', metavar="N", type=int, nargs=2, help="2 fakorer for multiplikasjonen")
parser.add_argument('-verbose', '-v', action='store_true', help="Skriver ut stegene i multiplikasjonen")
parser.add_argument('-exact', '-x', action='store_true', help="Utfører multiplikasjonen uten å sortere argumentene")
parser.add_argument('-metode', '-m', action='store_true', help="Viser hvordan multiplikasjonen utføres")
args = parser.parse_args()

if args.exact:
  faktorer = args.faktorer
else:
  faktorer = sorted(args.faktorer)

skriv("Faktorer: ", args.verbose, False) 
skriv( faktorer, args.verbose)
sum=0
for x in range (0, faktorer[0]):
  sum += faktorer[1]
  skriv("Runde {}, sum {}".format(x+1, sum), args.verbose)
  if x==0:
    metode="  " + str(faktorer[1])
  else:
    metode += " + {}".format(str(faktorer[1]))

skriv(metode + " = " + str(sum), args.metode)
#print metode
print "Summen av \"{} x {}\" er: {}".format(args.faktorer[0], args.faktorer[1], sum)

