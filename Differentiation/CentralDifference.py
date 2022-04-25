import plot;
import numpy as np;

#Problem : Find the slope of f(x) at x=X_0 by numerical method
def f(x):
    return np.sin(x)
X_0=np.pi/3;
delX=0.1;
#plug in True Value of f'(X_0) here if known beforehand,otherwise give 'None' value
#if TrueValue is set to 'None', errors won't show
trueValue:float=0.5;


#Central difference appoximation of slope m at X_0 of f(x)
def findSlope(function,X_0,delX):
    s=((function(X_0+delX))-(function(X_0-delX)))/(2*delX);
    return s;

# Forward Difference method to find deriavative of f(x) at X_0
def findSlopeForward(function,X_0,delX)->float:
    slope=(function(X_0+delX)-function(X_0))/delX;
    return slope;

#finds the value of c of a line y=mx+c which touches f(x) at X_0 
def findConstant(function,X_0,m)->float:
    c=function(X_0)-m*X_0;
    return c;

#find the absolute relative true error in percent
def error(trueValue,obtainedValue):
    err=(trueValue-obtainedValue)/trueValue;
    if(err<0):
        err=-1*err;
    return err*100;

#plot the main function
x1=np.arange(X_0-5,X_0+5.1,0.001);
plot.addPlot(x1,f(x1),Label='f(x)');
plot.addPoint(X_0,f(X_0),'green');

#get the values of tangent y=mx+c at X_0 obtainted by central method
m=findSlope(f,X_0,delX);
c=findConstant(f,X_0,m);

#plot the tangent by central method
x2=np.arange(X_0-1,X_0+1.1,0.1);
plot.addPlot(x2,m*x2+c,Label='central_tangent',color='red');

#get the values of tangent y=mx+c at X_0 obtainted by forward method

m1=findSlopeForward(f,X_0,delX);
c1=findConstant(f,X_0,m1);

#plot the tangent by forward method
x3=np.arange(X_0-1,X_0+1.1,0.1);
plot.addPlot(x2,m1*x2+c1,Label='forward_tangent',color='blue');

print('value of deriavative at x= ',X_0,' is: ',m,' (By Central Difference)');
print('value of deriavative at x= ',X_0,' is: ',m1,' (By Forward Difference)');
if(trueValue!=None):
    print('Absolute relative true error in central method: ',error(trueValue,m),' %');
    print('Absolute relative true error in forward method: ',error(trueValue,m1),' %');
plot.showPlot();