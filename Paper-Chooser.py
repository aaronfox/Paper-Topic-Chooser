#!python3
import requests
from bs4 import BeautifulSoup

# Obtain URLS
url = requests.get("https://en.wikipedia.org/wiki/Petr_Eben")
# use https://en.wikipedia.org/wiki/Special:Search?search=Petr+Eben+1929 for searching
# then use first url
soup = BeautifulSoup(url.content, "lxml")
# print(soup)

# The following was specific for editing my topics paper
# this separates out
text_file = open("./guitar_paper_topics.txt", encoding="utf8")
write_file = open("./edited_guitar_topics.txt", "w", encoding="utf8")
print(text_file)
for line in text_file:
    print(line)
    new_line = line.replace("§", "\n")
    if new_line[0] == ' ' or new_line[0] == '-':
        new_line = new_line[1:]
    if new_line[0] == ' ' or new_line[0] == '-':
        new_line = new_line[1:]
    if new_line[0] == ' ' or new_line[0] == '-':
        new_line = new_line[1:]
    print("new_line == " + new_line)
    write_file.write(new_line)
text_file.close()
write_file.close()

# Eliminate empty lines
read_file = open("edited_guitar_topics.txt", "r", encoding="utf8")
write_file = open("./new_edited_guitar_topics.txt", "w", encoding="utf8")
for line in read_file:
    char_flag = False
    index = 0
    for char in line:
        if char.isalpha():
            char_flag = True
        # Get rid of leading spaces
        if char_flag == False:
            if char == " ":
                line = line[0:index] + line[index + 1:]
        index = index + 1
    if char_flag:
        write_file.write(line)
    if line[0] == " ":
        print("line[0] == \" \" where line == " + line + " and line[0] == \"" + line[0] + "\"")


read_file.close()
write_file.close()




print('hello!')