import matplotlib.pyplot as plt
import numpy as np
import pickle

with open('file_communities.pkl', 'rb') as f:
    file_comms = pickle.load(f)
with open('service_communities.pkl', 'rb') as f:
    service_comms = pickle.load(f)

xticks = ['2.0.0', '2.0.5', '2.0.8', '2.2.0', '3.0.0']
fig, axs = plt.subplots(2, 2)

file_raw = file_comms['raw_temporal_activity']
file_in = file_comms['in_temporal_activity']
service_raw = service_comms['raw_temporal_activity']
service_in = service_comms['in_temporal_activity']
file_in = file_in / np.max(file_in)
file_raw = file_raw / np.max(file_raw)
service_in = service_in / np.max(service_in)
service_raw = service_raw / np.max(service_raw)
print(service_raw.shape)

plt.subplot(221)
plt.plot(file_raw[:,0], 'o-', label='File comm. 1')
plt.plot(file_raw[:,1], 'x--', label='File comm. 2')
plt.title('File collaboration')
plt.ylabel('Raw activity')
plt.xticks([0, 1, 2, 3, 4], xticks)
#plt.legend()

plt.subplot(222)
plt.plot(service_raw[:,0], 'o-', label='Service comm. 1')
plt.plot(service_raw[:,1], 'x--', label='Service comm. 2')
plt.plot(service_raw[:,2], '+-.', label='Service comm. 3')
plt.plot(service_raw[:,3], 'd:', label='Service comm. 4')
plt.plot(service_raw[:,4], 'v-', label='Service comm. 5')
plt.title('Service collaboration')
plt.xticks([0, 1, 2, 3, 4], xticks)
#plt.legend()

plt.subplot(223)
plt.plot(file_in[:,0], 'o-')
plt.plot(file_in[:,1], 'x--')
plt.ylabel('Scaled activity')
plt.xticks([0, 1, 2, 3, 4], xticks)

plt.subplot(224)
plt.plot(service_in[:,0], 'o-', label='Service comm. 1')
plt.plot(service_in[:,1], 'x--', label='Service comm. 2')
plt.plot(service_in[:,2], '+-.', label='Service comm. 3')
plt.plot(service_in[:,3], 'd:', label='Service comm. 4')
plt.plot(service_in[:,4], 'v-', label='Service comm. 5')
plt.xticks([0, 1, 2, 3, 4], xticks)

fig.supxlabel('Release')
fig.suptitle("Temporal activity of discovered communities")

plt.savefig('temporal_activity.png')
plt.show()
