#	Read It to Me
#
#	Author: Brandon Hines
#
#   Date: January 30, 2022

import os
import pdftotext
from gtts import gTTS

def pdf2txt(pdfPath):
    """
    Export the text from a PDF file into a plain text file.

    Parameter: pdfPath variable is a PDF file path entered as a string.

    Precondition: PDF file cannot be password protected.

    Returns: Content of PDF file in plain text named tmp.txt.

    """

    # Load .pdf
    with open(pdfPath, "rb") as tmp:
        pdf = pdftotext.PDF(tmp)

    # .pdf > .txt, all text placed in one string
    with open('tmp.txt', 'w') as tmp:
        tmp.write("\n\n".join(pdf))

def txt2audio(mp3Name):
    """
    Convert plain text file to mp3 audio file.

    Paramater: mp3Name variable is the mp3 output name entered as a string.

    Precondition: Existing plain text tmp.txt file, like the one generated
    by pdf2txt() stored in the same folder that the script is run from.

    Returns: 32kb/s 24 kHz mono mp3 file in directory script is run from.

    """
    # Print confirmation that .txt > .mp3 process is starting
    print('Processing ' + mp3Name + '.mp3...')

    # Open .txt file, then read it
    file = open('tmp.txt', 'r')
    txt = file.read()
    file.close()

    # .txt > .mp3
    language = 'en'
    audio = gTTS(text=txt, lang=language, slow=False)
    audio.save(mp3Name + '.mp3')

    # Delete tmp.txt
    os.remove('tmp.txt')

    # Print confirmation
    print(mp3Name + '.mp3 created successfuly.')
