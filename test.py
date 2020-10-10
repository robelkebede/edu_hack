
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def generate():
    bad = [np.random.randint(0,4) for i in range(24)]
    good = [np.random.randint(4,6) for i in range(154)]
    vgood = [np.random.randint(6,8) for i in range(24)]

    sample = bad+good+vgood
    sample = np.array(sample)

    #np.save("stud_data.npy",sample)

    y = [i for i in range(len(sample))]
    return sample
    #plt.scatter(sample,y)
    #plt.show()

def means():
    X = np.load("stud_data.npy")
    X = np.append(3,X)[:,np.newaxis]

    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    labels = np.array(kmeans.labels_)[:,np.newaxis]
    stud_id = np.array([i for i in range(len(labels))])[:,np.newaxis]

    print(labels.shape)
    print(stud_id.shape)
    table = np.concatenate([stud_id,labels],axis=1)

    print(table.shape)
    print(table[139])


y = generate()

plt.hist(y)
plt.show()



