# ffmpegTrim.py
# Video Trimming Script
# Written by nobully
# http://osu.ppy.sh/users/nobully

import os

#read in file location with user input
file_path=input("Location of video to trim: ")
#grab start time of clip
starttime=input("Start time of the clip: ")
#grab end time of clip
endtime=input("End time of the clip: ")
#strip original file extension, add _Trim.mp4 to denote the output file, and restore file extension
outputfile=file_path.rsplit( ".", 1 )[ 0 ]+"_Trim.mp4"

#passthru string to hard code ffmpeg command
ffmpegString="ffmpeg -i "+file_path+" -ss "+starttime+" -to "+endtime+" -c:v copy -c:a copy "+outputfile

#run ffmpeg with specified parameters
os.system(ffmpegString)