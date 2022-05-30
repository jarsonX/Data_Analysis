#File 'top500' contains names and gross revenues of 500 films.
#Those films need to be sorted based on revenues in descending order.
import csv
#This can be done without csv module but it will be easier that way.

def sort_films(input_file, output_file):
    
    movie_list = []
    
    #read the file
    with open(input_file, 'r') as inp:
        inp_reader = csv.reader(inp, delimiter = '\t')  #to avoid splitting
        #csv.reader reads the file and returns an iterable object
        #then thanks for the loop, each line is converted into a list
        #and appended to the movie_list
        for line in inp_reader:
            movie_list.append((int(line[1]), (line[0])))
        
    #sort the list
    movie_list_sorted = sorted(movie_list, reverse=True)
    
    #Note: key parameter would be a good way to sort, if we wanted a different order
    #movie_list_sorted = sorted(movie_list, key=lambda x: x[1], reverse=True)  
    
    #save the list
    with open(output_file, 'w') as out:
        for movie in movie_list_sorted:
            print(movie[0], '\t', movie[1], file=out)
  
sort_films('...\top500.txt', '...\top500result.txt')
