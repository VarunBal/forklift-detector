import os

with open("train.txt", "w") as a:
    for path, subdirs, files in os.walk(r'dataset\train_data'):
       for file in files:
           if not file.endswith(".txt"):
               filepath = 'data/fork_lift/' + file
               a.write(str(filepath)+"\n")
