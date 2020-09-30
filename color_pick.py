import cv2
from sklearn.cluster import KMeans
import urllib.request
import numpy as np

class ColorFinder:

    IMAGE = None
    COLORS = None
    LABELS = None
    
    def __init__(self, image_url):
        self.IMAGE_URL = image_url
        # print(self.IMAGE_URL)
        url_response = urllib.request.urlopen(self.IMAGE_URL)
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        self.IMAGE = cv2.imdecode(img_array, -1)

        
    def dominantColors(self):
    
        #read image
        img = self.IMAGE.copy()
        #convert to rgb from bgr
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
        #reshaping to a list of pixels
        img = img.reshape((img.shape[0] * img.shape[1], 3))
        
        
        #using k-means to cluster pixels
        kmeans = KMeans(n_clusters = 2)
        kmeans.fit(img)
        
        #the cluster centers are our dominant colors.
        self.COLORS = kmeans.cluster_centers_
        
        #save labels
        self.LABELS = kmeans.labels_
        
        #returning after converting to integer from float
        return self.COLORS.astype(int)

    def borderColor(self):
        # img = imutils.url_to_image(self.IMAGE)

        img = self.IMAGE.copy()

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        cols = np.zeros(3)

        for k in range(3):
            cols[k] = np.mean(img[0,:,k])+np.mean(img[-1,:,k])+np.mean(img[:,0,k])+np.mean(img[:,-1,k])
            print(cols[k])
            cols[k] = cols[k]/4

        return cols.astype(int)


if __name__=="__main__":
    img = 'https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg'
    clusters = 2
    dc = DominantColors(img, clusters) 
    dom_colors = dc.dominantColors()
    bor_colors = dc.borderColor()
    print(dom_colors)
    print(bor_colors)