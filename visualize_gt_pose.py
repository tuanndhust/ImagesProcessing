import numpy as np
import matplotlib.pyplot as plt

ego = '/home/tuanhust/Data/KITTI/kitti_test/10_3/poses.txt'
# # ego = '/home/tuanhust/ego.txt'

# with open(ego) as f:
#     read_pose = [s.strip() for s in f.readlines()]
#     num_pose = len(read_pose)
# #print(read_pose)
# x = []
# y = []
# for i in range(num_pose):
#     a = read_pose[i].split(" ")
#     x.append(a[3])
#     y.append(a[11])
# print(x)
#print(y)

poses = np.loadtxt(ego)

x = poses[:, 3]
y = poses[:, 7]

plt.plot(x,y)
plt.title('sequence')

plt.show()
