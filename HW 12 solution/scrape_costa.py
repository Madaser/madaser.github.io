import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import pandas as pd


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    
    url='https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)

    soup = bs(response.text, 'html.parser')

    results=soup.find_all('div', class_='image_and_description_container')
    results_image=soup.find_all('img', class_='img-lazy')



    list1=[]
    for i in range(len(results_image)):
        list1.append((str(results_image[i]).split("=")[1][:-7]))
    list1



    results_comment=soup.find_all('div', class_='rollover_description_inner')
    list2=[]
    for i in range(len(results_comment)):
        list2.append(results_comment[i].text.strip())
    list2



    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")

    html = browser.html
    soup2 = bs(html, 'html.parser')


    featureimg = soup2.find('article', class_='carousel_item')

    updateimg=str(featureimg).split("=")[3]
    finalimg=updateimg.split("'")[1]
    featureimgurl="https://www.jpl.nasa.gov"+finalimg
    featureimgurl


    
    browser.visit("https://twitter.com/marswxreport?lang=en")
    html2=browser.html
    soup3=bs(html2,'html.parser')


    tweet=soup3.find('p',class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')


    mw=(str(tweet).split("="))[3].strip()[5:][:-8]
    mw

    doc = mw.split('\n')
    mars_weather = " ".join(doc)
    mars_weather

    tables=pd.read_html("https://space-facts.com/mars/")
    tables

    df=tables[0]

    df1=tables[1]
    df1.columns=['Mars Planet Profile', 'Data']
    df1


    dfinfo=df.to_html()
    df1info=df1.to_html()


    dfinfo

    updatedf=dfinfo.replace('\n', '')
    updatedf

    df.to_html('table1.html')
    df1.to_html('table2.html')

    
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced")
    html3=browser.html
    soup4=bs(html3,'html.parser')

    CEimg=str(soup4.find('div',class_='downloads')).split("=")[4][:-8][1:]
    CE="Cerberus Hemisphere"
    print("we done")
    
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced")
    html4=browser.html
    soup5=bs(html4,'html.parser')
    print("we done")

    VMimg=str(soup5.find('div',class_='downloads')).split("=")[4][:-8][1:]
    VM="Valles Marineris"



    
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced")
    html5=browser.html
    soup6=bs(html5,'html.parser')


    SHimg=str(soup6.find('div',class_='downloads')).split("=")[4][:-8][1:]
    SH="Schiaparelli"
    print("we done")

    
    browser.visit("https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced")
    html6=browser.html
    soup7=bs(html6,'html.parser')

    SM= "Syrtis Major"
    SMimg=str(soup7.find('div',class_='downloads')).split("=")[4][:-8][1:]



    hemisphere_image_urls = [{"title":CE, "img_url":CEimg},
                             {"title":VM, "img_url":VMimg},
                             {"title":SH, "img_url":SHimg},
                             {"title":SM, "img_url":SMimg}]

    wedothis=[list1[0],list2[0],featureimgurl,mars_weather, CE, CEimg, VM, VMimg, SH, SHimg, SM, SMimg]
    wedothis_dict={"key":wedothis}
    print("we done")
    return wedothis_dict