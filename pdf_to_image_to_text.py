from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 

# Path of the pdf 
PDF_file = "pdf_name"


''' 
Part #1 : Converting PDF to images 
'''

# Store all the pages of the PDF in a variable 
pages = convert_from_path(PDF_file, 500) 

# Counter to store images of each page of PDF to image 
image_counter = 1

# Iterate through all the pages stored above 
for page in pages: 

	filename = "page_"+str(image_counter)+".jpg"
	
	# Save the image of the page in system 
	page.save(filename, 'JPEG') 

	# Increment the counter to update filename 
	image_counter = image_counter + 1



pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

''' 
Part #2 - Recognizing text from the images using OCR 
'''
	
# Variable to get count of total number of pages 
filelimit = image_counter-1


# Creating a text file to write the output 
outfile = "out_text.txt"

# Open the file in append mode so that 
# All contents of all images are added to the same file 
f = open(outfile, "a") 

# Iterate from 1 to total number of pages 
for i in range(1, filelimit + 1): 

	filename = "page_"+str(i)+".jpg"
		
	# Recognize the text as string in image using pytesserct 
	text = str(((pytesseract.image_to_string(Image.open(filename))))) 

	text = text.replace('-\n', '')	 

	# Finally, write the processed text to the file. 
    
	f.write(str(text.encode("utf-8"))+'\n') 

# Close the file after writing all the text. 
f.close() 



