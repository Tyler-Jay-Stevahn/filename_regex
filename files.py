import os
import pandas as pd

# print(str(i/len(data))[:4], '%',"finished")
df = pd.DataFrame(columns=["Filename"])

for root, dirs, files in os.walk("C:\\Users\\tstevahn\\Phone\\Vault\\Obsidian Vault"):
    for filename in files:
        if filename.endswith(".md"): 
            df = df.append({"Filename": filename}, ignore_index=True)
            #print("'", filename, "'")

print("finished making list, starting search for duplicates.")

df.to_csv('files.csv')
df.to_csv('files2.csv')
print('saved to csv files')
data = df
data2 = df

data_combined = pd.DataFrame(columns=["Phrase1", "Phrase2"])
print('starting search for subsets')

for i in range(len(data)):
    filename = data.iloc[i]["Filename"]
    # print(filename)
    for j in range(len(data2)):
        filename2 = data.iloc[j]["Filename"]
        filname2 = " " + filename2 + " "
        if filename2 in filename and filename != filename2: # and not str(filename).endswith(filename2)
            # print(filename2, "is in", filename)
            phrase1 = filename
            phrase2 = filename2
            data_combined = data_combined.append({"Phrase1": phrase2, "Phrase2": phrase1}, ignore_index=True)

    print(filename, "finished")
data_combined.to_csv("combined.csv")
data_check = data_combined["Phrase1"]
data_check.drop_duplicates()

print("finished combined search for subsets")
data_fin = pd.DataFrame(columns=["phrase", "subset", "phrase2"])

for i in range(len(data)):
    filename = data.iloc[i]["Filename"]
    # print(filename)
    for j in range(len(data_check)):
        # print(data_check.head(), data_check.shape)
        filename2 = data_check.iloc[j]
        phrase = filename2[:-3]
        subset = "no"
        if filename2 in filename and filename2 != filename:
            subset = "yes"
            print(phrase, "is in", filename)
        data_fin = data_fin.append({"phrase": phrase, "subset": subset}, ignore_index=True)
# print(str("(?<!Warren )\bbridge(?! Truss)"))
print("finished setting up subsets in new dataframe")
data_fin.to_csv("data_fin.csv")