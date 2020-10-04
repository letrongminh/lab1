import re
import csv
all_char = 0
spaces = 0
punctuation_marks = 0
number_of_sentences = 0
words = 0
try:
    open_file = open("hoc_file_csv.csv","r", encoding="utf-8")
    csv_reader = csv.reader(open_file)
    for line in csv_reader:
        characters = ",".join(line)
        all_char += len(characters)
        spaces += characters.count(" ")
        punctuation_marks += characters.count(".") + characters.count(",") + characters.count("?") + characters.count("(") + characters.count(")") + characters.count(";") + characters.count("-") + characters.count("_") + characters.count(":") + characters.count("/") + characters.count("\'") + characters.count("\"")
        words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", characters))
        number_of_sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", characters))
    print("Total number of characters:", all_char)
    print("Total number of characters without spaces:", all_char - spaces)
    print("Number of characters without punctuation:", all_char - punctuation_marks)
    print("Number of words:", words)
    print("Number of sentences: ", number_of_sentences)
finally:
    open_file.close()
