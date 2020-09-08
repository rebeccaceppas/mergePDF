import os
from PyPDF2 import PdfFileMerger

def merge():

    # determining source directory
    location = input('Enter the relative path to the files (inside of Re):\n')
    path = '/Users/rebeccaceppas/Re/' + location + '/'

    # creating merger object
    merger = PdfFileMerger()

    # looping through items in source directory
    for item in os.listdir(path):
        if item.endswith('.pdf'):
            merger.append(path + item)

    title = input('What is the new title?\n')
    merger.write(title)
    merger.close()

merge()