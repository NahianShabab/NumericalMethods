import plot;
import numpy as np;

# Find first deriavative of f(x) at X_0
X_0=16; 

def f(x):
    return (2000*np.log(14*10**4/(14*10**4-2100*x))-9.8*x);

# Forward Difference method to find deriavative of f(x) at X_0
def findSlope(function,X_0,delX)->float:
    slope=(function(X_0+delX)-function(X_0))/delX;
    return slope;

#finds the value of c of a line y=mx+c which touches f(x) at X_0 
def findConstant(function,X_0,m)->float:
    c=function(X_0)-m*X_0;
    return c;

#plot the main function
x1=np.arange(X_0-5,X_0+5.1,0.1);
plot.addPlot(x1,f(x1),Label='f(x)');

#get the values of tangent y=mx+c at X_0
delX=0.1;
m=findSlope(f,X_0,delX);
c=findConstant(f,X_0,m);

#plot the tangent
x2=np.arange(X_0-1,X_0+1.1,0.1);
plot.addPlot(x2,m*x2+c,Label='tangent',color='red');

print('value of deriavative at x= ',X_0,' is: ',m);
plot.showPlot();