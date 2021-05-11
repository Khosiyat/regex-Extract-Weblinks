                                                                    #Copywrite Warning: Owner of the code is Gulcheera Academy(Khosiyat Sabirova)
                                                        #This code can be used by anyone for free, but the name "Gulcheera Academy" must be acknowledged 
import pandas as pd
import numpy as np
import matplotlib as plt
import re
import warnings
#%matplotlib inline

#You may change the regular expression patterns
example_textData2=["https://www.apple.com","http://www.banana.net", "@this is great post", "#IT @my godfather http://bit.ly/3h63x  he did not deserve this","#culture_art Here is a post of modern art"]

#extract weblinks
def extract_webLink(inputText):
  weblinks=[]

  for word in inputText:
    #You may change the regular expression patterns
    weblink=re.findall(r"https?://[\w+\.]?\w+\.\w", word)
    weblinks.append(weblink)
  return weblinks
  #print (weblinks)

extract_webLink(example_textData2)
