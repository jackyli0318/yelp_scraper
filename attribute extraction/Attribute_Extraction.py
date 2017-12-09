

import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk import load
import os
import re

def get_reviews(fpath):

    f=open(fpath)
    text=f.read().strip()
    f.close()
    sentences=sent_tokenize(text) 
    reviews=[]
    for sentence in sentences:
        if sentence.find("https://www.yelp.com")==-1:
            reviews.append(sentence)
    return reviews

def get_attributes(review,POStags,tagger):
	
    tagged_terms=tagger.tag(review)#do POS tagging on the tokenized sentence

    POSterms={}
    for tag in POStags:POSterms[tag]=set()
    #for each tagged term
    for pair in tagged_terms:
        for tag in POStags: # for each POS tag 
            if pair[1].startswith(tag): POSterms[tag].add(pair[0])    
    return POSterms

def getAdjNoun(terms,nouns,adjectives): # good food
    result=[]
    Twograms = ngrams(terms,2) #compute 5-grams    
    for tg in Twograms:  
        if tg[0] in adjectives and tg[1] in nouns:# and tg[3] in PosNegLex and tg[4].find(c)>-1: # if the 5gram is a an adverb followed by an adjective
            result.append(tg[1])
    return result

def getNounNoun(terms,nouns): #good food menu
    result=[]
    Threegrams = ngrams(terms,3) 
    #for each 5#compute 5-grams    
     #for each 5gram
    for tg in Threegrams:  
        if tg[0] in nouns and tg[1] in nouns:# and tg[3] in PosNegLex and tg[4].find(c)>-1: # if the 5gram is a an adverb followed by an adjective
            result.append(tg[0])
            result.append(tg[1])
    return result

def getAdjNounAnyNoun(terms,nouns,adjectives): #good food and wine
    result=[]
    Fourgrams = ngrams(terms,4) 
    #for each 5#compute 5-grams    
     #for each 5gram
    for tg in Fourgrams:  
        if tg[0] in adjectives and tg[1] in nouns and tg[3] in nouns:# and tg[3] in PosNegLex and tg[4].find(c)>-1: # if the 5gram is a an adverb followed by an adjective
            result.append(tg[1])
            result.append(tg[3])
    return result

def getNounVerbAdj(terms,nouns,adjectives,verbs):# food was good
    result=[]
    Threegrams = ngrams(terms,3) #compute 5-grams    
     #for each 5gram
    for tg in Threegrams:
        if tg[0] in nouns and tg[1] in verbs and tg[2] in adjectives:
            result.append(tg[0])
    return result

def getNounVerbAdvAdj(terms,nouns,adjectives,verbs,adverbs):# food was very good
    result=[]
    Fourgrams = ngrams(terms,4) #compute 5-grams    
     #for each 5gram
    for tg in Fourgrams:  
        if tg[0] in nouns and tg[1] in verbs and tg[2] in adverbs and tg[3] in adjectives: # and tg[3] in PosNegLex and tg[4].find(c)>-1: # if the 5gram is a an adverb followed by an adjective
            result.append(tg[0])
    return result

def getNounAnyNounVerbAdvAdj(terms,nouns,adjectives,verbs,adverbs):# food was very good
    result=[]
    Fourgrams = ngrams(terms,4) #compute 5-grams    
     #for each 5gram
    for tg in Fourgrams:  
        if tg[0] in nouns and tg[1] in verbs and tg[2] in adverbs and tg[3] in adjectives: # and tg[3] in PosNegLex and tg[4].find(c)>-1: # if the 5gram is a an adverb followed by an adjective
            result.append(tg[0])
    return result

def clean(terms,wordstoremove):
    for term in terms:  
        if term in wordstoremove:
           terms.remove(term)
    return terms

def clean_uselesswords(terms):
    for term in terms:
            if term in ['one','super','guy','sooo','everything',	'children','parents','reason',	'part','amount',	'wouldn',	'groups',	'way',	'ways','thing','marriage',	'ones','level','everyone',	'yet',	'told','twice','whatever',	'everthing',	'anything','thing','things','somehow','amazing','monday','wednesday','tuesday','thursday','friday','saturday','sunday']:
                terms.remove(term)
    return terms


