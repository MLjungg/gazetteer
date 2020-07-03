from sklearn.neighbors import NearestNeighbors
import numpy

path_to_embed_file = "/Users/mikael/Documents/Programmeringsprojekt/coreNLP-Swedish/Dependency-Parser/embed/cleaned_model_embed.txt"
embed_file = open(path_to_embed_file, encoding="UTF-8")


cathegories = {
"religion": ["kristen", "muslim", "jude", "buddhist", "gud", "jesus", "kyrka", "bibel", "koran"],
"health": ["sjuk", "cancer", "sjukskriven", "illamående", "förkyld", "huvudvärk", "utmattad", "eksem", "leukemi", "hjärnskada", "allergi", "astma"],
"politics": ["politik", "diktatur", "demokrati", "liberal", "moderat", "vänsterpartiet", "inrikespolitik", "ideologi", "feminism"],
"sexual_orientation": ["homosexuell", "bisexuell", "heterosexuell", "transsexuell", "gay", "lesbisk", "bög", "pedofil", "prostituerad"],
"ethnicity": ["svensk", "afrikan", "utomeuropeisk"],
}


word_to_vec = {}
vec_to_word = {}
word_list = []
written_words = []
similarity_threshold = 0.77  # 1 is completely similar

iter = -1
neightbours = NearestNeighbors(n_neighbors=5, metric="cosine")
for line in embed_file:
    iter += 1
    word = line.split(" ")[0]
    embedding = line.split(" ")[1:-1]
    word_list.append(numpy.asarray(embedding).astype(numpy.float))
    word_to_vec[word] = numpy.asarray(embedding).astype(numpy.float)
    vec_to_word[str(word_to_vec[word])] = word


    if (iter % 50000 == 0):
        print("Finished processing: " + str(round((iter/3010197), 2)*100) + "% of the words!")

neightbours = NearestNeighbors(n_neighbors=5, metric="cosine")
neightbours.fit(word_list)

for cathegory in cathegories:
    synonyms_file = open("./data/synonyms_" + cathegory + ".txt", "w")
    synonyms_file.write("Looking for synonyms to:" + str(cathegories[cathegory]))
    for word in cathegories[cathegory]:
        vec = neightbours.kneighbors([word_to_vec[word]], 1000)
        for index, cosine_similarity in zip(vec[1][0], vec[0][0]):
            if (1-cosine_similarity) > similarity_threshold:
                word = vec_to_word[str(word_list[index])]
                if word not in written_words:
                    written_words.append(word)
                    synonyms_file.write("\n" + word)
