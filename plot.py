#%%
import matplotlib.pyplot as plt
import numpy as np




# %%
fig = plt.figure(figsize=(9, 7))
n = 10
my_xticks = ['chest', 'oct', 'path', 'axial', 'pneumonia', 'derma', 'coronal', 'retina', 'breast', 'sagittal']
X = np.arange(n)+1 
plt.xticks(X, my_xticks, rotation=45)
Y_orig = np.array([0.69960, 0.94638, 0.96283, 0.99481, 0.96006, 0.89606, 0.99056, 0.72535, 0.90915, 0.97121])
Y_ours = np.array([0.67783, 0.90254, 0.95670, 0.98687, 0.93753, 0.87747, 0.98661, 0.70135, 0.85338, 0.95773])
plt.bar(X, Y_ours, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='ours', lw=1)
plt.bar(X+0.35, Y_orig, alpha=0.9, width = 0.35, facecolor = 'yellowgreen', edgecolor = 'white', label='origin', lw=1)
plt.legend(loc="upper left") 
fig.suptitle("AUC Results of Resnet18")
fig.savefig('./auc_reset18.jpg')
plt.clf()
# %%
fig = plt.figure(figsize=(9, 7))
n = 10
my_xticks = ['chest', 'oct', 'path', 'axial', 'pneumonia', 'derma', 'coronal', 'retina', 'breast', 'sagittal']
X = np.arange(n)+1 
plt.xticks(X, my_xticks, rotation=45)
Y_orig = np.array([0.94681, 0.72300, 0.82214, 0.91636, 0.84615, 0.73766, 0.90215, 0.53500, 0.83974, 0.75411])
Y_ours = np.array([0.94741, 0.68600, 0.79958, 0.88593, 0.83013, 0.72170, 0.86901, 0.54250, 0.83974, 0.73372])
plt.bar(X, Y_ours, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='ours', lw=1)
plt.bar(X+0.35, Y_orig, alpha=0.9, width = 0.35, facecolor = 'yellowgreen', edgecolor = 'white', label='origin', lw=1)
plt.legend(loc="upper left") 
fig.suptitle("ACC Results of Resnet18")
fig.savefig('./acc_reset18.jpg')
plt.clf()
# %%
fig = plt.figure(figsize=(9, 7))
n = 7
my_xticks = ['axial', 'pneumonia', 'derma', 'coronal', 'retina', 'breast', 'sagittal']
X = np.arange(n)+1 
plt.xticks(X, my_xticks, rotation=45)
Y_orig = np.array([0.99357, 0.94934, 0.88189, 0.98904, 0.70689, 0.84586, 0.96883])
Y_ours = np.array([0.98801, 0.93643, 0.85398, 0.97871, 0.69673, 0.85046, 0.95731])
plt.bar(X, Y_ours, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='ours', lw=1)
plt.bar(X+0.35, Y_orig, alpha=0.9, width = 0.35, facecolor = 'yellowgreen', edgecolor = 'white', label='origin', lw=1)
plt.legend(loc="upper left") 
fig.suptitle("AUC Results of Resnet50")
fig.savefig('./auc_reset50.jpg')
plt.clf()
# %%
fig = plt.figure(figsize=(9, 7))
n = 7
my_xticks = ['axial', 'pneumonia', 'derma', 'coronal', 'retina', 'breast', 'sagittal']
X = np.arange(n)+1 
plt.xticks(X, my_xticks, rotation=45) 
Y_orig = np.array([0.90550, 0.87179, 0.71471, 0.87857, 0.48500, 0.80769, 0.73972])
Y_ours = np.array([0.87704, 0.79808, 0.69875, 0.83478, 0.50500, 0.83333, 0.72318])
plt.bar(X, Y_ours, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='ours', lw=1)
plt.bar(X+0.35, Y_orig, alpha=0.9, width = 0.35, facecolor = 'yellowgreen', edgecolor = 'white', label='origin', lw=1)
plt.legend(loc="upper left") 
fig.suptitle("ACC Results of Resnet50")
fig.savefig('./acc_reset50.jpg')
plt.clf()

# %%

# %%
