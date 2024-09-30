#
# Helper script to properly merge two one-sided scans of a PDF,
# where the odd-numbered pages are scanned in order but the
# even-numbered pages are scanned in reverse order.
# 
# Requires PyPDF2 ('pip install PyPDF2')
#
# Input PDFs should be named the same thing, with _odd and _even as
# suffixes to the filename (e.g., doc_odd.pdf and doc_even.pdf).
# Pass the base filename into the script,
# WITHOUT the .pdf extension (e.g., 'python scanmerge.py doc').
#

import itertools as itt
import sys

import PyPDF2 as PDF


def main():
    for i in range(30):
        mergePdf(i+1)

    return 0

def mergePdf(i):
    fbase = str(i)

    pdf_out = PDF.PdfFileWriter()


    try:
        with open(fbase + " 正.pdf", 'rb') as f_odd:
            with open(fbase + " 反.pdf", 'rb')  as f_even:
                pdf_odd = PDF.PdfFileReader(f_odd)
                pdf_even = PDF.PdfFileReader(f_even)

                for p in itt.chain.from_iterable(
                    itt.zip_longest(
                        pdf_odd.pages,
                        reversed(pdf_even.pages),
                    )
                ):
                    if p:
                        pdf_out.addPage(p)

                with open(fbase + ".pdf", 'wb') as f_out:
                    pdf_out.write(f_out)
    except:
        print("error.")

    return 0  


if __name__ == "__main__":
    sys.exit(main())