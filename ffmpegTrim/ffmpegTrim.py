import os
import ffmpegSetup

# init json configuration file for if first run
if not os.path.exists("config.ini"):
    print("Running first time setup...\n")
    ffmpegSetup.setup()

import ffmpeg
from configparser import ConfigParser
config = ConfigParser()

# read in config
config.read("config.ini")

# config variables
audioCodec = config.get("main", "audio")
videoCodec = config.get("main", "video")
fileExtension = config.get("main", "extension")

# get user input
print("ffmpegTrim v3.0.0")

inputPath = input("Path to video (or drag and drop): ")
inputPath = inputPath.strip('\"\'')
startTime = input("Start time of clip (mm:ss): ")
endTime = input("End time of clip (mm:ss): ")

# split file extension and append to filename to indicate trimmed video, also change extension to reflect configuration file
tempPath, tempFileExtension = inputPath.rsplit( ".", 1 )
outputPath = tempPath + "_Trim." + fileExtension

# check for existing clips and increment filename
# this is technically the slow way but not many people will be creating millions of clips from a single 10-15 min replay buffer so idc
if os.path.exists(outputPath):
    i = 1
    while os.path.exists(outputPath):
        tempPath, tempFileExtension = inputPath.rsplit( ".", 1 )
        outputPath = tempPath + "_Trim%s." % i + fileExtension
        i += 1
else: pass

# run ffmpeg via wrapper library (new method)
# stream copy will not work with .trim() as reencoding is required or something idk
# for whatever fuckass reason i have to specify aac for audio stream now even though copy worked in the past
(
    ffmpeg
    .input(inputPath)
    .output(outputPath, ss=startTime, to=endTime, acodec=audioCodec, vcodec=videoCodec)
    .run()
)