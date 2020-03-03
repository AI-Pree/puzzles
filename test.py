import csv
def delete_record():
  lines = []
  with open('some.csv','r') as csvfile:
    index = 1
    csvreader = csv.reader(csvfile, delimiter = "\n", quotechar = ",") #---> here 
    lines = [x for x in csvreader]
    del lines[index]
  print(lines)#----> check this part ? whats in there
delete_record()