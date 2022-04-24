import matplotlib.pyplot as plt;
import numpy as np


def addPlot(x,y,color='black',Label=None):
    if(Label==None):
        plt.plot(x,y,color);
    else:
        plt.plot(x,y,color,label=Label);
    pass;

def addPoint(x,y,color='black'):
    plt.scatter(x,y,c=color);

def showPlot(xLabel:str='x',yLabel:str='y',hasGrid:bool=True):
    plt.xlabel=xLabel;
    plt.ylabel=yLabel;
    plt.axhline(0)
    plt.axvline(0);
    plt.grid(hasGrid);
    plt.legend();
    plt.show();
    pass;


if __name__=="__main__":
    x=np.arange(-2,2.1,0.1);
    addPlot(x,x,'red','linear');
    addPlot(x,x**2,'green','quadratic');
    addPoint(1,2,color='red');
    showPlot('x','y');