#!/bin/bash
#
#   This script should be run in a cron. It submits script to
#   orchestrate updates on both Cheyenne and Casper. It updates
#   the Lmod module page for display on our Drupal front end.
#
#   Authors:         Thomas Johnson III, Brian Vanderwende
#   Last Revised:    10:54, 08 Jul 2019
#

# Use login nodes to run updates
DAVNODES=(casper01.ucar.edu casper26.ucar.edu)
CHEYNODES=(cheyenne{1..6}.head)

MYPATH="$( cd "$(dirname "$0")" ; pwd )"

function run_update {
    for LN in $1; do
        ssh $LN "cd $MYPATH; ./driver.sh"

        if [[ $? == 0 ]]; then
            break
        fi
    done
}

run_update $DAVNODES
run_update $CHEYNODES
