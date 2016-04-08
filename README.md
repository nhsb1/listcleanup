# Stuff
=====================================================
Description stuff


Install
-------

Install stuff

Usage
-------
cleanup1.py -f source.csv > cleaned-up.csv


Options
-------
Options stuff

The goal: A clean file that's ready for import into some other system
The Source: source.csv is the starting point
Pre-work: source.csv was pulled from an Mturk raw output column no scrubbing otherwise

Requirements:
python string case must be installed (pip install stringcase); https://github.com/okunishinishi/python-stringcase

Usage: cleanup1.py -f source.csv > cleaned.csv

Takes a input file with rows that resembles: 
"jennifer D. Doe P.E./CM, jdoe@somedomain.org"
"BOB SMITH, bsmith@here.com"

And turns it into output that resembles:
"Jennifer Doe, jdoe@somedomain.org"
"Bob Smith, bsmith@here.com"

Bugs:
*fixed the regex bug on middle initals