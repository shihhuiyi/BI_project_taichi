# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 建立座標
# label 空白:0 白色(左):1 黑色(右):2
data = []
for x in range(1,201):
    for y in range (1,201):
        label = 0
        #標記太極內外
        if (x-100)**2 + (y-100)**2 <=10000: label =1
        data.append([x,y,label])
data = np.array(data)

#右半標記為黑
for i in range(len(data)):
    x,y=data[i,0],data[i,1]
    if ((x-100)**2+(y-50)**2 >2500) & (x>100) & ((x-100)**2 + (y-100)**2 <10000):
        data[i,2] = 2

#上面標記為黑
for i in range(len(data)):
    x,y=data[i,0],data[i,1]
    if (x-100)**2 + (y-150)**2 <=2500:
        data[i,2] = 2

#上面小圓標記為白
for i in range(len(data)):
    x,y=data[i,0],data[i,1]
    if (x-100)**2 + (y-150)**2 <=300:
        data[i,2] = 1

#下面小圓標記為黑
for i in range(len(data)):
    x,y=data[i,0],data[i,1]
    if (x-100)**2 + (y-50)**2 <=300:
        data[i,2] = 2

colors = ['darkgrey','white','black']
fig = plt.figure(figsize=(4,4))
plt.scatter(data[:,0],data[:,1],c = data[:,2],cmap=matplotlib.colors.ListedColormap(colors))
# %%
