import pandas as pd


def main():
    # Load the dataframe
    df = pd.read_csv('data/Spotify-2000manualcleaned.csv')


    song_data = df.to_dict(orient='records')

    # print(df[df['Index'] == 232][['Title', 'Artist', 'Top Genre']].to_string(index=False))

    print(type(song_data))

    song_index = 974
    song_info = [song for song in song_data if song.get('Index') == song_index]

    # The matching song item is a list of one dictionary assuming the Index column has unique values

    print(f"{song_info[0].get('Title')} by {song_info[0].get('Artist')}")


    # print(df.loc[232, ['Title', 'Artist', 'Top Genre']].to_string(index=False))

    # result = ' '.join(map(str, df.loc[232, ['Title', 'Artist', 'Top Genre']]))
    # print(result)

if __name__ == '__main__':
    main()