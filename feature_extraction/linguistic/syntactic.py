from nltk.tokenize import word_tokenize as wt
from nltk import pos_tag, RegexpParser
from feature_extraction.linguistic.utils import reshape_vector, reshape_matrix

def phrase_freq(tags, parser, shape):
    phrases = []
    for tagged in tags:
        chunks = parser.parse(tagged)
        for sub in chunks.subtrees(filter=lambda t: t.label() == 'PHRASES'):
            phrases.append(' '.join([i[0] for i in sub]))
    freq = [phrases.count(p) / len(phrases) for p in phrases]
    return reshape_matrix(freq, shape, shape)

def get_syntactic_features(sentences, shape):
    tags = [pos_tag(words) for words in [wt(sent) for sent in sentences]]
    parser = RegexpParser('''
                        PHRASES: {<DT>* <NNP> <NNP>+}
                        ''')
    return phrase_freq(tags, parser, shape)
