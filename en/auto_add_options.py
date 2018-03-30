#!/usr/bin/env python

import spacy
import random
import json 

def getFunc():
    words = ""
    f = open('20k.txt')
    line = f.read() 
    while True:
        if line != "":
            words += line.replace("\n"," ")
            line = f.read()
        else:
            break

    nlp = spacy.load('en_core_web_lg')
    print("module loaded.")
    tokens = nlp(words)

    THRESHOLD = 0.5
    LENGTH = 3

    def family_check(word1,word2):
        if len(word1) < len(word2):
            return word2.find(word1)
        else:
            return word1.find(word2)

    def inner(w):
        queue = [] #[['dog',0.1],['cat',0.2]...]
        if w != "":
            txt = nlp(w)
            for token in tokens:
                score = token.similarity(txt)
                if score >= THRESHOLD and family_check(txt.text.strip().lower(),token.text.strip()) < 0:
                    if len(queue) >= LENGTH:
                        index = 0 # in order to contrast 
                        value = 1.0
                        for i in range(0,len(queue)):
                            if queue[i][1] < value:
                                value = queue[i][1]
                                index = i
                        if value < score:
                            queue[index] = [token.text,score]

                    else:
                        queue.append([token.text,score])
        return [x[0].capitalize() for x in queue] # only return the word.
    return inner 


if __name__ == '__main__':
    getSimilar = getFunc()
    path_in = input("input your file path:")
    # eg.
    # ./todo/toys_and_games.json
    # 
    file_in = open(path_in)

    line = file_in.read()
    content = ""
    # read raw json file
    while True:
        if line != "":
            content += line
            line = file_in.read()
        else:
            break
    
    j = json.loads(content.strip()) # parse json
    print("the number of total elements is %d,please wait..." %( len(j)))
    for index in range(0,len(j)):
       key = j[index]['answers'][0] # get the only one.
       answers = getSimilar(key)
       answer = random.randint(0,len(answers))
       answers.insert(answer,key) 
       j[index]['answer'] = answer
       j[index]['answers'] = answers
       print("index is %d ,key is %s.\r" % (index,key))

    path_out = "./need_review/" + path_in.split("/")[-1]
    file_out = open(path_out,'w+')
    file_out.write(json.dumps(j))

    file_in.close()
    file_out.flush()
    file_out.close()
