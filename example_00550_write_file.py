
# read and write file
text="hallo"
myfile="mytext.txt"

with open(myfile, "w") as f: #f=VAR_datei
    f.write(text)
