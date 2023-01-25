import flowtools
import numpy as np
import matplotlib.pyplot as plt

x_loc = []
ppt = []

skip = 2
count = 0

f1 = open("testfile.txt", "r")

for x in f1:
    if count >= skip:
        x = x.strip()
        values = x.split("\t")
        x_loc.append(float(values[0]))
        ppt.append(float(values[1].strip()))
    count += 1
    
x_loc = np.array(x_loc)
ppt = np.array(ppt)

plt.plot(x_loc,ppt)
plt.show()

gamma = 1.4



#out = flowtools.flowisentropic2(gamma,50.0,'sub')
#print(out)

#out2 = flowtools.flownormalshock2(gamma,2.5,'mach')
#print(out2)

f.close()