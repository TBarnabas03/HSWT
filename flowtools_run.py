import flowtools
import numpy as np
import matplotlib.pyplot as plt

x_loc = []
ppt = []
areas_loc = []
areas = [] #A/A_t for the fixed nozzle

Mach = []
TT0 = []
pp0 = []
rr0 = []
aa_ref = []


skip = 2
count = 0

#reading measurements
f_1ab = open(".\data_for_report\\Data_Test_1AB.txt", "r")
for x in f_1ab:
    if count >= skip:
        x = x.strip()
        values = x.split()
        x_loc.append(float(values[0]))
        ppt.append(float(values[1].strip()))
    count += 1

#reading fixed nozzle area ratios
f_area = open("area.txt", "r")
for line in f_area:
    areas.append(float(line))

#reading fixed nozzle area ratio locations
f_arealoc = open("area ratio locations.txt", "r")
for line in f_arealoc:
    areas_loc.append(float(line))

#fixed nozzle area ratio arrays
areas_loc = np.array(areas_loc)
areas = np.array(areas)
areas_sub = areas[0:3]
areas_sup = areas[3:]

#pressure readings with location arrays
x_loc = np.array(x_loc)
ppt = np.array(ppt)

gamma = 1.4

for i in areas_sub:
    out = flowtools.flowisentropic2(gamma,i,'sub')
    Mach.append(out[0])

for i in areas_sup:
    out = flowtools.flowisentropic2(gamma,i,'sup')
    Mach.append(out[0])

for i in areas_sub:
    out = flowtools.flowisentropic2(gamma,i,'sub')
    Mach.append(out[0])

for i in areas_sup:
    out = flowtools.flowisentropic2(gamma,i,'sup')
    Mach.append(out[0])

#print(Mach)
plt.subplot(311)
plt.plot(areas_loc,areas,marker="o", label="Area to throat ratios")
plt.xlabel("x [mm]")
plt.ylabel("A/At [-]")
plt.xlim(40, 200)
plt.ylim(0,2.5)
plt.legend()

plt.subplot(312)
plt.plot(x_loc,ppt,marker="o", label="Measured pressure ratios")
plt.xlabel("x [mm]")
plt.ylabel("p/pt [-]")
plt.xlim(40, 200)
plt.ylim(0,1)
plt.legend()

plt.subplot(313)
plt.plot(areas_loc,Mach,marker="o", label="Theoretical Mach number")
plt.xlabel("x [mm]")
plt.ylabel("M [-]")
plt.xlim(40, 200)
plt.ylim(0,2.5)
plt.legend()

plt.show()

#out2 = flowtools.flownormalshock2(gamma,2.5,'mach')
#print(out2)

f_1ab.close()
f_area.close()