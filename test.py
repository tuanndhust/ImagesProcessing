import numpy as np
#path to pose.txt file
ego = '/home/tuannghust/ego2odo.txt'
#path to converted file
odo = '/home/tuannghust/odo/txt'
#from list string to transformation matrix (4x4)
def str2arr(str):
    arr = str.split(" ")
    arr = list(map(int, arr))
    arr = np.array(arr)
    arr = arr.reshape([3,4])
    arr1 = np.array([[0,0,0,1]])
    arr = np.concatenate((arr,arr1))
    return arr
def arr2str(arr):
    arr = arr[:3].flatten()
    arrtolist = arr.tolist()
    arrtostr = ' '.join(str(e) for e in arrtolist)
    return arrtostr
with open(ego) as f:
    read_pose = [s.strip() for s in f.readlines()]
    num_pose = len(read_pose)
odometry = []
# odometry[0] = arr2str(read_pose[0])
for i in range(num_pose):
    odometry.append(str2arr(read_pose[i]))    
for i in range(1,len(odometry)):
    odometry[i] = odometry[i]@odometry[i-1]
print(odometry)
