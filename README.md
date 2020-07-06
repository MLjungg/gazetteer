# gazetteer

This repository was created to find words belonging to a specific cathegory, creating so called gazeeteers. This can be useful when you want to label data used to train a NER model.

The file "find_synonyms" exploits word embeddings with the algorithm nearest neighbour to find words that have a similar semantic meaning.

To run the code you need to specify/customize the following in the find_synonyms file:
- The variable cathegories: define your cathegory and some words belonging to this cathegory.
- Similarity threshold: how similar a word has to be in order for it to be considered a semantic synonym. It ranges from 0-1 where 1 is completely similar.

You also need to download a word embedding file, this can be found here:
http://vectors.nlpl.eu/repository/#. I used the one based on the algorithm, Word2Vec Continuous Skipgram.
This file contains some syntactical errors. Run the "clean embedding" file to fix this. 

In the data directory you will find my attemp to find words belonging to the GDPR sensitive cathegories: health, poltiics, race, sexual orientation and religion.


The overall run time to find synonyms is about 1 hour.
