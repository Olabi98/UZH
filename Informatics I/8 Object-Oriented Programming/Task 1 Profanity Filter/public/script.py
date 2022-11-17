#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords=sorted(keywords, key=len, reverse=True)
        self.__template=template 

    def filter(self, msg):
        msg1=msg.lower()
        key=[]
        for word in self.__keywords:
            key.append(word.lower())
            
        for word in key:
            if word in msg1: 
                count= len(word)//len(self.__template)
                rest= len(word)%len(self.__template)
                msg1=msg1.replace( word, count*self.__template + str(self.__template[:rest]))

        msgtoreturn=""
        for i in range (len(msg1)):
            if msg1[i] in self.__template:
                msgtoreturn+=msg1[i]
            else:
                msgtoreturn+= msg[i]
        
           
        return msgtoreturn
    
# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
