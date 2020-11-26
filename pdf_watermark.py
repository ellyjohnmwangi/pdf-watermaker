import PyPDF2

# open pdf file to be watermarked
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# open pdf containing th watermark
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# iterate through the document pages
for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked.pdf', 'wb') as file :
        output.write(file)
