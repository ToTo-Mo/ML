#python example to train doc2vec model (with or without pre-trained word embeddings)

import os
import gensim.models as g
import logging

#doc2vec parameters
vector_size = 200
window_size = 2
min_count = 1
sampling_threshold = 1e-5
negative_size = 5
train_epoch = 100
dm = 1 #0 = dbow; 1 = pv-dm
worker_count = 1 #number of parallel processes

#pretrained word embeddings
pretrained_emb = "toy_data/pretrained_word_embeddings.txt" #None if use without pretrained embeddings

#input corpus
train_corpus = 'toy_data/문자메세지.txt'


#output model
saved_path = "toy_data/doc2vec_s_200_w_2_pv-dm.bin"


#enable logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#train doc2vec model
docs = g.doc2vec.TaggedLineDocument(train_corpus)
model = g.Doc2Vec(docs, size=vector_size, window=window_size, min_count=min_count, 
                    sample=sampling_threshold, workers=worker_count, hs=0, dm=dm, negative=negative_size, 
                    dbow_words=1, dm_concat=1, pretrained_emb=pretrained_emb, iter=train_epoch)

#save model
model.save(saved_path)