import csv
import plotly.express as px
import numpy as np

def plotFigure(datapath):
    with open(datapath) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()
        
def getDataSource(datapath):
    coffee=[]
    sleep=[]
    with open(datapath) as f:
        df=csv.DictReader(f)
        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":sleep}
def findCorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print(corelation[0,1])
    
def setUp():
    path="./cups of coffee vs hours of sleep.csv"
    datasource=getDataSource(path)
    findCorelation(datasource)
    plotFigure(path)
    
setUp()
    
    
    
    
    
    
        
            
            
        
    
    
