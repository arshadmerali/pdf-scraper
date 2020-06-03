import PyPDF2 as p2;

PDFfile = open("restaurantCoalitionToronto.pdf", "rb")
pdfread = p2.PdfFileReader(PDFfile)

q = 3
for q in range (3,20):
    x = pdfread.getPage(q)
    print(x.extractText())
    q += 1
