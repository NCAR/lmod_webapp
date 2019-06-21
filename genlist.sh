#!/bin/bash

shopt -s expand_aliases
alias mod_avail='module -t av |& grep -v "/$"'

# First get default list
module purge
mod_avail > list.out

# Get list of compilers and MPIs
CMPLIST=($(grep -l -r 'family("compiler")' $MODULEPATH_ROOT | sed 's|.*compilers/\(.*\).lua|\1|'))
MPIALL=$(grep -l -r 'family("mpi")' $MODULEPATH_ROOT)

for CMP in ${CMPLIST[@]}; do
    echo "Processing $CMP ..."

    # Get MPI libraries specific to this compiler
    MPILIST=($(echo "$MPIALL" | grep $CMP | sed "s|.*${CMP}/\(.*\).lua|\1|"))

    # Load compiler and get available modules
    module load $CMP
    mod_avail | sed -n "\|/glade.*$CMP|,$ p" >> list.out

    # Load MPI and get available modules
    for MPI in ${MPILIST[@]}; do
        echo "Processing $CMP -> $MPI ..."
        module load $MPI
        mod_avail | sed -n "\|/glade.*$MPI|,$ p" >> list.out
        module unload $MPI
    done

    module unload $CMP
done
