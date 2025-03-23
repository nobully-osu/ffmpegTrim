import os
import subprocess

def setup():
    print("Installing ffmpeg via winget...\n")
    subprocess.run(["winget", "install", "Gyan.FFmpeg"])
    print("Installing python libraries via pip...\n")
    subprocess.run(["pip", "install", "ffmpeg-python", "configparser"])

    # generate config for storing options
    from configparser import ConfigParser

    print("Generating configuration file...")
    config = ConfigParser()

    config.read("config.ini")
    config.add_section("main")
    config.set("main", "audio", "aac")
    config.set("main", "video", "copy")
    config.set("main", "extension", "mp4")

    with open("config.ini", "w") as f:
        config.write(f)

    # declare download script is finished for user experience
    print("Done!\n")