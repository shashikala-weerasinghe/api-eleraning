import random
import traceback
import string


import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer


def generate_binary_questions(file_content=''):


    main_file = file_content.replace('\n', '')  # make lines in one page
    main_file = main_file.strip()  # Remove Spaces from start and end
    file1 = sent_tokenize(main_file)
    # print(file_content)


    questions_list = []

    for sentence in file1:
        try:
            x = random.randint(1, 100)

            if (x % 2) == 1:
                positive_phrase = clean_sentence(sentence)
                q_yes = {'question': positive_phrase, 'answer': "YES"}
                questions_list.append(q_yes)
            else:
                processed_sentence = clean_sentence(sentence)
                negative_phrase = negative_sentence(processed_sentence)

                q_no = {"question": negative_phrase, "answer": "NO"}
                questions_list.append(q_no)
        except Exception:
            traceback.print_exc()
            break

    # print(json.dumps(questions_list));
    return questions_list


def negative_sentence(single_line):
    tokenize = nltk.word_tokenize(single_line)
    tagged = nltk.pos_tag(tokenize)


    for i, a in enumerate(tagged):
        if a[1] == 'VBZ' or a[1] == 'VBP' or a[1] == 'VBN' or a[1] == 'VB' or a[1] == 'VB ' or a[1] == 'VBD ' or a[
            1] == 'VBG ' or a[1] == 'VBN ' or a[1] == 'VBP ' or a[1] == 'VBZ ' or a[1] == 'MD':
            negative_form = ('not', 'ZZ')
            tagged.insert(i + 1, negative_form)


    word_list = [word for (word, tag) in tagged]
    my_list = list(dict.fromkeys(word_list))
    complete_sentence = TreebankWordDetokenizer().detokenize(my_list)
    return complete_sentence


def get_questions(file_content):
    return generate_binary_questions(file_content)


def clean_sentence(single_line):
    # eliminate punctuation from sentence
    cleaned_sentence = single_line.translate(str.maketrans('', '', string.punctuation))

    tokenize = nltk.word_tokenize(cleaned_sentence)
    tagged = nltk.pos_tag(tokenize)

    for i, s in enumerate(tagged):
        if i == 0 and (s[1] == 'IN' or s[1] == 'RB' or s[1] == 'CC'):
            del tagged[0]

    word_list = [word for (word, tag) in tagged]
    complete_sentence = TreebankWordDetokenizer().detokenize(word_list)




    return complete_sentence
