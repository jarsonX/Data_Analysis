#File 'top500' contains names and gross revenues of 500 films.
#Those films need to be sorted in order from greates gross revenue to least.

import csv

def sort_films(input_file, output_file):
    
    movie_list = []
    
    #read the file
    with open(input_file, 'r') as inp:
        inp_reader = csv.reader(inp, delimiter = '\t')  #to avoid splitting
        
        #fill the movie_list
        for line in inp_reader:
            movie_list.append((line[0], int(line[1])))
        
    #sort the list
    movie_list_sorted = sorted(movie_list, key=lambda x: x[1], reverse=True)
        
    #save the list
    with open(output_file, 'w') as out:
        for movie in movie_list_sorted:
            print(movie[1], '\t', movie[0], file=out)
  
sort_films(r"C:\Users\krzys\Desktop\top500.txt", r"C:\Users\krzys\Desktop\top500result.txt")






