# Listcleanup
-------
Produces a clean output file that's ready for use in some other system

I had a results .csv file that came from some mechnical turk hits that I had created, with varying output (very small sample provided in the repo: source.csv). I needed a way to clean-up the output for use in a email marketing campaign, because the data set had several formatting problems (e.g. variation on middle names/initials, professional abbreviations that I didn't care about, varying cases, etc.).  The result, is this listcleanup tool.


Install
-------
I haven't packaged this via pip, so you'll have to download the .py file, and install the pre-reqs... argparse, re, stringcase. 
 
Usage
-------
cleanup1.py -f source.csv > cleaned-up.csv


Takes a input file with rows that resembles: 

"jennifer D. Doe P.E./CM, jdoe@somedomain.org"

And turns it into output that resembles:

"Jennifer Doe, jdoe@somedomain.org"

Options
-------
NA

Notes
-------

fixed the regex bug on middle names & initals