#Developer: Mustafa Malick
#The goal of this project is to analyze the dataset of US medical insurance costs
import csv

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

def listfiller(file_name,list_name,column_name):
	with open(file_name) as insurance:
		insurance_csv = csv.DictReader(insurance)
		for row in insurance_csv:
			list_name.append(row[column_name])

listfiller('insurance.csv', age, 'age')
listfiller('insurance.csv', sex, 'sex')
listfiller('insurance.csv', bmi, 'bmi')
listfiller('insurance.csv', children, 'children')
listfiller('insurance.csv', smoker, 'smoker')
listfiller('insurance.csv', region, 'region')
listfiller('insurance.csv', charges, 'charges')

