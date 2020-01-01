import json
import difflib
data = json.load(open("data.json"))
#loading the data from Json file
#print(data["rain"])

def translate(word):
    word=word.lower() #converts to lower case the inputted word
    if(word in data.keys()):
        return data[word]
    else:
        sim = difflib.get_close_matches(word,data.keys())
        #get_close_matches will return a list of words which closely matches with the inputted word
        if(sim!=[]):
            print("Did you mean %s? Type yes or no" % sim[0])
            yn = input()
            yn=yn.lower()
            if(yn=="yes" or yn=="y"):
                return data[sim[0]]
            elif(yn=="no" or yn=="n"):
                return "\n"
            else:
                return "Didn't understand your input"
        else:
            return "Word entered not in Dictionry"

while(True):
    word=input("Enter a word or exit1 to exit :")
    if(word=="exit1"):
        print("=================================")
        break;
    else:
        li=translate(word)
        if(isinstance(li,str)):
            print(li)
        else:
            for meaning in li:
                print(meaning,"\n")
        print("=================================")
