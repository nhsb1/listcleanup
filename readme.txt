The goal: A clean file that's ready for import into some other system
The Source: test2.csv is the starting point
Pre-work: Test2.csv was pulled from an Mturk raw output column no scrubbing otherwise

Usage: cleanup1.py -f source.csv > cleaned.csv

Takes a input file with rows that resembles: 
"jennifer D. Doe P.E./CM, jdoe@somedomain.org"
"BOB SMITH, bsmith@here.com"

And turns it into output that resembles:
"Jennifer Doe, jdoe@somedomain.org"
"Bob Smith, bsmith@here.com"

Bugs:
*fixed the regex bug on middle initals