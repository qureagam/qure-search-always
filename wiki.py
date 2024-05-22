import wikipedia
import random as rd

def wiki(value):
     try:
        wiki_value= value
        answer = wikipedia.summary(wiki_value)
        if (answer ==None):
            pass
        else:
            return answer 
     except Exception as e:
         pass
     

