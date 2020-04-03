from array import *

def resetCount(listResponses):
    for x in listResponses:
        x.count = 0

class Response:
  def __init__(self, count, response, keywords):
    self.count = count
    self.response = response
    self.keywords = keywords
            

#spelled with a C here because K spelling is pronouced incorrectly.
#spelled Dockertty for pronoucation

sentences = ["Hello! My name is Curious.", "Alexis's phone number is (478) 832-8697.", "Alexis's email is alexis monet dockertty at gmail.com.", "You can contact Alexis at (478) 832-8697 or at alexis monet dockertty at gmail.com.", "Alexis was born on July 13 1999.", "I was born on March 31st 2020, but Alexis was born on July 13 1999.", "My name is Curious. I'm Alexis's chat bot.", "My purpose is to answer questions about Alexis dockertty", "I answer the questions you ask me about Alexis", "While this is a very general answer, you should hire Alexis because she is honest, trustworthy, conscientious, and excited to learn more within the field of Computer Science"]

keywordsList = [["hello", "hi", "what"], ["what", "Alexis's", "phone", "number"], ["what", "Alexis's", "email", "address"], ["contact", "Alexis", "phone", "email"], ["when", "Alexis", "born", "birthday"], ["When", "born", "you", "birthday"], ["what", "your", "name"], ["what", "your", "purpose", "why", "made"], ["what", "do", "you", "do"], ["why", "should", "we", "hire", "Alexis", "give", "job"]]
listResponses = []

i = 0
for x in sentences:
  newObj = Response(0, x, keywordsList[i])
  listResponses.append(newObj)
  i = i + 1