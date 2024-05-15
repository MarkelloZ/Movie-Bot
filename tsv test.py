import csv
import numpy as np

genres = ["Action", "Adult", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "Film-Noir", "Game-Show", "History", "Horror", "Musical", "Music", "Mystery", "News", "Reality-TV", "Romance", "Sci-Fi", "Short", "Sport", "Talk-Show", "Thriller", "War", "Western"]

ratings = []

with open("title.ratings.tsv", 'r', newline='', encoding='utf-8') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row1 in reader:
       ratings.append(row1)
       

basics = []
 
with open("title.basics.tsv", 'r', newline='', encoding='utf-8') as tsvfile:
   reader = csv.reader(tsvfile, delimiter='\t')
   for row2 in reader:
      basics.append(row2)
   

rule = input("Short By:\n1)Genre\n2)Release Date")
if rule in genres:
   for row2 in basics:
      for row1 in ratings:
         if row2[0] == row1[0] and row2[8] == rule :
            #movie_id=t_const,title,date,genres,rsting,votes
            print(row2[0],row2[3],row2[5],row2[8],row1[1],row1[2])