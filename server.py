from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the dataframe
df = pd.read_csv('data/Spotify-2000manualcleaned.csv')

# sort by artist name
df.sort_values(by='Artist', inplace=True)

# Create dictionary of song information to be displayed to the user
# so they can choose a song
song_data=df.to_dict(orient='records')

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html', song_data=song_data)

# Create the result page showing user's recommendations.
@app.route('/result', methods=['POST'])
def result():
    # Retrieve the selected value from the form submission
    selected_song = request.form['songs']

    # Get song info that user selected. The index comes in as a string, so convert to an int to find it
    song_info = [song for song in song_data if song.get('Index') == int(selected_song)]

    print (song_info)

    # Render a new page with the selected value
    return render_template('result.html', song_data=song_data, selected_song_info=song_info)


if __name__ == '__main__':
    app.run(debug=True)