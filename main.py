import asyncio

def filter_movies(name_movie):
    print(f'Initial process data with name search: {name_movie}')
    import pandas as pd

    titles = pd.read_csv('titles.tsv', sep='\t', dtype='unicode')
    rating = pd.read_csv('rating.tsv', sep='\t', dtype='unicode')

    df_title = pd.DataFrame(titles)
    df_title.drop(
        columns=[
            'titleType','isAdult',
            'startYear', 'endYear', 'runtimeMinutes', 'genres'],
        inplace=True
    )

    movies_selected = df_title[df_title['primaryTitle'].str.contains('(?i)'+name_movie, na=False)]
    df_rating = pd.DataFrame(rating)
    result = pd.merge(movies_selected, df_rating, on='tconst')

    return result.sort_values(by='averageRating', ascending=False)

async def download():
    print('Initial download files IMDB')
    import requests
    
    loop = asyncio.get_event_loop()

    try:
        print('Download rating file')
        ft_rating = loop.run_in_executor(None, requests.get, 'https://datasets.imdbws.com/title.ratings.tsv.gz')
        print('Download title file')
        ft_titles = loop.run_in_executor(None, requests.get, 'https://datasets.imdbws.com/title.basics.tsv.gz')

        resp_rating = await ft_rating
        resp_titles = await ft_titles
        print('Downloads completed!')

        open('rating.gz', 'wb').write(resp_rating.content)
        open('titles.gz', 'wb').write(resp_titles.content)
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
        loop = asyncio.get_event_loop()
        loop.run_until_complete(download())
    else:
        pass
    
    if not os.path.isfile('rating.tsv') == True or not os.path.isfile('titles.tsv') == True:
        ungz()
    else:
        pass
    # Execute query with name movie.
    print(
        filter_movies(
            name_movie='avengers'
        )
    )