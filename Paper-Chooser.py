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
    print("new_line == " + new_line)
    write_file.write(new_line)
text_file.close()
write_file.close()

print('hello!')