# import csv

# with open("data.csv", "w") as file:
# 	fields = ["Key", "Name", "Episodes"]
# 	writer = csv.DictWriter(file, fieldnames=fields)

# key = 0
# with open("data.csv", "a") as file:
# 	writer = csv.writer(file)
# 	writer.writerow([key+1,"Naruto", "720"])

# with open("data.csv", "r") as file:
# 	reader = csv.reader(file)
# 	for column in reader:
# 		if column!=[]:
# 			print(column[2])
