import flowtools
import matplotlib.pyplot as plt
# import seaborn

gamma = 1.4


with open("Data_Test_3B.txt","r") as fin: #Taking data from measurement 3A/B
    for testfile3 in fin:
        testfile3 = fin.readlines()

with open("Data_Test_4B.txt","r") as fin: #Taking data from measurement 4A/B
    for testfile4 in fin:
        testfile4 = fin.readlines()

with open("Data_Test_5B.txt","r") as fin: #Taking data from measurement 5A/B
    for testfile5 in fin:
        testfile5 = fin.readlines()


xtab = []
p__pt_measured3_tab = []
M_measured3_tab = []

p__pt_measured4_tab = []
M_measured4_tab = []

p__pt_measured5_tab = []
M_measured5_tab = []

hk2 = 14.6
dh__dx = 0.01692
h0 = 8.0

for line in testfile3:
    line = line.strip()
    line = line.split()
    xtab.append(float(line[0]))
    p__pt_measured3_tab.append(float(line[1]))
#    M_measured3_tab.append(flowtools.flowisentropic2(gamma, float(line[1]), 'pres')[0])

for line in testfile4:
    line = line.strip()
    line = line.split()
    p__pt_measured4_tab.append(float(line[1]))
#    M_measured4_tab.append(flowtools.flowisentropic2(gamma, float(line[1]), 'pres')[0])

for line in testfile5:
    line = line.strip()
    line = line.split()
    p__pt_measured5_tab.append(float(line[1]))
#    M_measured5_tab.append(flowtools.flowisentropic2(gamma, float(line[1]), 'pres')[0])

pe3__pt_theoretical_tab = []

throat2xtab = [x for x in range(410, 761)]

for i in range(len(throat2xtab)):
    regime = 'sub'
    values = flowtools.flowisentropic2(gamma, ((dh__dx * throat2xtab[i]) + h0)/hk2, regime)
    pe3__pt_theoretical_tab.append(float(values[2]))


for i in range(len(throat2xtab)):
    values = flowtools.flowisentropic2(gamma, ((dh__dx * throat2xtab[i]) + h0)/hk2, regime)
    pe3__pt_theoretical_tab.append(float(values[2]))

shock1_pos = 630
shock2_pos = 530

h_shock1 = dh__dx * shock1_pos + h0
h_shock2 = dh__dx * shock2_pos + h0

Aratio_shock1 = h_shock1/hk2
Aratio_shock2 = h_shock2/hk2

pe6__pt_shock1 = flowtools.flowisentropic2(gamma, Aratio_shock1, 'sup')[2]
pe6__pt_shock2 = flowtools.flowisentropic2(gamma, Aratio_shock2, 'sup')[2]

M_shock1 = flowtools.flowisentropic2(gamma, Aratio_shock1, 'sup')[0]
M_shock2 = flowtools.flowisentropic2(gamma, Aratio_shock2, 'sup')[0]

print(M_shock1, M_shock2)

shock1 = flowtools.flownormalshock2(gamma, M_shock1, 'mach')
shock2 = flowtools.flownormalshock2(gamma, M_shock2, 'mach')

print(shock1)
print(shock2)

pe5__pt_shock1 = (shock1[2] * pe6__pt_shock1)
pe5__pt_shock2 = (shock2[2] * pe6__pt_shock2)

pe3__pt_shock1 = flowtools.flowisentropic2(gamma, Aratio_shock1, 'sub')[2]
pe3__pt_shock2 = flowtools.flowisentropic2(gamma, Aratio_shock2, 'sub')[2]

# At__astar_shock1 = flowtools.flowisentropic2(gamma, pe5__pt_shock1, 'pres')[4]/Aratio_shock1
# At__astar_shock2 = flowtools.flowisentropic2(gamma, pe5__pt_shock2, 'pres')[4]/Aratio_shock2

# p__pt_shock1theoretical_tab = []
# for i in range(len(throat2xtab)):
#     if throat2xtab[i] < shock1_pos:
#         Aratio = ((dh__dx * throat2xtab[i]) + h0)/hk2
#         regime = 'sup'
#     else:
#         Aratio = (((dh__dx * throat2xtab[i]) + h0)/hk2) * At__astar_shock1
#         regime = 'sub'
#     values = flowtools.flowisentropic2(gamma, Aratio, regime)
#     p__pt_shock1theoretical_tab.append(float(values[2]))

# p__pt_shock2theoretical_tab = []
# for i in range(len(throat2xtab)):
#     if throat2xtab[i] < shock2_pos:
#         Aratio = ((dh__dx * throat2xtab[i]) + h0)/hk2
#         regime = 'sup'
#     else:
#         Aratio = (((dh__dx * throat2xtab[i]) + h0)/hk2) * At__astar_shock2
#         regime = 'sub'
#     values = flowtools.flowisentropic2(gamma, Aratio, regime)
#     p__pt_shock2theoretical_tab.append(float(values[2]))


# fig, ax = plt.subplots(figsize=(60, 40))

print(pe3__pt_shock1, pe5__pt_shock1, pe6__pt_shock1)
print(pe3__pt_shock2, pe5__pt_shock2, pe6__pt_shock2)

#plt.vlines(44.8, 0, 1, linestyle='--', color='k', linewidth=0.7)
#plt.vlines(760, 0, 1, linestyle='--', color='k', linewidth=0.7)
plt.plot([shock1_pos, shock1_pos], [0, 1], '--', color = "lightseagreen", label='Shock position - 3B')
plt.plot([shock2_pos, shock2_pos], [0, 1], '--', color = "chocolate", label='Shock position - 4B')
plt.plot([390, 390], [0, 1], '--', color='fuchsia', label='Second throat position')

plt.plot(xtab, p__pt_measured3_tab, color ='darkcyan', label="3B experiment")
plt.plot(xtab, p__pt_measured4_tab, color = 'sienna', label="4B experiment")
plt.plot(xtab, p__pt_measured5_tab, color = 'violet', label="5B experiment")

plt.plot([shock1_pos], [pe6__pt_shock1], 'o', label='Min. p/p_t for supersonic flow - 3B')
plt.plot([shock2_pos], [pe6__pt_shock2], 'o', label='Min. p/p_t for supersonic flow - 4B')
plt.plot([shock1_pos], [pe5__pt_shock1], 'o', label='p/p_t after shock - 4B')
plt.plot([shock2_pos], [pe5__pt_shock2], 'o', label='p/p_t after shock - 5B')
plt.plot([shock1_pos], [pe3__pt_shock1], 'o', label='Max. p/p_t for subsonic flow - 3B')
plt.plot([shock2_pos], [pe3__pt_shock2], 'o', label='Max. p/p_t for subsonic flow - 4B')
# plt.plot(throat2xtab, pe3__pt_theoretical_tab, 'y', label="Theoretical flow with pe3 at exit")
# plt.plot(throat2xtab, p__pt_shock1theoretical_tab, 'b', label="Theoretical flow with shock at x=630mm")
# plt.plot(throat2xtab, p__pt_shock2theoretical_tab, 'r', label="Theoretical flow with shock at x=530mm")
# plt.xlim(40, 200)
##ax.set_aspect('equal')
# ax.grid(True, linestyle='--', which='both')

# seaborn.despine(ax=ax, offset=0) 
plt.xlim(0, 900)
plt.ylim(0, 1)
plt.xlabel('x[mm]')
plt.ylabel('p/p_t [-]')
plt.legend()
plt.show()

# out = flowtools.flowisentropic2(gamma,50.0,'sub')
# print(out)

# out2 = flowtools.flownormalshock2(gamma,2.5,'mach')
# print(out2)
