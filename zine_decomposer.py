import sys
import copy
from PyPDF2 import PdfReader, PdfWriter

def split_half(page, left=True):
    llx, lly = float(page.mediabox.lower_left[0]), float(page.mediabox.lower_left[1])
    urx, ury = float(page.mediabox.upper_right[0]), float(page.mediabox.upper_right[1])
    midy = lly + (ury - lly) / 2
    midx = llx + (urx - llx) / 2

    new_page = copy.deepcopy(page)

    if ury > urx:
        if left:
            new_page.mediabox.lower_left = (llx, lly)
            new_page.mediabox.upper_right = (urx, midy)
        else:
            new_page.mediabox.lower_left = (llx, midy)
            new_page.mediabox.upper_right = (urx, ury)

    else:
        if left:
            new_page.mediabox.lower_left = (llx, lly)
            new_page.mediabox.upper_right = (midx, ury)
        else:
            new_page.mediabox.lower_left = (midx, lly)
            new_page.mediabox.upper_right = (urx, ury)
    return new_page

def new_order_index(original_page_count):
    new_order = []
    for i in range(int(original_page_count / 2)):
        if i % 2 == 0:
            new_order.append(i * 2 + 1)
        else:
            new_order.append(i * 2)
    for i in range(int(original_page_count / 2) -1, -1, -1):
        if i % 2 == 0:
            new_order.append(i * 2)
        else:
            new_order.append(i * 2 + 1)
    print(new_order)
    return new_order

def split_pdf(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    pages = []
    for page in reader.pages:
        # rotate page 90 degrees clockwise
        page.rotate(90)
        left_page = split_half(page, left=True)
        right_page = split_half(page, left=False)
        pages.append(left_page)
        pages.append(right_page)

    for page_num in new_order_index(len(pages)):
        writer.add_page(pages[page_num])

    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zine_decomposer.py input.pdf output.pdf")
        sys.exit(1)
    split_pdf(sys.argv[1], sys.argv[2])