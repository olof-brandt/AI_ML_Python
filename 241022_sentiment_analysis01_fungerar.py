


#!pip install transformers datasets

from transformers import pipeline

classifier = pipeline("sentiment-analysis")#, model="nlptown/bert-base-multilingual-uncased-sentiment")


res = classifier("du är dum!!!")

print(res)
