

def filter_movies(name_movie):
    print(f'Initial process data with name search: {name_movie}')
    import pandas as pd

    titles = pd.read_csv('titles.tsv', sep='\t', dtype='unicode')
    rating = pd.read_csv('rating.tsv', sep='\t', dtype='unicode')

    df_title = pd.DataFrame(titles)
    df_title.drop(
        columns=[
            'titleType','primaryTitle','isAdult',
            'startYear', 'endYear', 'runtimeMinutes', 'genres'],
        inplace=True
    )
    movies_selected = df_title.loc[df_title['originalTitle'] == name_movie]
    df_rating = pd.DataFrame(rating)
    result = pd.merge(movies_selected, df_rating, on='tconst')

    return result.sort_values(by='averageRating', ascending=False)

def download():
    print('Initial download files IMDB')
    import requests
    try:
        rating = requests.get('https://datasets.imdbws.com/title.ratings.tsv.gz')
        open('rating.gz', 'wb').write(rating.content)
        titles = requests.get('https://datasets.imdbws.com/title.basics.tsv.gz')
        open('titles.gz', 'wb').write(titles.content)
    except Exception as e:
        raise str(e)
    print('Download Completed')
    return 'Ok'

def ungz():
    print('Initial ungz files.')
    import gzip
    import shutil
    try:
        with gzip.open('rating.gz', 'rb') as f_in:
            with open('rating.tsv', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        with gzip.open('titles.gz', 'rb') as f_in:
            with open('titles.tsv', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
    except Exception as e:
        raise str(e)
    print('Completed ungz files.')
    return 'Ok'


if __name__ == "__main__":
    import os
    # Verify if exist files gz.
    if not os.path.isfile('rating.gz') == True or not os.path.isfile('titles.gz') == True:
        download()
    else:
        pass
    
    if not os.path.isfile('rating.tsv') == True or not os.path.isfile('titles.tsv') == True:
        ungz()
    else:
        pass
    # Execute query with name movie.
    print(
        filter_movies(
            name_movie='John'
        )
    )