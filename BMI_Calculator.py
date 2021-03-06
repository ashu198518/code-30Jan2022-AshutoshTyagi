# Library import
import json, csv

# Defined a class for the given categories of BMI & Health risk
class BMI:
    bmi_categoty ={ 'UW' :'Underweight',
                    'NW': 'Normal Weight',
                    'OW': 'Over Weight',
                    'MO': 'Moderately obese',
                    'SO': 'Severly obese',
                    'VSO': 'Very Severly obese',
                   }
    health_risk = {
                    'MR':'Malnutrition Risk',
                    'LR': 'Low Risk',
                    'ER': 'Enhanced Risk',
                    'MRS': 'Medium Risk',
                    'HR': 'High Risk',
                    'VHR': 'Very High Risk',
    }

# Functions to read data (after converting JSON to CSV)
def read_data():
    row_list = []
    with open('data.json') as json_file:
        jsondata = json.load(json_file)
    data_file = open('data.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
    count = 0
    for data in jsondata:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(data.values())
    data_file.close()
    with open('data.csv') as file:
        alllines = csv.reader(file)
        for row in alllines:
            row_list.append(row)
        return row_list

# Function having final data with BMI
def finaldata_with_bmi(alldata):
    line_count = 0
    notValidData = []
    validData = []
    for row in alldata:
        if line_count == 0:
            line_count = 1
        elif row[0].isalpha() == True and row[1].isnumeric() == True and row[2].isnumeric() == True :
            bmi = calculate_bmi(row)
            validData.append(row+bmi)
            line_count +=1
        else:
            notValidData.append(row)
            line_count +=1
    return validData

# Function to calculate BMI using mentioned conditions in problem
def calculate_bmi(data):
    BMI_categoty= None
    Health_risk= None
    BMI_range = None
    x = int(data[1])
    y = int(data[2])
    bmi = round(y/((x/100)**2), 2)
    if bmi <= 18.4 :
        BMI_categoty = BMI.bmi_categoty.get('UW')
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('MR')
    elif bmi >=18.5 and bmi <= 24.9:
        BMI_categoty = BMI.bmi_categoty.get('NW')
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('LR')
    elif bmi >=25 and bmi <= 29.9:
        BMI_categoty = BMI.bmi_categoty.get("OW")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('ER')
    elif bmi >=30 and bmi <= 34.9:
        BMI_categoty = BMI.bmi_categoty.get("MO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('MRS')
    elif bmi >= 35 and bmi <= 39.9:
        BMI_categoty = BMI.bmi_categoty.get("SO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('HR')
    elif bmi > 40:
        BMI_categoty = BMI.bmi_categoty.get("VSO")
        BMI_range = bmi
        Health_risk = BMI.health_risk.get('VHR')
    bmi_list =[BMI_categoty,BMI_range,Health_risk]
    return bmi_list

# Writing final output to CSV
def write_csv(data):
    with open('BMI Calculation output.csv', 'w',newline='') as file:
        csv_data = csv.writer(file, delimiter=',')
        csv_data.writerow(['Gender', 'Height', 'Weight', 'BMI_categoty', 'BMI_range', 'Health_risk'])
        for row in data:
            csv_data.writerows([row])
    return 'CSV file has been added successfully ~'

# Printing results
if __name__ == '__main__':
    contents = read_data()
    finaldata = finaldata_with_bmi(contents)
    print('Final data with BMI : ', finaldata)
    result = write_csv(finaldata)
    print(result)