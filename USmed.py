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

class PatientInfo:
	def __init__(self, age, sex, bmi, children, smoker, region, charges):
		self.age = age
		self.sex = sex
		self.bmi = bmi
		self.children = children
		self.smoker = smoker
		self.region = region
		self.charges = charges

	def analyzeSmokers(self):
		smokes = 0
		nonsmokes = 0
		nonsmokecharge = 0
		smokecharge = 0
		for smoke, charge in zip(self.smoker,self.charges):
			if smoke == "yes":
				smokes += 1
				smokecharge += float(charge)

			else:
				nonsmokes += 1
				nonsmokecharge += float(charge)

		smokersdict = {'smokers': smokes, 'smokers avg insurance': smokecharge/smokes, 'non smokers': nonsmokes, 'non smokers avg insurance': nonsmokecharge/nonsmokes}
		return smokersdict

patient_info = PatientInfo(age, sex, bmi, children, smoker, region, charges)
smokerStats = patient_info.analyzeSmokers()
print(smokerStats)