import gensim
import glob

file_names = glob.glob("search/*.txt")
raw_documents=[]
for file in file_names:
    try:
        with open (file, "r" , encoding = "utf-8") as f: raw_documents.append(f.read())
    except:
        pass
    
clean_text=[]
for text in raw_documents :
    clean_text.append(gensim.utils.simple_preprocess(text))

def search(input):


    dictionary = gensim.corpora.Dictionary(clean_text)

    corpus = [dictionary.doc2bow(text) for text in clean_text]

    tf_idf=gensim.models.TfidfModel(corpus)

    similarity_object = gensim.similarities.Similarity('search/',tf_idf[corpus],num_features=len(dictionary))

    text = raw_documents[1]

    query_doc = gensim.utils.simple_preprocess(input)

    query_doc_bow =  dictionary.doc2bow(query_doc)

    query_doc_tf_idf=tf_idf[query_doc_bow]

    similarty_scores=list(similarity_object[query_doc_tf_idf])

    max_scores=max(similarty_scores)

    
    return ('{:.150}'.format(raw_documents[similarty_scores.index(max_scores)]),"...Show more")

b = search('boy')

print (b)