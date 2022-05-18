import numpy as np
#path to pose.txt file
ego = '/home/tuannghust/ego2odo.txt'
#path to converted file
odo = '/home/tuannghust/odo/txt'
def str2arr(str):
    arr = str.split(" ")
    arr = list(map(int, arr))
    arr = np.array(arr)
    arr = arr.reshape([3,4])
    #print(arr)
    return arr
with open(ego) as f:
    read_pose = [s.strip() for s in f.readlines()]
    num_pose = len(read_pose)
ar = str2arr(read_pose[1]) 
ar2 =  str2arr(read_pose[1-1])
print(ar.dot(ar2))
print(ar)
print(ar2.shape)
# for i in range(1,num_pose):
#      read_pose[i] = str2arr(read_pose[i]) @ str2arr(read_pose[i-1])
# print(read_pose)
