# In the first file there is a table of members. Each month unactive members
# are being removed. At the same time, unactive members are stored in the
# second file. The whole process needs to be automatised.

# Format of both files needs to be preserved. No data should be lost.

directory = r"<<<<<DIRECTORY>>>>>\"

file_members = directory + "members.txt"
file_inactive = directory + "inactive.txt"

def clean_files(file_to_clean, file_to_store):
    file_to_clean = open(file_to_clean, "r+")
    file_to_store = open(file_to_store, "a+")
    
    file_to_clean.read()
    file_to_clean.seek(0)
    
    members = file_to_clean.readlines()
    header = members.pop(0)

    inactive = [member for member in members if ('no' in member)]
    
    file_to_clean.seek(0)
    file_to_clean.write(header)
    
    for member in members:
        if member in inactive:
            file_to_store.write(member)
        else:
            file_to_clean.write(member)
            
    file_to_clean.truncate()
    
    file_to_clean.close()
    file_to_store.close()
  
   
clean_files(file_members, file_inactive)

print("Done")
    