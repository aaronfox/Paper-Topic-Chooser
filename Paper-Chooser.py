#!python3
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
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

# count = 3
topics_dict = {}
for line in topics_file:
    # if count < 8:
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
        print(regex_result.group(1))
        # Replace commas with 
        num_str = regex_result.group(1)
        num_str = num_str.replace(',', '')
        print(num_str)
        topics_dict[line] = int(num_str)
        # print(search_result_data.text)
    else:
        print(line[:-1] + ' is empty')
        # Don't include empty results
        # topics_dict[line] = 0
    # count = count + 1

for key,val in topics_dict.items():
    print(key[:-1] + ": " + str(val))

keys_tuple = ()
for key in topics_dict.keys():
    # Only use first 10 chars to make the plot more readable and consistent
    if len(key) >= 18:
        key = key[:18] + "..."
    else:
        key = key[:-1]
    keys_tuple = keys_tuple + (key,)

vals_tuple = ()
for val in topics_dict.values():
    vals_tuple = vals_tuple + (val,)

objects = keys_tuple
y_pos = np.arange(len(objects))
performance = vals_tuple

# import matplotlib.pyplot as plt
# import random

# x = range(13)
# y = [random.randrange(100) for _ in range(13)]
# plt.bar(x, y)
# for a,b in zip(x, y):
#     plt.text(a, b, str(a))
# plt.show()
 
plt.bar(y_pos, performance, align='center', alpha=0.8, color='chartreuse')
plt.xticks(y_pos, objects)
plt.xticks(rotation=90)
# Make Room for bottom text
plt.tight_layout()
plt.ylabel('Number of Words', fontname="monospace")
plt.xlabel('Topic', fontname="monospace")

plt.title('Number of Words for Each Topic\'s Wikipedia Article')
plt.show()

print('End of Paper-Chooser.py!')