# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:21:23 2014

@author: hakan
"""

from matplotlib import rc
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)


import numpy as np
import matplotlib as mpl

npoints = 1024

np.random.seed(11)

x = np.random.randn(npoints)
y = np.random.randn(npoints)
xy = np.column_stack([x,y])

covxy = np.cov(xy.T)

plot(x,y,'.',alpha=0.16,ms=10)
xlabel('$x$');ylabel('$y$')
axis('equal')

mux,sigmax = np.mean(x), np.std(x)
muy,sigmay = np.mean(y), np.std(y)

print "mux,sigmax = ", mux,sigmax
print "muy,sigmay = ", muy,sigmay

mux_, muy_ = 6,4
sigmax_, sigmay_ = 2,1
theta = 120*np.pi/180.0

x_ = mux_ + np.cos(theta)*sigmax_*x - np.sin(theta)*sigmay_*y
y_ = muy_ + np.sin(theta)*sigmax_*x + np.cos(theta)*sigmay_*y

plot(x_,y_,'.r',alpha=0.16,ms=10)

def shadedEllipse(x,y,a,b,theta,col,alp):
    ell1 = matplotlib.patches.Ellipse((x,y),a,b,theta)
    ell1.set_alpha(alp)
    ell1.set_facecolor(col)
    ell1.set_edgecolor(col)
    return ell1

shades = [(0.9,)*3,(0.8,)*3,(0.7,)*3]
radii = [3,2,1]
alp = 0.7
for i in range(3):
    ell1 = shadedEllipse(0,0,1*radii[i]*2,1*radii[i]*2,0,shades[i],alp)
    ell2 = shadedEllipse(mux_,muy_,sigmax_*radii[i]*2,sigmay_*radii[i]*2,theta*180.0/np.pi,shades[i],alp)   
    
    pl.gca().add_artist( ell1 )
    pl.gca().add_artist( ell2 )
    
mpl.pyplot.annotate("$\mu_x,\mu_y$", (0,0), (-3,3), size=10,
         arrowprops=dict(arrowstyle="->",                         
                         fc=(1,1,0), ec="green",
                         patchB=None,
                         connectionstyle="angle3,angleA=-90,angleB=0"))
                         
mpl.pyplot.annotate("$\mu_x^{'},\mu_y^{'}$", (mux_,muy_), (mux_+6,muy_+6), size=10,
         arrowprops=dict(arrowstyle="->",                         
                         fc=(1,1,0), ec="green",
                         patchB=None,
                         connectionstyle="angle3,angleA=-90,angleB=0"))                         
                         
mpl.pyplot.annotate("$\sigma_x$",xycoords='data',textcoords='data',xy=(0,0),xytext=(3.0,0.0),size=10,annotation_clip=False,arrowprops=dict(arrowstyle="->", fc=(1,1,0), ec="green",patchA=None,patchB=None,shrinkA=0.,shrinkB=0.))
                         

#grid(xdata=range(-5,10,1))
#xlim(-5,10)
#ylim(-5,10)
#xticks(range(-5,10,1))
#yticks(range(-5,10,1))
mpl.pyplot.grid()

mpl.pyplot.savefig('plt1.pdf')
