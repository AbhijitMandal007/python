# Develope Python program to compute sttistical measure without using numpy

# Given Data
marks = [78,85,92,67,88,73,95,81,76,89]
temperature = [28.5,30.2,29.8,31.4,27.9,32.1,30.5]
sales = [12500,13800,14200,11900,15100,14750,16000]

def statistic(data):
    n = len(data)
    #Mean
    mean =sum(data)/n
    #Median
    sort_data = sorted(data)
    if(n%2==0):
        median = (sort_data[n//2-1]+sort_data[n//2])/2
    else:
        median = (sort_data[n//2])
    # Standard Deviation
    veriance = sum((x-mean)**2 for x in data)/n
    std = veriance**0.5

    #MAX
    maximum = max(data) 
    #MIN 
    minimun = min(data)  

    return mean ,median,std,maximum,minimun  



data = {
    "marks":marks,"temperature":temperature,"sales":sales
}
for name,value in data.items():
    mean,median,maximum,minimun = statistic(value)

    print("\n",name)
    print("Mean =",mean)
    print("median =",median)
    print("standard deviation =",std)
    print("maximum =",max)
    print("minimun =",min)