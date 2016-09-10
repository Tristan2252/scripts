#! /bin/bash
DIR=$1
FILES=$(ls $DIR | grep .mkv)

for i in $FILES; do
    filename=$(basename $i)
    filename=${filename%.*}

    echo $filename
    HandBrakeCLI -i $i -o $DIR$filename.mp4 --preset="High Profile" --denoise="medium" --cfr --quality 22
    
    if [ $? != 0 ]; then
        echo "ERROR: HandBrakeCLI exit non 0"
        exit -1
    fi

    rm $i
done
