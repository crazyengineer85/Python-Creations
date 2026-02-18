from imdby.imdb import imdb

ia = imdb()
liste = ia.get_movie_list('ls023154907')  # Liste ID'si

for film in liste:
    print(film['title'])