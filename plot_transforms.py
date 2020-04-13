import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#following tutorial here: https://matplotlib.org/3.1.1/tutorials/advanced/transforms_tutorial.html

x = np.arange(0,10,0.005)
y = np.exp(-x/2) * np.sin(2*np.pi*x)

fig, ax = plt.subplots()    #subplot figure argument and axis arguments are stored
ax.plot(x,y)
ax.set_xlim(0,10)
ax.set_ylim(-1,1)

xdata, ydata = 5, 0
xdisplay, ydisplay = ax.transData.transform_point((xdata, ydata))

bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(
    arrowstyle = "->",
    connectionstyle="angle,angleA=0,angleB=90,rad=10")

offset = 72
ax.annotate('data = (%.1f, %.1f)' % (xdata,ydata),
            xy=(xdata,ydata), xytext=(-2*offset,offset), textcoords='offset points',
            bbox=bbox, arrowprops=arrowprops)

disp = ax.annotate('display = (%.1f, %.1f)' % (xdisplay,ydisplay),
                   xy=(xdisplay,ydisplay), xytext=(0.5*offset,-offset),
                   xycoords='figure pixels',
                    textcoords='offset points',
                   bbox=bbox, arrowprops=arrowprops)
#plt.show()



fig = plt.figure()
for i, label in enumerate(('A', 'B', 'C', 'D')):
    ax = fig.add_subplot(2, 2, i+1)
    ax.text(0.05, 0.95, label, transform=ax.transAxes,
            fontsize=16, fontweight='bold', va='top')

#plt.show()

fig, ax = plt.subplots()
x,y = 10*np.random.rand(2,1000)
ax.plot(x,y, 'go', alpha =0.2) #plot data in data coordinates

rect = mpatches.Rectangle((0.5,0.5), width=0.25, height=0.25, transform = ax.transAxes, facecolor='blue', alpha=0.75)

ax.add_patch(rect)
plt.show()