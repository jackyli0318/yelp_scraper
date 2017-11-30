#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:03:48 2017

@author: jackylee
"""
from bs4 import BeautifulSoup
import re
import time
import requests


def getCritic(review):
    criticChunk = review.find('a',{'href':re.compile('/critic/')})
    if criticChunk and str(criticChunk).strip():
        critic = criticChunk.text
    else:
        critic = 'NA'
    
    critic = str(critic).strip()
    return critic


def getRating(review):
    ratingChunk = review.find('div', {'class':re.compile('review_icon icon')})
    attributes = ratingChunk.attrs
    if attributes and str(attributes).strip():
        results = attributes.get('class')
        try:
            rating = results[3]
        except IndexError:
            rating = 'NA'
    else:
        rating = 'NA'
    
    rating = str(rating).strip()
    return rating


def getSource(review):
    sourceChunk = review.find('a',{'href':re.compile('/source-')})
    if sourceChunk and str(sourceChunk).strip():
        source = sourceChunk.text
    else:
        source = 'NA'
    
    source = str(source).strip()
    return source
        


def getDate(review):
    dateChunk = review.find('div',{'class':'review_date subtle small'})
    if dateChunk and str(dateChunk).strip(): 
        date = dateChunk.text
    else:
        date = 'NA'
    
    date = str(date).strip()
    return date


def getTextLen(review):
    content = review.find('div',{'class':'the_review'})
    if content and str(content).strip(): 
        length = len(content.text)
    else:
        length = 'NA'
    
    length = str(length).strip()
    return length


def getLink(link):
    source = link.get('href')
    if '/biz' in source:
        source = "https://www.yelp.com" + source
        source = source.split('?osq=')[0].strip()
        print (source)
    else:
        source = 'NA'
    return source


def run_japan(url):

    pageNum=10

    fw=open('japanese.txt','w') 
#    fw.write("Link\t\tRating\t\tSource\t\tDate\t\tTextLen\n")
	
    for p in range(0,pageNum): 

        print ('page',p)
        html=None

        
        pageLink=url+str(p*10) 
		
        for i in range(5):
            try:
                
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content 
                break 
            except Exception as e:
                print ('failed attempt',i)
                time.sleep(2) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 

#        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) 
        links=soup.findAll('a', {'class':re.compile('biz-name js-analytics-click')})
        print("reading data...\n")
        for link in links:

#            critic = getCritic(review)
#            rating = getRating(review)
#            source = getSource(review)
#            date = getDate(review)
#            length = getTextLen(review)
            
#            print(critic)
#            print(rating)
#            print(source)
#            print(date)
#            print(length + '\n')
            
#            fw.write(critic + "\t" + rating + "\t" + source + "\t" + date + "\t" + length + "\n" )
#            print (link)
            source = getLink(link)
#            print (source)
            if source == 'NA':
                continue
#            source = source.split('?osq=japanese+restaurant')[0].strip()
            fw.write(source + "\n" ) 
		
            time.sleep(2)	

    fw.close()
    
def run_indian(url):

    pageNum=10

    fw=open('indian.txt','w') 
#    fw.write("Link\t\tRating\t\tSource\t\tDate\t\tTextLen\n")
	
    for p in range(0,pageNum): 

        print ('page',p)
        html=None

        
        pageLink=url+str(p*10) 
		
        for i in range(5):
            try:
                
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content 
                break 
            except Exception as e:
                print ('failed attempt',i)
                time.sleep(2) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 

#        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) 
        links=soup.findAll('a', {'class':re.compile('biz-name js-analytics-click')})
        print("reading data...\n")
        for link in links:

#            critic = getCritic(review)
#            rating = getRating(review)
#            source = getSource(review)
#            date = getDate(review)
#            length = getTextLen(review)
            
#            print(critic)
#            print(rating)
#            print(source)
#            print(date)
#            print(length + '\n')
            
#            fw.write(critic + "\t" + rating + "\t" + source + "\t" + date + "\t" + length + "\n" )
#            print (link)
            source = getLink(link)
#            print (source)
            if source == 'NA':
                continue
            fw.write(source + "\n" ) 
		
            time.sleep(2)	

    fw.close()
    
def run_usa(url):

    pageNum=10

    fw=open('american.txt','w') 
#    fw.write("Link\t\tRating\t\tSource\t\tDate\t\tTextLen\n")
	
    for p in range(0,pageNum): 

        print ('page',p)
        html=None

        
        pageLink=url+str(p*10) 
		
        for i in range(5):
            try:
                
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content 
                break 
            except Exception as e:
                print ('failed attempt',i)
                time.sleep(2) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 

#        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) 
        links=soup.findAll('a', {'class':re.compile('biz-name js-analytics-click')})
        print("reading data...\n")
        for link in links:

#            critic = getCritic(review)
#            rating = getRating(review)
#            source = getSource(review)
#            date = getDate(review)
#            length = getTextLen(review)
            
#            print(critic)
#            print(rating)
#            print(source)
#            print(date)
#            print(length + '\n')
            
#            fw.write(critic + "\t" + rating + "\t" + source + "\t" + date + "\t" + length + "\n" )
#            print (link)
            source = getLink(link)
#            print (source)
            if source == 'NA':
                continue
            fw.write(source + "\n" ) 
		
            time.sleep(2)	

    fw.close()
    

def get_review_rating(tag):
    ratingChunk = tag.find('meta',{'itemprop': "ratingValue"})
    rating = ratingChunk.get('content')
    print (rating)
    
    reviewChunk = tag.find('p',{'itemprop': "description"})
    if reviewChunk and str(reviewChunk).strip():
        review = reviewChunk.text
        print (review)
    else:
        review = 'NA'
    rating = str(rating).strip()
    review = str(review).strip()
    return rating, review


def jp_get_tags(url):
    pageNum=0

    fw=open('jp_review.txt','w') 
    fw.write("Rating\t\tReview\t\tSource\n")
	
    for p in range(0,pageNum+1): 

        print ('page',p)
        html=None

        
        pageLink=url+"?start="+str(p*10) 
		
        for i in range(5):
            try:
                
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content 
                break 
            except Exception as e:
                print ('failed attempt',i)
                time.sleep(2) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 

#        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) 
        tags=soup.findAll('div', {'itemprop': "review"})
        print("reading data...\n")
        for tag in tags:

#            critic = getCritic(review)
#            rating = getRating(review)
#            source = getSource(review)
#            date = getDate(review)
#            length = getTextLen(review)
            
#            print(critic)
#            print(rating)
#            print(source)
#            print(date)
#            print(length + '\n')
            
#            fw.write(critic + "\t" + rating + "\t" + source + "\t" + date + "\t" + length + "\n" )
#            print (link)
            rating, review = get_review_rating(tag)
#            print (source)
            if review == 'NA':
                continue
#            fw.write(rating + "\t\t" + review + "\t\t" + pageLink + "\n" )
            fw.write(rating + "\n" + review + "\n" + pageLink + "\n\n" )
		
            time.sleep(2)	

    fw.close()

def get_link_list(filename):
    f = open(filename, 'r')
    
    linklst = list()
    with f:
        lines = f.readlines()
        for line in lines:
            linklst.append(line.strip())
        f.close()
    return linklst

if __name__=='__main__':
<<<<<<< HEAD
    #Japanese list link
#    jp_url='https://www.yelp.com/search?find_desc=japanese+restaurant&find_loc=Chicago&start='
#    run_japan(jp_url)
#    
#    in_url='https://www.yelp.com/search?find_desc=Indian+restaurant&find_loc=Chicago&start='
#    run_indian(in_url)
#    
#    usa_url='https://www.yelp.com/search?find_desc=American+restaurant&find_loc=Chicago&start='
#    run_usa(usa_url)
    
    jp_linklst = get_link_list("japanese.txt")
#    in_linklst = get_link_list("indian.txt")
#    usa_linklst = get_link_list("american.txt")
    
#    for link in jp_linklst:
#        jp_get_tags(link)
    jp_get_tags(jp_linklst[0])
#    for link in in_linklst:
#        jp_get_tags(link)
#        
#    for link in usa_linklst:
#        jp_get_tags(link)
    
    

=======
#	Japanese list link
    jp_url='https://www.yelp.com/search?find_desc=japanese+restaurant&find_loc=Chicago&start='
    run_japan(jp_url)
# 	Indian list link
    in_url='https://www.yelp.com/search?find_desc=Indian+restaurant&find_loc=Chicago&start='
    run_indian(in_url)
# 	American list link
    usa_url='https://www.yelp.com/search?find_desc=American+restaurant&find_loc=Chicago&start='
    run_usa(usa_url)
>>>>>>> 3563a6939f70d31e64e8307b018ee99faacb2da1
    
    
    







