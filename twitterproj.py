#importing necessary modules to scrape twitter data
import snscrape.modules.twitter as sntwitter
import streamlit as st  
import pandas as pd   
import pymongo 
from pymongo import MongoClient
from datetime import date   
import json
import time

#connecting with mongoclient to store  the scrapped data in database mongodb
connect = MongoClient(host='localhost',port=27017)
tweetdb     =  connect["twitter"]
tweetscol   =  tweetdb["tweets scrapped"]

#providing commands on for to excute on streamlit 
def scrape():
    tweets = 0 
    st.title("TWITTER SCRAPER")

    #presentation in streamlit
    options = st.sidebar.header("OPTIONS")
    choice  = st.sidebar.radio('navigate',["MAIN","BRIEF","SEARCH","ONSCREEN","DOWNLOAD"])

    # main page customization
    if  choice == "MAIN":
        st.markdown("# LETS SCRAPE SOME TWEETS")
        st.markdown("# BASIC INFORMATION")
        st.write("""we will be scrapping data from twitter which is one of the modern warehouse for tons of data using 
        mongodb and snscrape""")
        st.markdown("# ABOUT STREAMLIT")
        st.write("""Streamlit’s open-source app framework is a breeze to get started with. 
                    Data scientists or machine learning engineers are not web developers
                    Instead, they want a tool that is easier to learn and to use, 
                    as long as it can display data and collect needed parameters for modeling. 
                    Streamlit allows you to create a stunning-looking application with only a few lines of code."""
                )
        
    # if the other one is choosen a brief about mongodb and snscrape is provided
    elif choice == "BRIEF":
        BRIEF= st.selectbox("BRIEF",["snscrape","mongodb"])
        if BRIEF== "snscrape":
            st.markdown("# SNSCRAPE")
            st.write("""snscrape is a scraper for social networking services (SNS). 
                        It scrapes things like user profiles, hashtags, or searches and returns the discovered items, 
                        e.g. the relevant posts.
                        snscrape module used mainly for the purpose of scrapping twitter data for inference purposes
                        and main functions in it are TwitterUserSearch(),TwitterSearchScraper() and much more.""")
        elif BRIEF== "mongodb":
            st.markdown("# Mongodb")
            st.write("""MongoDB is a document database with the scalability 
                        and flexibility that you want with the querying and indexing that you need
                        Mongodb is mainly used for storing the scrapped data in databases such that for the purposes of
                        easy access and handling""")

    #search option opens with delete to clear data and with elements to search a hashtag specifically
    elif choice == "SEARCH" :

        tweetscol.delete_many({})

        with st.form(key="Advanced search"):
            #providing with header and key value names
            st.markdown("# ADVANCED SEARCH")
            st.write("enter hashtag or keyword")
            query = st.text_input('like IPL')
            # invoking number_input to intake number 
            st.write("ENTER THE NUMBER OF TWEETS")
            limit = st.number_input("NUMBER",min_value=0,max_value=1000,step=15)
            #as  for dates  start and end date are given
            st.write("ENTER THE DATES TO SCRAPE")
            start = st.date_input('START DATE')
            end   = st.date_input('END DATE')

            submit_button = st.form_submit_button("TWEET SCRAPE")
            #successful submit button would imply that it started the query on given hashtag
        if submit_button :
           st.success (f"scrape {query}".format(query))
          

        #using snscrape function twittersearchscraper querying for the required data with given specifics
        for tweet in sntwitter.TwitterSearchScraper(f'from:{query} since:{start} until:{end}').get_items():
           #given input will be the limit to perform scraping
            if tweets == limit:
               break
            #else the actaual data to scrape would be given in the following format
            else:
              mes = {"DATE":tweet.date,"ID":tweet.id,"URL":tweet.url,"CONTENT":tweet.content,"USER":tweet.user.username,"REPLYCOUNT":tweet.replyCount,"RETWEETS":tweet.retweetCount,"LANG":tweet.lang,"SOURCE":tweet.source,"LIKES":tweet.likeCount}
              tweetscol.insert_one(mes)
              tweets += 1

        #len gives the number of tweets scraped and find() function is used to query through the scrapped tweets
        df = pd.DataFrame(list(tweetscol.find()))
        l  = len(df)
        st.success(f"TOTAL NO OF SCRAPED TWEETS:{l}".format(l))

    # another choice gives the onscreen presentation with same find() function
    elif choice == "ONSCREEN":
        st.subheader("HENCE THE SCRAPPED TWEETS ARE AS FOLLOWS")
        df = pd.DataFrame(list(tweetscol.find()))

        st.dataframe(df)
     #two format downloads are made possible
    else :
      JSON,CSV = st.columns(2)
      #csv download 
      with CSV:
           st.subheader("FOR CSV FILE")
           st.write("DOWNLOAD CSV")

           df=pd.DataFrame(list(tweetscol.find()))
           #convrting to csv and downloading as csv file
           df.to_csv('tweetcsv.csv')
           def convert_df(data):
               
               return df.to_csv().encode('utf-8')
           csv = convert_df(df)
           st.download_button(
                              label="CSV DOWNLOAD",
                              data=csv,
                              file_name='twittercsv.csv',
                              mime='text/csv'
                              )
      with JSON:
          st.subheader("FOR JSON FILE")
          st.write("for JSON ")
           
          tweetjs= df.to_json(default_handler= str).encode()
          #dumping values into json and dowload it as json file
          obj = json.loads(tweetjs)
          js  = json.dumps(obj,indent=5)
          st.download_button(
                              label="JSON DOWNLOAD",
                              data=js,
                              file_name='tweetjs.js',
                              mime='text/js',

              )
          
scrape()

