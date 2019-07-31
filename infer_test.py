#python example to infer document vectors from trained doc2vec model
import gensim.models as g
import pandas as pd

def doc2vec(data,model,save_path):

    #load model
    m = g.Doc2Vec.load(model)

    #infer test vectors
    doc2vec = []
    with open(data,encoding='utf-8') as _ :
        for line in _:
            doc2vec.append(m.infer_vector([line]))

    dataframe = pd.DataFrame(doc2vec)
    dataframe.to_csv(save_path,header=False,index=False)

doc2vec('toy_data\\문자메세지.txt','toy_data\\doc2vec_s_200_w_2_pv-dm.bin','toy_data\\doc2vec_s_200_w_2_pv-dm.csv')
#doc2vec('toy_data\\문자메세지.txt','toy_data\\doc2vec_s_300_w_2_pv-dm.bin','toy_data\\doc2vec_s_300_w_2_pv-dm.csv')
