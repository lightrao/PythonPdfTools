import os
from PyPDF2 import PdfFileMerger
 
source_dir = os.getcwd()
 
merger = PdfFileMerger()
 
for item in sorted(os.listdir(source_dir)):
    if item.endswith('pdf'):
        merger.append(item)
    print(item)

merger.write('Complete.pdf')       
merger.close()
