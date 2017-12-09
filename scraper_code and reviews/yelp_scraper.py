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


# Find and return the link from a html tag
def getLink(link):
    source = link.get('href')
    if '/biz' in source:
        source = "https://www.yelp.com" + source
        source = source.split('?osq=')[0].strip()
        print (source)
    else:
        source = 'NA'
    return source


# Find all <a> tags that contain links of Japanese restaurants and output the links into the file.
def run_japan(url):

    pageNum=10

    fw=open('japanese.txt','w') 
	
    for p in range(0,pageNum+1): 

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
                time.sleep(0.1) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 

        links=soup.findAll('a', {'class':re.compile('biz-name js-analytics-click')})
        print("reading data...\n")
        for link in links:


            source = getLink(link)
            
            if source == 'NA':
                continue
            
            fw.write(source + "\n" ) 
		
            time.sleep(0.1)	

    fw.close()
    
    
# Find all <a> tags that contain links of Indian restaurants and output the links into the file.
def run_indian(url):

    pageNum=10

    fw=open('indian.txt','w') 
	
    for p in range(0,pageNum+1): 

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
                time.sleep(0.1) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 


        links=soup.findAll('a', {'class':re.compile('biz-name js-analytics-click')})
        print("reading data...\n")
        for link in links:


            source = getLink(link)
            
            if source == 'NA':
                continue
            fw.write(source + "\n" ) 
		
            time.sleep(0.1)	

    fw.close()
    
    
# Find all <a> tags that contain links of American restaurants and output the links into the file.
def run_usa(url):

    pageNum=10

    fw=open('american.txt','w') 
    
	
    for p in range(0,pageNum+1): 

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
                time.sleep(0.1) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 


        links=soup.findAll('a', {'class':re.compile('biz-name js-analytics-click')})
        print("reading data...\n")
        for link in links:

            source = getLink(link)
            
            if source == 'NA':
                continue
            fw.write(source + "\n" ) 
		
            time.sleep(0.1)	

    fw.close()
    

# Find and get the review and rating of the given tag and return them
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


# Find all <div> tags that contain reviews of Japanese restaurants and output the review into the file.
def jp_get_tags(url,PROCESS):
    pageNum=10

    fw=open('jp_review.txt','a+') 
    
	
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
                time.sleep(0.1) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 


        tags=soup.findAll('div', {'itemprop': "review"})
        print("reading data...\n")
        for tag in tags:

            rating, review = get_review_rating(tag)
            
            if review == 'NA':
                continue
            
            fw.write(rating + "\n" + review + "\n" + pageLink + "\n\n" )
            PROCESS = PROCESS + 1
            print(PROCESS)
        
            time.sleep(0.1)	

    fw.close()
    return (PROCESS)


# Find all <div> tags that contain reviews of Japanese restaurants and output the review into the file.
def in_get_tags(url, PROCESS):
    
    pageNum=10

    fw=open('in_review.txt','a+') 
    
	
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
                time.sleep(0.1) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 


        tags=soup.findAll('div', {'itemprop': "review"})
        print("reading data...\n")
        for tag in tags:

            rating, review = get_review_rating(tag)
            
            if review == 'NA':
                continue
            
            fw.write(rating + "\n" + review + "\n" + pageLink + "\n\n" )
            
            PROCESS = PROCESS + 1
            print(PROCESS)
		
            time.sleep(0.1)	

    fw.close()
    return (PROCESS)
    

# Find all <div> tags that contain reviews of Japanese restaurants and output the review into the file.
def usa_get_tags(url,PROCESS):
    pageNum=10

    fw=open('usa_review.txt','a+') 
    
	
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
                time.sleep(0.1) 
				
		
        if not html:continue 
        
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') 


        tags=soup.findAll('div', {'itemprop': "review"})
        print("reading data...\n")
        for tag in tags:

            rating, review = get_review_rating(tag)
            
            if review == 'NA':
                continue
            
            fw.write(rating + "\n" + review + "\n" + pageLink + "\n\n" )
            PROCESS = PROCESS + 1
            print(PROCESS)
            time.sleep(0.1)	

    fw.close()
    return (PROCESS)
    
    
# Get the link from the given file and return a list of links
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
    # Get Japanese restaurants links
    jp_url='https://www.yelp.com/search?find_desc=japanese+restaurant&find_loc=Chicago&start='
    run_japan(jp_url)
    # Get Indian restaurants links
    in_url='https://www.yelp.com/search?find_desc=Indian+restaurant&find_loc=Chicago&start='
    run_indian(in_url)
    # Get American restaurants links    
    usa_url='https://www.yelp.com/search?find_desc=American+restaurant&find_loc=Chicago&start='
    run_usa(usa_url)
    
    # Getting reviews of each restaurant 
    PROCESS1=0
    # collect all the Japanese Restaurants links from the file 
    jp_linklst = get_link_list("japanese.txt")
    for link in jp_linklst:
        PROCESS1 = jp_get_tags(link, PROCESS1)


    PROCESS2=0
    # collect all the Indian Restaurants links from the file 
    in_linklst = get_link_list("indian.txt")
    for link in in_linklst:
        PROCESS2 = in_get_tags(link,PROCESS2)
        
    
    PROCESS3=0
    # collect all the American Restaurants links from the file 
    usa_linklst = get_link_list("american.txt")
    for link in usa_linklst:
        PROCESS3 = usa_get_tags(link,PROCESS3)
    
    # Print the reviews that each function has collected
    print (PROCESS1)
    print (PROCESS2)
    print (PROCESS3)
    

    
    
    







