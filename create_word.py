import win32com.client

# Open MS Word
def create_table(chrx,file_name):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False  # Make Word visible

    # Create a new document
    doc = word.Documents.Add()

    # Add a table (3 rows, 4 columns)
    lenx = int(len(chrx)/10)
    num_rows = lenx+1
    num_cols = 10+1
    table = doc.Tables.Add(doc.Range(0, 0), num_rows, num_cols)
    # Insert initial values
    cx = 0
    rx = 0
    rr = 0
    for row in range(1, num_rows + 1):
        for col in range(1, num_cols + 1):
            if row == 1:
                    if row == 1 and col == 1:
                        table.Cell(row, col).Range.Text = "-"
                    else:
                        table.Cell(row, col).Range.Text = rr
                        rr += 1
            elif col == 1:
                table.Cell(row, col).Range.Text = rx
                rx += 1
            else:
                table.Cell(row, col).Range.Text = str(chrx[cx])
                cx += 1

    doc.SaveAs(f'C:\\Users\\Shino\\Downloads\\tryfastapi\\word\\'+file_name+'.docx')
    doc.Close()
    word.Quit()

import OTPv1 as otv
import os

def forcreate_table_to_word():
    folder_path = './data'  # Replace with your folder path
    extensions = ('.CHR', '.KEY')  # Specify the extensions you want to read
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the file has the correct extension and is a file
        if os.path.isfile(file_path) and file_name.endswith(extensions):
            with open(file_path, 'r') as file:
                content = file.read()
                print(content)
                if file_name.find('.CHR') != -1:
                    x = otv.interface_get_char_table(content.strip())
                    create_table(x,file_name)
                else:
                    x = otv.interface_get_key_table(content.strip())
                    create_table(x,file_name)
        
forcreate_table_to_word()