# scrapingtweets
The scrapingtweets projects is used to scrape tweets from twitter with the help of :
* streamlit
   Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps.
   It is a Python-based library specifically designed for machine learning engineers.
   Streamlit is the easiest way especially for people with no front-end knowledge to put their code into a web application:
   No front-end (html, js, css) experience or knowledge is required.
   You don't need to spend days or months to create a web app, you can create a really beautiful machine learning or 
   data science app in only a few hours or even minutes.
* Snscrape
   Snscrape requires at least Python 3.8 or higher. 
   Snscrape is another approach for scraping information from Twitter that does not require the use of an API. 
   Snscrape allows you to scrape basic information such as a user's profile, tweet content, source, and so on.
   Snscrape is not limited to Twitter, but can also scrape content from other prominent social media networks like Facebook, Instagram, and others.
* Mongodb
   MongoDB is a document database used to build highly available and scalable internet applications. 
   With its flexible schema approach, it's popular with development teams using agile methodologies.
   MongoDB is an open-source document database built on a horizontal scale-out architecture that uses a flexible schema for storing data. Founded in 2007, MongoDB has a worldwide following in the developer community.
   Instead of storing data in tables of rows or columns like SQL databases, each record in a MongoDB database is a document described in BSON, 
   a binary representation of the data. Applications can then retrieve this information in a JSON format.
steps involved:
s1 - with scrapping as the main task SNSCRAPE helps in a wide variety to search through the tweets mainly with functions such as TwitterSearchScraper,TwitterUserScraper
     and much more , hence importing the snscrape.modules we can start scraping.(i also attached a basic scrapper code to scrape 10 tweets of the given query)
s2 - importing pymongo paves the way for storing the scrapped data in the specific database as per our convenience and access it in future necessities.
s3 - with streamlit making a working GUI with the above modules will result in the given TWITTER SCRAPPER.
s4 - import all modules as given in requirement(note: streamlit installation also installs pandas and more)
s5 - delete_many,insert_one and find functions of pymongo used to store and download data in and out of mongodb
s6 - one main function is called in for to encompass the whole code in a simple and maintainable manner.
s7 - streamlit commands are used for better access through GUI and for loop to TwitterSearchScraper
s8 - with the streamlit , pymongo , snscrape scrappingtweets project is given. 

     
