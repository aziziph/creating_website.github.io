# # libraries & dataset
# import seaborn as sns
# import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(12,6))
ax = plt.subplot(111)
plt.yscale('log')
#ax.set_zscale('log')
font = {'weight' : 'normal',
        'size'   : 20}
plt.rc('font', **font)
plt.rcParams["mathtext.fontset"] = "cm"
ax.tick_params('both', length=5, width=2, which='major', direction="in")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

file_name = "data"
data = np.loadtxt(file_name, unpack=True)
x = data[0]
y = data[1]
z = data[2]
#
file_name = "/home/maazizi/Projects/greenX/Time_grids/CP2K/CT_ST_MODULES/5_May/plots/3D_plot/data_full_erange"
data = np.loadtxt(file_name, unpack=True)
x1 = data[0]
y1 = data[1]
z1 = data[2]

plt.xticks(np.arange(min(x), max(x)+2, 2.0))

# plt.scatter(x, y,
#             edgecolors = 'black',
#             c = np.log10(z),
#             s = 150,
#             cmap=plt.cm.get_cmap('jet'))

for i in range(len(x1)):
     if (z1[i] > 0.1):
         plt.scatter(x1[i], y1[i], s=100, facecolors='none', edgecolors='gray')
        # plt.scatter(x1[i], y1[i], edgecolors='black', c=np.log10(z1[i]), s=150)
#cmap=plt.cm.get_cmap('hsv')
plt.scatter(x, y,
            edgecolors = 'black',
            c = np.log10(z),
            s = 100,
            cmap=plt.cm.get_cmap('jet'))
plt.xlabel("number of time/frequency points", fontsize=20)
plt.ylabel("$\epsilon_{max}/\epsilon_{min}$", fontsize=30)
plt.colorbar()
plt.savefig('duality_error_colour.eps', dpi=500)

plt.show()

