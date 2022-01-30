#	Read It to Me
#
#	Author: Brandon Hines
#
#   Date: January 30, 2022

import os
import pdftotext
from gtts import gTTS
from funcs import *

# pdftotext OS Dependencies: https://pypi.org/project/pdftotext/

pdfPath = input('Enter the file path of the PDF you would like to convert.\n')

mp3Name = input('What would you like to name your exported audio file as? The file extension (.mp3) will be added autmatically.\n')

pdf2txt(pdfPath)
txt2audio(mp3Name)
