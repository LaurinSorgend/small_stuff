#small script to rencode all mp4s in a folder in av1 using ffmpeg
from dotenv import load_dotenv
import os
load_dotenv()
import subprocess as sp


FOLDER_PATH = os.getenv("FOLDER_PATH")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")

# get all mp4s in folder
files = os.listdir(FOLDER_PATH)
mp4s = [f for f in files if f.endswith(".mp4")]



# encode all mp4s in folder 
for mp4 in mp4s:
    sp.check_call(["ffmpeg", "-i", os.path.join(FOLDER_PATH, mp4), "-c:v", "libaom-av1", "-crf", "23", os.path.join(OUTPUT_PATH, mp4)])
