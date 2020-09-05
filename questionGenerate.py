import docx2txt

import binary
import gapFillQuestions


my_text = docx2txt.process("C:\\Users\\Acer\\Desktop\\Research_Shash\\software11.docx")
print(my_text)
q_array = gapFillQuestions.get_questions(my_text)

binary_q_array = binary.get_questions(my_text)





print(q_array)
print(binary_q_array)

