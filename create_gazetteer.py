cathegories_NN_JJ = {"health":[], "politics":[]}
cathegories_PM = {"per": [], "loc": [], "org": []}

for cathegory in cathegories_NN_JJ:
    file_cathegory = open("./data/words/" + cathegory + ".txt", "r")
    for line in file_cathegory.readlines()[1:]:
        cathegories_NN_JJ[cathegory].append(line.split()[0])
for cathegory in cathegories_PM:
    file_cathegory = open("./data/words/" + cathegory + ".txt", "r")
    for line in file_cathegory.readlines():
        cathegories_PM[cathegory].append(line.split()[0])

# Creating train file
sentence_has_tag = False
sentence = []
file_gazeteer = open("./data/gazetteers/text.txt", "r")
file_train_gazeteer = open("./data/gazetteers/ner_train_file.txt", "a")

for line in file_gazeteer:
    if line == "\n":
        file_train_gazeteer.write("\n")
        continue

    word, tag = line.split()

    if tag == "NN" or tag == "JJ":
        for cathegory, cathegory_words in cathegories_NN_JJ.items():
            for cathegory_word in cathegory_words:
                if word.upper() == cathegory_word.upper():
                    sentence_has_tag = True
                    tag = cathegory

    if tag == "PM":
        for cathegory, cathegory_word in cathegories_PM.items():
            if word in cathegory_word:
                sentence_has_tag = True
                tag = cathegory
                break

    if tag == "NN" or tag == "JJ" or tag == "PM":
        tag = 0

    sentence.append((word + "\t" + str(tag).upper() + "\n"))

    if word == "." and sentence_has_tag:
        file_train_gazeteer.write("".join(sentence))
        file_train_gazeteer.write("\n")
        sentence_has_tag = False

    if word == "." and not sentence_has_tag:
        sentence.clear()
