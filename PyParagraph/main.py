#import modules
import os
import re

#designate data path
filepath = os.path.join('.','paragraph_1.txt')

#initialize variables
sentence = []
lengthcount = {1:0}
wordcount = 0
sentence_count = 0
sentence_length =0
weighted_ave =0
raw_sentence_count = 0

#use the file
with open(filepath, 'r', encoding='utf-8') as textfile:
    for block in textfile:
        paragraph = re.split("(?<=[.\n!?]) +", block)
        sentence_count = len(paragraph) #not reliable
        for sentence_num in range(0,len(paragraph)):
            #print(f" {paragraph[sentence_num]}\t{len(paragraph)}")
			#get rid of all the crap.  There's probably more succinct ways to do this
            paragraph[sentence_num] = paragraph[sentence_num].replace('-',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('; ',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('>',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('<',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace(' (',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace(') ',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace(',',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('–',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('`','')
            paragraph[sentence_num] = paragraph[sentence_num].replace('~',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('& ',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('.',' ')
            paragraph[sentence_num] = paragraph[sentence_num].replace('“','')
            paragraph[sentence_num] = paragraph[sentence_num].replace('”','')
            paragraph[sentence_num] = paragraph[sentence_num].replace('  ',' ')
            sentence = paragraph[sentence_num].split(" ")
            if len(sentence)>1: #don't count 1-word sentences
                sentence_length += len(sentence)
                raw_sentence_count +=1
            
            #print(f"{sentence}, {len(sentence)}")
            for word_num in range(0,len(sentence)):
                #print(f"{len(sentence[word_num])}\t{sentence[word_num]}")
                if len(sentence[word_num])>0: #don't count blank "" words
                    wordcount +=1
                    check = 0
                while check == 0:
                    for i in lengthcount.keys():
                        #print(f"{i}, {lengthcount[i]}")
                        if i == len(sentence[word_num]):
                            lengthcount[i] = int(lengthcount[i])+1
                            check = 1
                        if check == 0:
                            check = 2 #add a new length to dictionary
                if check == 2:
                    lengthcount[len(sentence[word_num])] = 1
                #print(lengthcount, wordcount, sentence_count, sentence_length/sentence_count)
    for i in lengthcount.keys():
        #print(i,lengthcount[i])
        weighted_ave += lengthcount[i]*i
        #print(weighted_ave, weighted_ave/wordcount)
    #print(raw_sentence_count)
	
#print to console, no required file output
print(f"\nParagraph Analysis")
print(f"------------------")
print(f"Word count: {wordcount}")
print(f"Sentence count: {raw_sentence_count}")
print(f"Average Letter count: {weighted_ave/wordcount}")
print(f"Average Sentence Length: {sentence_length/raw_sentence_count}")