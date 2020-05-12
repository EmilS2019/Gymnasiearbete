import csv
import matplotlib.pyplot as plt

def dataAnalysis():
    with open('smhi.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        data=list(csv.reader(csvfile))
        
        leapYearOffset=0
        percipitationArray, totalExtremePercipitation = [],[]
        
        #There are 161 years from 1858 to 2019
        #41 years between 1858 and 1900
        #Since this loops from 1900-2019
        for i in range(41,161):
            #J is the index for first of January 
            j = i*365-345+leapYearOffset

            row, date = getRowData(data, j)

            leapyear=0
            if(isLeapYear(date[0])==True):
                leapYearOffset+=1
                leapyear=1

            avgPercipitation, totalPercipitation = 0,0
            extremePercipitationDays=0
            
            for k in range(j, j+365+leapyear):
                row, date = getRowData(data, k)
                
                #Appends precipitation to lists
                percipitation = float(row[3])
                totalPercipitation += percipitation
                if(percipitation > 40):
                    extremePercipitationDays+=1

            avgPercipitation = totalPercipitation/(365+leapyear)
            percipitationArray.append(avgPercipitation)
            totalExtremePercipitation.append(extremePercipitationDays)
            print(f"year: {date[0]}, average percipitation: {avgPercipitation}")            
            print(f"year: {date[0]}, extreme percipitation days: {extremePercipitationDays}")            
            #print(date) 
        plt.plot([i for i in range(1899,2019)], totalExtremePercipitation)
        plt.show()


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