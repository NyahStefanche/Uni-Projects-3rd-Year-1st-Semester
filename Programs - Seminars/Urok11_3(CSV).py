import csv

try:
	f_csv =  open("students.csv")
	reader = csv.reader(f_csv)
	stud = list(reader)
	f_csv.close()
except FileNotFoundError:
	print("CSV file not exist")
	quit()

print(stud)