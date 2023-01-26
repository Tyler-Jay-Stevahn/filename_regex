import os
import re
import time
import pandas as pd

df = pd.read_csv("files.csv")


lastname = " "
temp_str = " "
searchstring = "arthropod "
search_stringLen = 0-len(searchstring)-2
# search_string = " "+str(searchstring)+" "
newsearchstring = " "+"[["+str(searchstring[:-1])+"]]"+" "
# print(search_stringLen)
print("Started searching")


for i in range(len(df)):
    for root, dirs, files in os.walk("C:\\Users\\Snick\\Documents\\Phone\\Vault\\Obsidian Vault"):
    # Iterate through the pdf_dir and get the path of all pdf files
        for filename in files:
            if filename.endswith(".md"):#  and "Conflict" in filename
                filename = filename.lower()
                # print(filename)
                file = os.path.join(root, filename)

                
                filenamed = df.iloc[i]["Filename"]
                searchstring = " " +filenamed[:-3]+" "
                search_stringLen = 0-len(searchstring)-2
                newsearchstring = " "+"[["+str(searchstring[1:-1])+"]]"+" "
                # print("'", searchstring, "'")
                # print(newsearchstring)
                with open(file, 'r', errors='ignore') as f:
                        # Get the text for the current page
                        text = f.read()
                        if searchstring in text:
                             print(searchstring, "is in", filename)
                        updated_text = re.sub(searchstring, newsearchstring, text)
                # print("Finished reading", filename)
                # Open the file for writing
                with open(file, 'w', errors='ignore') as f:
                    # Write the updated text to the file
                    f.write(updated_text)

                        # print(text)
                        # Speak the text
                        # engine.say(text)
                        # Run the text-to-speech engine
                        # engine.runAndWait()
                
                # print(filename, "is deleted.")
                # file_path = os.path.join(root, filename)
                # os.remove(file_path)
                '''
                filepath = os.path.abspath(os.path.join(root, filename))
                file_name = filename
                filename = re.sub(" ", "_", filename)
                print(file_name, "renamed to", filename)
                os.rename(filepath, os.path.join(root, filename))
                '''
                # time.sleep(1)
print("Finished Program")