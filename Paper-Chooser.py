#!python3
import requests
from bs4 import BeautifulSoup
import re
import unidecode
# see https://pypi.org/project/Unidecode/

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
# print(text_file)
for line in text_file:
    new_line = line.replace("§", "\n")
    if new_line[0] == ' ' or new_line[0] == '-':
        new_line = new_line[1:]
    if new_line[0] == ' ' or new_line[0] == '-':
        new_line = new_line[1:]
    if new_line[0] == ' ' or new_line[0] == '-':
        new_line = new_line[1:]
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
        # Change special accents to closest ascii representation
        # for ease of searching
        # ref https://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string
        line = unidecode.unidecode(line)
        # Get rid of leading spaces
        if char_flag == False:
            if char == " ":
                line = line[0:index] + line[index + 1:]
        index = index + 1
    if char_flag:
        write_file.write(line)

read_file.close()
write_file.close()

# Now that we have the properly edited guitar topics,
# let's see which topics are the most popular on Wikipedia
# Let's arbitrarily say that topics with the largest
# Wikipedia articles are the ones with the most
# overall information on the web and would
# therefore be the easiest to write papers on

topics_file = open("./new_edited_guitar_topics.txt", "r", encoding="utf8")

count = 0
for line in topics_file:
    if count < 5:
        print(line, end="")
        # Obtain search URL
        search_url = requests.get("https://en.wikipedia.org/w/index.php?search=" + line)
        soup = BeautifulSoup(search_url.content, "lxml")
        search_result_url = soup.find("div", {"class":"mw-search-result-heading"})
        search_result_data = soup.find("div", {"class":"mw-search-result-data"})
        if search_result_url:
            first_link = 'https://en.wikipedia.org' + search_result_url.find('a')['href']
            # print(first_link, end='')
            # Use regex to extract number of words for the entry
            regex = re.compile(r"\((.*) words\)")
            print(search_result_data.text);
            regex_result = regex.search(search_result_data.text)
            print(regex_result.group())
            # print(search_result_data.text)
    count = count + 1


print('End of Paper-Chooser.py!')