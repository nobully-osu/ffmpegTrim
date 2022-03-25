import wget
import os
from pyunpack import Archive
import shutil

ffmpegURL = 'https://github.com/GyanD/codexffmpeg/releases/download/5.0/ffmpeg-5.0-essentials_build.7z'

#download latest ffmpeg build from gyan.dev github
if not os.path.exists("ffmpeg-5.0-essentials_build.7z"):
    wget.download(ffmpegURL)

#actually extract the file
Archive("ffmpeg-5.0-essentials_build.7z").extractall(".")

#copy to main directory
shutil.copyfile("ffmpeg-5.0-essentials_build/bin/ffmpeg.exe", "ffmpeg.exe")

#remove zip file for cleanliness
os.remove("ffmpeg-5.0-essentials_build.7z")