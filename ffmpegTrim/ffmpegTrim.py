# ffmpegTrim.py
# Video Trimming Script
# Written by nobully
# http://osu.ppy.sh/users/nobully
# https://github.com/randomman254/PythonScripts/

import os
import subprocess

#check for ffmpeg and download if needed
if not os.path.exists("ffmpeg\\bin\\ffmpeg.exe"):
    subprocess.call("ffmpegDownload.py", shell=True)

#announce version
print("ffmpegTrim v1.2.1")

#read in file location with user input
filePath = input("Location of video to trim (or drag and drop target video on window): ")

#grab start time of clip
startTime = input("Start time of the clip (hh:mm:ss): ")

#grab end time of clip
endTime = input("End time of the clip (hh:mm:ss): ")

#strip original file extension, add _Trim.mp4 to denote the output file, and restore file extension (old way)
#outputFile = filePath.rsplit( ".", 1 )[ 0 ] + "_Trim.mp4"

#store file extension in a neater way to account for other file extensions
outputFile, fileExtension = filePath.rsplit( ".", 1 )

#passthru string to (slightly less) hard coded ffmpeg command
ffmpegTrim = "ffmpeg -i " + filePath + " -ss " + startTime + " -to " + endTime + " -c:v copy -c:a copy " + outputFile + "_Trim." + fileExtension

#run ffmpeg with specified parameters
os.system(ffmpegTrim)