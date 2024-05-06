#! /bin/bash

# folder structure generator for the folders

arr=(.config test .build res doc src tools)
for val in ${arr[*]}
	do
		echo $val
		mkdir $val
	done