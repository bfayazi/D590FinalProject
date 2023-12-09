# D590 Final Project
This is the repository for Group 6's Final Project, a song recommendation system.

Team members:
- Aimee Flynn
- Barza Fayazi-Azad
- Paul Miller


## Project Description 

### Objectives 

Create a music recommendation engine that users provide criteria to, which 
returns a list of songs that match the criteria that the user provided to them. The main problem we are looking to solve is the issue where a user is not being given music recommendations that 100% mean their tastes and preferences. With our recommendation engine, a user should be able to provide a song title, artist, or even genre that they like, and our recommendation engine will return a list of songs that match what they’re looking for given the criteria they provided. 

### Usefulness 

With the rise of Spotify’s renowned recommendation system and curated playlists, users are expecting more curated and personalized content more than ever. The expectation is now on the music companies to be able to use a user’s data and provide a constant stream of recommended content that they feel like they would like based off of their listening history. Having an effective music recommendation engine allows us to meet this rising need in the industry and match the systems already in place at companies such as Spotify and Apple. 

There are numerous datasets out there that contain rich music related data thanks to public Spotify API, which allows anyone to interact with Spotify’s streaming service and retrieve metadata or create their own playlists. The main difference is that our dataset has a much sharper focus on only the most popular songs of all time, which can allow for a more curated view and remove a bunch of the noise that you may find on Spotify, given the abundance of songs that can come from unknown sources. 

The general user base that we are targeting are individuals who want a personalized recommendation experience in regard to their music, which we believe is the large majority of the population. Ideally, the target user has a preference towards more historically popular and recognizable songs since our dataset focuses on only the most popular songs in history. 
 

## Data 
Data will be sourced from an existing Kaggle dataset which contains information on the top 2000 songs. 
Source: https://www.kaggle.com/datasets/iamsumat/spotify-top-2000s-mega-dataset/ 

After extracting from a .zip file, the data is contained in a .csv file containing 1994 records. 

Each row has the following data fields:  
'Index', 'Title', 'Artist', 'Top Genre', 'Year', 'Beats Per Minute (BPM)', 'Energy', 'Danceability', 'Loudness (dB)', 'Liveness', 'Valence', 'Length (Duration)', 'Acousticness', 'Speechiness', 'Popularity' 

Data for this project will consist of only the Title, Artist and Top Genre fields. All other columns contain numeric characteristics for each song which are not relevant. 

Initial exploratory data analysis reveals there are 149 unique genres of music. The data does not contain any null values. 

The three text columns will require some manual cleaning. For example, a few song titles contain extra text such as “2002 Remaster”.  Several records are in foreign languages which might present a challenge for processing. 

We will also consider combining certain categories or renaming them for clarity. 

## Functionalities
We will be using five NLP Functions.  Text Similarity will provide a coefficient of similarity of two texts, comparing vectors of both texts. Name Entity Recognition will find named entities, such as persons, in the text. Topic Extraction will identify implicit subgroups in the training data into input data, which can be classified. Keyword Extraction will check for the presence of more important keywords in the input text. And lastly, Text Summarization will help in working with a large corpus. 

A web interface will provide a simple text box to capture input from a user to pass into the recommendation engine. This could be a song title, artist name or genre. 

After submitting their text, users will then be shown a list of 10 recommendations from the top 2000 Spotify song data. 
