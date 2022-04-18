import models.db_session as db_session
from models.word import Word

session = db_session.db_init()

words_file = open('../simple_words_5.txt', 'r')
for word_text in words_file.readlines():
    word = Word()
    word.text = word_text[0:5]
    word.is_simple = True

    session.add(word)

session.commit()

words_file = open('../words_5.txt', 'r')
for word_text in words_file.readlines():
    word = Word()
    word.text = word_text[0:5]
    word.is_simple = False

    session.add(word)

session.commit()

res = session.query(Word).all()
session.close()

print("We have {} words".format(len(res)))
