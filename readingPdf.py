import pdfplumber


x0 = 0    # Distance of left side of character from left side of page.
x1 = 0.6  # Distance of right side of character from left side of page.
y0 = 0.55  # Distance of bottom of character from bottom of page.
y1 = 1  # Distance of top of character from bottom of page.


with pdfplumber.open("C:/Users/kalee/OneDrive/Documents/kaleem's/MIR's Resume (1).pdf") as pdf: 
    for i, page in enumerate(pdf.pages):
        width = page.width
        height = page.height

        # Crop pages
        left_bbox = (x0*float(width), y0*float(height), x1*float(width), y1*float(height))
        page_crop = page.crop(bbox=left_bbox)
        left_text = page_crop.extract_text()

        
        if i < 1:  # help you see the first page
            print(left_text)
