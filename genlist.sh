#!/bin/bash

module purge
module load ncarenv

# Specify system-specific output file
OUTFILE=$NCAR_HOST-list.out

# First get default list
module -t av |& grep -v "/$" | sed 's|.*/\(.*:\)|\1|' > $OUTFILE

# Get list of compilers and MPIs
CMPLIST=$(find $MODULEPATH_ROOT/ -type f -exec grep -l '^family("compiler")' {} \;)
MPILIST=$(find $MODULEPATH_ROOT/ -type f -exec grep -l '^family("mpi")' {} \;)

function check_hidden {
    SKIP=false

    if [[ ${HIDELIST}z != z ]]; then
        if grep -q $1 <<< "$HIDELIST"; then
            SKIP=true
            echo "Skipping hidden module $2"
        fi
    fi
}

function get_modules {
    MODPATH=$(echo $MODULEPATH | rev | cut -d: -f1 | rev)
    MYMODS=$(module -t av |& grep -v "/$" | sed -n "1,\|$MODPATH|!p")

    if [[ ${MYMODS}z != z ]]; then
        echo ${1}: >> $OUTFILE
        echo "$MYMODS" >> $OUTFILE
    fi
}

if [[ -f $MODULEPATH_ROOT/localinit/hidden.lua ]]; then
    HIDELIST=$(sed 's|.*"\(.*\)".*|\1|g' $MODULEPATH_ROOT/localinit/hidden.lua)
fi

for CMPFILE in ${CMPLIST[@]}; do
    CMP=$(sed 's|.*compilers/\(.*\).lua|\1|' <<< $CMPFILE)
    check_hidden $CMPFILE $CMP
    [[ $SKIP == true ]] && continue

    echo "Processing $CMP ..."

    # Get MPI libraries specific to this compiler
    SPECMPI=$(echo "$MPILIST" | grep $CMP)

    # Load compiler and get available modules
    module load $CMP
    get_modules $CMP

    # Load MPI and get available modules
    for MPIFILE in ${SPECMPI[@]}; do
        MPI=$(sed "s|.*${CMP}/\(.*\).lua|\1|" <<< $MPIFILE)
        check_hidden $MPIFILE $MPI
        [[ $SKIP == true ]] && continue
        
        echo "Processing $CMP -> $MPI ..."
        module load $MPI
        get_modules $MPI/$CMP
        module unload $MPI
    done

    module unload $CMP
done
