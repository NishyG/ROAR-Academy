import os
import PyPDF2
file_handle = open("C:\\Users\\Anish\\Downloads\\Sense-and-Sensibility-by-Jane-Austen.pdf", "rb")
pdf_reader = PyPDF2.PdfReader(file_handle)
page_number = len(pdf_reader.pages)
pdf_object = pdf_reader.pages[0]
page_text_string = pdf_object.extract_text()
page_text_list = page_text_string.split(" ")

frequency_table = dict()

for a in range(page_number):
    pdf_object = pdf_reader.pages[a]
    page_text_string = pdf_object.extract_text()
    page_text_list = page_text_string.split(" ")

    for i in page_text_list:
        if i.isalpha():
            if i in frequency_table:
                frequency_table[i] += 1

            elif i not in frequency_table:
                frequency_table[i] = 1

frequency_table_sorted = sorted(frequency_table.items(), key=lambda x:x[1])

