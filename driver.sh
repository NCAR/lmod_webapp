#!/bin/bash -l

# Run bash scripts to collect data
./genlist.sh > /dev/null
./genhelp.sh > /dev/null

# Next, run Python code to generate website
# Reference: https://stackoverflow.com/questions/229551/how-to-check-if-a-string-contains-a-substring-in-bash
module purge
module load python
computing_system_name='$NCAR_HOST'
if [['flaskenvcasper' == *"$computing_system_name"*]];
then
  source flaskenvcasper/bin/activate
fi
if [['flaskenvcheyenne' == *"$computing_system_name"*]];
then
  source flaskenvcheyenne/bin/activate
fi
export FLASK_APP=document.py
flask run
