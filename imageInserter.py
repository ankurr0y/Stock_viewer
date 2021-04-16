import fitz

image_rectangle=fitz.Rect(450,20,550,120)

img_file='BG.png'

file_handle=fitz.open('test.pdf')
first_page=file_handle[0]

first_page.insertImage(image_rectangle, fileName=img_file)

file_handle.save('test.pdf')
