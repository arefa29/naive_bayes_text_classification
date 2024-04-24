import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')

class TextPreprocessor:
    def preprocess_text(self, text):
        text = self.remove_punctuations(text)
        text = self.remove_extra_spaces(text)
        text = self.remove_numbers(text)
        text = self.lower_case(text)
        return text

    def remove_punctuations(self, text):
        result = re.sub(r'[\!\(\)\-\[\]\{\}\;\:\'\"\\\,\<\>\.\?\@\#\$\%\^\&\*\_\~]', '', text)
        return result

    def remove_space(self, text):
        result = re.sub('\s+', '', text)
        print(result)
        print('\n')
        return result

    def remove_extra_spaces(self, text):
        result = re.sub('\s+', ' ', text)
        return result

    def tokenize_words(self, text):
        wrds = word_tokenize(text)
        # print(wrds)
        return wrds

    def remove_stopwords(self, text):
        total_count = len(text)
        stop_words = set(stopwords.words("english"))
        result = [w for w in text if w not in stop_words]
        new_count = len(result)
        # print(f'Removed {total_count - new_count} words out of {total_count} words.')
        return result

    def sentence_tokenize(self, text):
        return nltk.sent_tokenize(text)
    
    def remove_numbers(self, text): 
        result = re.sub(r'\d+', '', text) 
        return result
    
    def lower_case(self, text):
        return text.lower()
    
    def remove_square_braces(self, text):
        result = re.sub(r'[\[\]]', '', text)
        return result