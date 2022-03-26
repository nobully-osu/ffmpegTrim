import os
import shutil
import sys
import subprocess

ffmpegURL = 'https://github.com/GyanD/codexffmpeg/releases/download/5.0/ffmpeg-5.0-essentials_build.7z'

#get pip packages if they are missing
#implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'wget', 'patool', 'pyunpack'])

#download latest ffmpeg build from gyan.dev github
from pyunpack import Archive
import wget

print("\nDownloading ffmpeg...\n")
wget.download(ffmpegURL)

#actually extract the file
Archive("ffmpeg-5.0-essentials_build.7z").extractall(".")

#rename the ffmpeg folder for easier code writing
os.rename("ffmpeg-5.0-essentials_build", "ffmpeg")

#copy ffmpeg.exe next to the script
shutil.copyfile("ffmpeg/bin/ffmpeg.exe", "ffmpeg.exe")

#remove zip file for cleanliness
os.remove("ffmpeg-5.0-essentials_build.7z")

#declare download script is finished for user experience
print("\n\nDone!\n")