def process_sentece(review):
        review=re.sub('[^a-zA-Z\d]',' ',review)#replace chars that are not letters or numbers with a spac
        review=re.sub(' +',' ',review).strip()#remove duplicate spaces
        #tokenize the sentence
        _POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'
        tagger = load(_POS_TAGGER)
        terms = nltk.word_tokenize(review.lower()) #removecase
        POStags=["JJ","JJR","JJS","RB","RP","NN","NNS","NNP","RB","RBR","RBS","VB","VBD","VBG","VBN","VBP","VBZ","CC","DT","TO","UH","WDT"] # POS tags of interest 		
        FinalPostTerms=get_attributes(terms,POStags,tagger)
               

        #Remoeve unnecessary words
        Particles=FinalPostTerms["RP"]
        cleantemrs=clean(terms,Particles)
        ProperNames=FinalPostTerms["NNP"]
        cleantemrs=clean(terms,ProperNames)
        Conjuctions=FinalPostTerms["CC"]
        cleantemrs=clean(terms,Conjuctions)
        Determiners=FinalPostTerms["DT"]
        cleantemrs=clean(cleantemrs,Determiners)
        TOERS=FinalPostTerms["TO"]
        cleantemrs=clean(cleantemrs,TOERS)
        Interjections=FinalPostTerms["UH"]
        cleantemrs=clean(cleantemrs,Interjections)
        WhichDeterminer=FinalPostTerms["WDT"]
        cleantemrs=clean(cleantemrs,WhichDeterminer)
        cleanterms=clean_uselesswords(cleantemrs)
        
        
        #Get all Names
        Nouns=FinalPostTerms["NN"]
    
        #Get all Adjectives
        AdjectivesSimp=FinalPostTerms["JJ"]
   
        #Get all Verbs 
        VerbsBasic=FinalPostTerms["VB"]
        
        #Get all Adverbs
        AdverbsSimp=FinalPostTerms["RB"]

        notanyword=[]
        #get the results for this sentence 
        notanyword+=getAdjNoun(cleanterms,Nouns,AdjectivesSimp)
        notanyword+=getAdjNounAnyNoun(cleanterms,Nouns,AdjectivesSimp)
        notanyword+=getNounNoun(cleanterms,Nouns)
        notanyword+=getNounVerbAdj(cleanterms,Nouns,AdjectivesSimp,VerbsBasic)
        notanyword+=getNounVerbAdvAdj(cleanterms,Nouns,AdjectivesSimp,VerbsBasic,AdverbsSimp)
        notanyword+=getNounAnyNounVerbAdvAdj(cleanterms,Nouns,AdjectivesSimp,VerbsBasic,AdverbsSimp)
        return notanyword


def processfile(fpath):
    reviews=get_reviews(fpath)
      #make a new tagger
    FinalPostTerms=[]
    AttributeDict={}
    Attributes=[]
    for review in reviews:
        Attributes=process_sentece(review)
        if len(Attributes)>0:
            for Attribute in Attributes:
                if Attribute not in FinalPostTerms:
                    FinalPostTerms.append(Attribute)
                    AttributeDict[Attribute]=1
                else:
                    value=AttributeDict.get(Attribute)+1
                    AttributeDict[Attribute]=value
    fpath='\\Users\\v523502\\Documents\\Stevens_Institute\\WebAnalytics\\Project\\reviews\\reviews-in-attributesv2.txt'
    file = open(fpath,"w") 
    for Attribute in  AttributeDict:
        file.write(Attribute)
        file.write(" ")
        file.write(str(AttributeDict[Attribute]))
        file.write('\n')
    file.close()
                  

if __name__=='__main__':
   processfile('\\Users\\v523502\\Documents\\Stevens_Institute\\WebAnalytics\\Project\\reviews\\reviews-in.txt')
    
