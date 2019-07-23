import numpy.random as npr
import numpy as np
print(npr.rand())
print(*(100,2))
#print(npr.randn(*(100,2)))#*samp_traj.shape
orig_trajs = [[[1,3],[34,2]],[[23,4],[24,546]]]
orig_trajs = np.stack(orig_trajs, axis=0)
print(orig_trajs)