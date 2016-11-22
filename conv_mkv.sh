#! /bin/bash


if [ "$#" -ne 1  ]; then
    echo ""
    echo "USAGE:"
    echo ""
    echo "conv_mkv <FOLDER>"
    echo "          converts all files in FOLDER and places them in the current working dir"
    echo ""
    echo ""
    exit -1
fi

DIR=$1
FILES=$(ls $DIR | grep *.mkv) # get files

for i in $FILES; do
    
    # get filename without .ext 
    filename=$(basename $i)
    filename=${filename%.*}
    
    echo ""
    echo "Converting $filename"
    echo ""
    sleep 2 # give a chance to check file name 
    
    HandBrakeCLI -i $i -o $filename.mp4 --preset="High Profile" --denoise="medium" --cfr --quality 22

    # if HandBrakeCLI fails exit with error 
    if [ $? != 0 ]; then
        echo ""
        echo ""
        echo "ERROR: HandBrakeCLI exit non 0"
        echo ""
        echo ""
        exit -1
    fi

    # check if the mp4 exists
    if [ -e $filename.mp4 ]; then 
        rm $i
    else
        echo ""
        echo "DST file not found..."
        exit -1
    fi
    
done

