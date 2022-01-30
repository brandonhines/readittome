# README #
# Read It to Me #

Read It to Me is a Python 3 script used to convert PDF files to audio files using Google Translate's text-to-speech API.

## Requirements ##
In addition to the module requirements listed in requirements.txt, poppler is required. Installation instructions for multiple platforms can be found on [pdftotext's PyPi page](https://pypi.org/project/pdftotext/) under OS Dependencies.

## Version History ##
### v1.0 - Initial release (2022 January 30) ###
* Convert PDFs to mp3 files

## Known Issues ##
* Large PDF files (70+ pages) can cause the the Google Translate API to reject the connection and conversion will fail
* Password protected PDFs are unsupported
