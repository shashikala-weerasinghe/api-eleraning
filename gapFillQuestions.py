import re
import string

from nltk.tokenize.treebank import TreebankWordDetokenizer

from extract import *

from nltk.tokenize import sent_tokenize, word_tokenize

# from app.structuredQuestion.pre_processor import gap_fill_clean_sentence
from phraseExtractor import PhraseRanker


def generate_gap_fill_questions(file_content=''):
    main_file = file_content.replace('\n', '')
    main_file = main_file.strip()

    file1 = sent_tokenize(main_file)

    questions_list = []

    for sentence in file1:
        try:
            processed_sentence = gap_fill_clean_sentence(sentence)

            important_phrase = get_important_phrase(processed_sentence)

            question = re.sub(important_phrase, "_______________", processed_sentence, flags=re.IGNORECASE)

            single_question = {"question": question, "answer": important_phrase}
            questions_list.append(single_question)

        except:
            break

    return questions_list


# pre process the sentence
def gap_fill_clean_sentence(single_sentence):
    # eliminate punctuation from sentence
    cleaned_sentence = single_sentence.translate(str.maketrans('', '', string.punctuation))
    word_list = word_tokenize(cleaned_sentence)  # changing variable
    # print(main_word)
    if word_list[0] == 'But' or word_list[0] == 'Also' or word_list[0] == 'So' or word_list[0] == ',':
        word_list[0] = ''

    word_list = [x for x in word_list if x]
    construct_sentence =  TreebankWordDetokenizer().detokenize(word_list)
    return construct_sentence


# identify most important phrase in sentence
def get_important_phrase(single_sentence):

    # Uses stopwords for english from NLTK, and all punctuation characters.
    r = PhraseRanker()

    # To get highest ranked keyword phrases.
    keywords = r.get_ranked_phrases(single_sentence)

    return keywords


def get_questions(file_content):

    return generate_gap_fill_questions(file_content)
