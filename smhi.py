import csv

def dataAnalysis():
    with open('smhi.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        data=list(csv.reader(csvfile))
        
        leapYearOffset=0
        #There are 161 years from 1858 to 2019
        #41 years between 1858 and 1900
        #Since this loops from 1900-2019
        for i in range(41,161):
            #J is the index for first of January 
            j = i*365-345+leapYearOffset

            row=data[j][0].split(";")
            date=row[2].split("-")
            row, date = getRowData(data, j)

            leapyear=0
            if(isLeapYear(date[0])==True):
                leapYearOffset+=1
                leapyear=1

            for k in range(j, j+365+leapyear):
                row=data[k][0].split(";")
                date=row[2].split("-")
                print(date)
            
            #print(date) 
    
    
def isLeapYear(year):
    year = int(year)
    if (year % 4) == 0:  
        if (year % 100) == 0:  
            if (year % 400) == 0:  
                return True  
            else:  
                return False
        else:  
            return True
    else:  
        return False


def getRowData(data, row):
    row=data[row][0].split(";")
    date=row[2].split("-")
    return row, date

dataAnalysis()