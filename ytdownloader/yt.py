import subprocess
import os
from pytube import YouTube
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


a = os.listdir(os.path.join(BASE_DIR,'media'))
print(a)