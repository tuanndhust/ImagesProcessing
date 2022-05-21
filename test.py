import numpy as np
import matplotlib.pyplot as plt

data = np.load("/home/tuannghust/SfmLearner-Pytorch/SfmLearner Models-20220520T152108Z-001/SfmLearner Models/predictions.npy")
for i in range(1,len(data)):
	r = data[i-1,1]
	data[i] = r[:,:3] @ data[i]
	data[i,:,:,-1] = data[i,:,:,-1] + r[:,-1]
groundtruth = []
for i in range(0, 5):
    x = data[0, i, 0, 3]
    z = data[0, i, 2, 3]
    groundtruth = np.append(groundtruth, [x, z])
for i in range(1, 1201):
    x = data[i, 4, 0, 3]
    z = data[i, 4, 2, 3]
    groundtruth = np.append(groundtruth, [x, z])
g = groundtruth.reshape(1205, 2)
plt.scatter(g[:, 0], g[:, 1])
plt.savefig('/home/tuannghust/10_1.jpg')