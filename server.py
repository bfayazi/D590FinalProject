from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the dataframe
df = pd.read_csv('data/Spotify-2000manualcleaned.csv')

print(df.head())

# sort by artist name
df.sort_values(by='Title', inplace=True)

# Create dictionary of song information to be displayed to the user
# so they can choose a song
song_data=df.to_dict(orient='records')

# Load similarity matrix which was saved from notebook
# After saving it was moved manually to the data folder
sim_matrix_df = pd.read_csv('data/similarity_df.csv', header=0)

print(sim_matrix_df.head())

# Recommendation Engine Function to output the top 10 most smilar songs to the user inputted title 
def song_rec_engine(song_title, full_data=df, sim_matrix_df=sim_matrix_df):
    
    print(f'Song_title to search for: {song_title}')

    # Get the id of the inputted song title
    # song_index = np.where(full_data['Title'] == song_title)[0][0]

    # Return a dataframe of the matching title, which should have only one row
    # Then use .values to return an array and get first element
    song_index = (full_data[full_data['Title'] == song_title]['Index'].values[0]) - 1

    print(f'song_index: {song_index}')
    
    sim_matrix_df.iloc[song_index]

    # Get all the similarity values to the inputted song title
    similar_songs = sim_matrix_df.iloc[song_index].values
    
    # Get the IDs of the top 10 most similar songs to the inputted song title
    # We skip the first once since it will always be the same song that was inputted
    similar_song_ids = np.argsort(-similar_songs)[1:11]

    print(f'similar_song_ids: {similar_song_ids}')
    
    # Get the names of the top 10 similar songs
    similar_song_names = full_data['Title'][similar_song_ids]
    similar_song_artists = full_data['Artist'][similar_song_ids]
    similar_song_genres = full_data['Top Genre'][similar_song_ids]
    
    # Return the song names 
    return [similar_song_names, similar_song_artists, similar_song_genres]


# Define the home page route
@app.route('/')
def home():
    return render_template('index.html', song_data=song_data)

# Create the result page showing user's recommendations.
@app.route('/result', methods=['POST'])
def result():
    # Retrieve the selected value from the form submission
    selected_song_index = request.form['songs']

    # Get song info that user selected. The index comes in as a string, so convert to an int to find it
    search_song_info_list = [song for song in song_data if song.get('Index') == int(selected_song_index)]

    search_song_info = search_song_info_list[0]

    print (f'Search for: {search_song_info}')

    # Call the model to get recommended songs
    similar_song_names, \
    similar_song_artists, \
    similar_song_genres = song_rec_engine(search_song_info.get('Title'), full_data=df, sim_matrix_df=sim_matrix_df)

    # Render a new page with the selected value
    return render_template('result.html', song_data=song_data, 
                           selected_song_info=search_song_info,
                           similar_song_names=similar_song_names,
                           similar_song_artists=similar_song_artists,
                           similar_song_genres=similar_song_genres,
                           zip=zip)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Define the about page route
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)