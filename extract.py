import docx2txt


def get_document():
    my_text = docx2txt.process("C:\\Users\\Acer\\Desktop\\Research_Shash\\software11.docx")
    return (my_text)
    # return (str(my_text).split("\n"))
