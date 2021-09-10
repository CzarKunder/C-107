import csv
import numpy as np
import plotly.express as px

def plotFigure(datapath):
    with open(datapath)as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Temperature",y="Ice-cream Sales( ₹ )")
        fig.show()
        
def getDataSource(datapath):
    icecreamsales=[]
    temperature=[]
    with open(datapath)as f:
        df=csv.DictReader(f)
        for row in df:
            icecreamsales.append(float(row["Ice-cream Sales( ₹ )"]))
            temperature.append(float(row["Temperature"]))
    return{"x":icecreamsales,"y":temperature}
def findCorelation(datasource):
    corelation=np.corrcoef(datasource["x"],datasource["y"])
    print(corelation[0,1])
    
def setUp():
    path="./Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    datasource=getDataSource(path)
    findCorelation(datasource)
    plotFigure(path)
    
setUp()
