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
    #print(arr)
    return arr
with open(ego) as f:
    read_pose = [s.strip() for s in f.readlines()]
    num_pose = len(read_pose)
ego.close()
# ar = str2arr(read_pose[1]) 
# ar2 =  str2arr(read_pose[1-1])
# print(ar.dot(ar2))
# print(ar)
# print(ar2.shape)
for i in range(1,num_pose):
    read_pose[i] = str2arr(read_pose[i]) @ str2arr(read_pose(i-1))
    
print(read_pose)
