import matplotlib.pyplot as plt #importing necessary stuff

x = [] #initializing arrays
y = []

readFile = open('millikan.txt','r') #reading in file
sepFile = readFile.read().split('\n') #separating file based off of spaces
readFile.close() #closing file

for plotPair in sepFile:
    xAndY = plotPair.split(' ') #splitting the x and y values
    x.append(float(xAndY[0]))
    y.append(float(xAndY[1]))

e_x = 0.0   #initializing the E values
e_y = 0.0
e_xx = 0.0
e_xy = 0.0

for i in range(0, len(x)):
    e_x = e_x + x[i]

e_x = (1/float(len(x)))*e_x #calculating the E values

for i in range(0, len(y)):
    e_y = e_y + y[i]

e_y = (1/float(len(y)))*e_y

for i in range(0, len(x)):
    e_xx = e_xx + pow(x[i],2.0)

e_xx = (1/float(len(x)))*e_xx

for i in range(0, len(y)):
    e_xy = e_xy + x[i]*y[i]

e_xy = (1/float(len(y)))*e_xy

m = (e_xy-e_x*e_y)/(e_xx-pow(e_x,2.0))
c = (e_xx*e_y - e_x*e_xy)/(e_xx-pow(e_x, 2.0)) #calculating slope and intercept

print(m, " is the slope")
print(c, " is the y intercept")

newY = []

for i in range(0, len(x)):
    newY.append(m*(x[i]) + c)  #calculating newY for the plot


plt.plot(x,y, 'r--', x, newY, 'bs') #plotting graph
plt.title('Millikan Graph')
plt.xlabel('frequency')
plt.ylabel('voltage')

plt.show() #showing graph