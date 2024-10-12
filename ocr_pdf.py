import pytesseract as py
import fitz
from PIL import Image
import openpyxl
import os

# Define the function to perform OCR on a PDF and save it to an Excel file
def pdf_to_excel_with_ocr(pdf_path, excel_path):
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "OCR Results"

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through the pages
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        # Convert PDF page to a pixmap
        pix = page.get_pixmap()
        
        # Convert the pixmap to an image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Perform OCR on the image
        text = pytesseract.image_to_string(img)

        # Write the text to the Excel sheet
        # Split the text by lines and add each line to a new row in the Excel sheet
        for line in text.splitlines():
            if line.strip():  # Avoid empty lines
                sheet.append([line])  # Append the line to the Excel sheet

    # Save the Excel workbook
    workbook.save(excel_path)
    print(f"Excel file saved as: {excel_path}")

# Define the paths
pdf_file_path = "contract pdf/GEMC-511687751808994.pdf"  # Replace with your PDF file path
excel_file_path = "contract_excel/output.xlsx"  # Replace with your desired output Excel file path

# Call the function
pdf_to_excel_with_ocr(pdf_file_path, excel_file_path)
