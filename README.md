# twitter-project
This project is designed by me, and satisfies my independent study requirement through Central Michigan University.
A brief explanation:
  This project's overall goal is to collect a large number of posts and their data from twitter, then run analytical queries on that data to find meaningful information about the "twittersphere".

  main.py - this file, as the name suggests, contains the main functionality of the project. It first authenticates to twitter using my developer credentials, and connects to a local SQLite database, 'twitter.db'. It then checks to see if the desired database tables exist - if they don't, it creates them. Next, tweets are collected and inserted into the database. For each tweet, the user, hashtags, and mentions are additionally inserted. The tweets are chosen from my home timeline, as well as from a handful of searches across a broad range of topics.

  twitter_authentication - this file contains my developer credentials, as well as functionality to actually authenticate to twitter's API.

  database_functionality - this file contains methods that connect to twitter.db, create tables for tweets/users/mentions/, insert data, and run analytical queries

  reference folder - this folder contains old code I didn't end up using, as well as some files containing info on how tweepy organizes tweet and user information.
