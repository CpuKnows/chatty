import random
import re

class Bot(object):
    def __init__(self):
        pass
    #def __init__(self, text):
        #tokens = nltk.word_tokenize(text)
        #print "tokenized"
        #self._model = nltk.model.ngram.NgramModel(3, tokens)
        #print "modelized"

    def respond_to(self, message):
        return 'echo:' + message

    def _format_response(self, content):
        def to_unicode(x):
            if isinstance(x, str):
                return x.decode('utf-8')
            return x

        s = u' '.join([to_unicode(c) for c in content])
        s = re.sub(r' ([\?,\.:!])', r'\1', s)  # Remove spaces before separators
        return s