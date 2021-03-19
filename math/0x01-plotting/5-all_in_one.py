#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig2.suptitle("All in one")
f2_ax1.plot( y0, color="red")
f2_ax1.set_xticks(np.arange(0, 12, 2))
f2_ax1.set_yticks(np.arange(0, 1200, 200))
f2_ax1.set_xlim([0, 10])

f2_ax2.scatter( x1,y1, c = 'purple',s=6)
f2_ax2.set_xlabel(xlabel="Height (in)",fontsize=8)
f2_ax2.set_ylabel(ylabel="Weight (lbs)",fontsize=8)
f2_ax2.set_title("Men's Height vs Weight",fontsize=8)


f2_ax3.plot(x2,y2)
f2_ax3.set_yscale("log")
f2_ax3.set_xlabel(xlabel="Time (years)",fontsize=8)
f2_ax3.set_ylabel(ylabel="Fraction Remaining",fontsize=8)
f2_ax3.set_title("Exponential Decay of C-14",fontsize=8)
f2_ax3.set_xticks(np.arange(0, 28000, 5000))
f2_ax3.set_xlim([0, 28000])


f2_ax4.plot(x3,y31,'r',dashes=[2, 3, 2, 3], label='C-14')
f2_ax4.plot(x3,y32,'g',label='Ra-226', markersize=5)
f2_ax4.set_xlabel(xlabel="Time (years)",fontsize=8)
f2_ax4.set_xticks(np.arange(0, 22500, 2500))
f2_ax4.set_xlim([0, 20000])
f2_ax4.set_ylim([0, 1])
f2_ax4.set_ylabel(ylabel="Fraction Remaining",fontsize=8)
f2_ax4.set_title("Exponential Decay of Radioactive Elements",fontsize=8)

f2_ax5.hist(student_grades, range=(0,100),bins = 10,ec="black")
f2_ax5.set_title("Project A",fontsize=8)
f2_ax5.set_xlabel(xlabel='Grades',fontsize=8)
f2_ax5.set_xticks(np.arange(0,110,10))
f2_ax5.set_yticks(np.arange(0,35,5))
f2_ax5.set_xlim([0, 100])
f2_ax5.set_ylabel(ylabel='Number of Students',fontsize=8,va="center",ha="center")

plt.show()
