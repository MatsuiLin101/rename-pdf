import os

from pdf2image import convert_from_path
from PIL import Image
from pyzbar import pyzbar


def pdf_to_png(folder, file_name):
    path = os.path.join(folder, file_name)
    pages = convert_from_path(path, 800)
    p2p_name = path.replace('.pdf', '.png')
    pages[0].save(p2p_name)
    barcode = scan_barcode(p2p_name)
    if barcode is not None:
        rename_pdf(barcode, folder, file_name)
    return barcode


def rename_pdf(barcode, folder, file_name):
    old = os.path.join(folder, file_name)
    new = os.path.join(folder, barcode)
    os.rename(old, new)


def scan_barcode(file_name):
    image = Image.open(file_name)
    barcodes = pyzbar.decode(image)
    if len(barcodes) > 0:
        barcode = barcodes[0].data.decode("utf-8")
        return f"{barcode}.pdf"
    else:
        return None


def scan_pdf(folder):
    files = os.listdir(folder)
    pdf_list = list()
    for file in files:
        if '.pdf' in file:
            pdf_list.append(file)
    return pdf_list
