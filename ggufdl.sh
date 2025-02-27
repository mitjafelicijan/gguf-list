#!/usr/bin/env sh

DATA_FILE="dialog-data.txt"

exit_script() {
	clear
	exit 1
}

download_dir=$(dialog --stdout --title "Where should models be downloaded?" --dselect $HOME/ 20 70)
if [ -z "$download_dir" ]; then exit_script; fi

data=$(sed -n "s/^c://p" $DATA_FILE)
collection=$(dialog --stdout --title "Select collection" --menu "Choose from the list:" 25 60 20 $data)
if [ -z "$collection" ]; then exit_script; fi
echo $collection

data=$(sed -n "s/^m:$collection://p" $DATA_FILE)
models=$(dialog --stdout --title "Select models" --checklist "Choose from the list:" 25 80 20 $data)
if [ -z "$models" ]; then exit_script; fi

dialog --stdout --yesno "Begin downloading selected models?" 7 50
confirm=$?
if [ $confirm -ne 0 ]; then exit_script; fi

clear

for model in $models; do
	repository=$(grep "f:$model" dialog-data.txt | awk '{print $2}' | uniq)
	echo "> $model => $repository"
	wget --progress=bar --continue "$repository" -P "$download_dir"
done

