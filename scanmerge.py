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
    fbase = sys.argv[1]

    pdf_out = PDF.PdfFileWriter()

    with open(fbase + "_odd.pdf", 'rb') as f_odd:
        with open(fbase + "_even.pdf", 'rb') as f_even:
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

    return 0


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Wrong number of arguments!")
        sys.exit(1)

    sys.exit(main())
