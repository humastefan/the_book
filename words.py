from urllib.request import urlopen


story = urlopen('http://www.adevarul.ro')
story_words = []
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)
story.close()

for word in story_words:
    print(word)
