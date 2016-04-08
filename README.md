# mrjob_pi
Calculating Pi with a MapReduce version of Gregory-Leibniz series https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

## prerequisites

pip install mrjob

## use

python mrjob_pi.py intervals.txt

or

seq 0 9999|python mrjob_pi.py
