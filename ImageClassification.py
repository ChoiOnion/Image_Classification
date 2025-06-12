import cv2
import numpy as np
import os
from google.colab.patches import cv2_imshow

src1 = cv2.imread('/content/sample/a_data.jpg')
img1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
img1 = cv2.resize(img1, (1200, 900))

siftF = cv2.SIFT_create()
kp1, des1 = siftF.detectAndCompute(img1, None)

path = '/content/data/'
dataset = [f for f in os.listdir(path) if f.endswith('.jpg')]

similarities = []

for data in dataset:
    src2 = cv2.imread(os.path.join(path, data))
    img2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)
    img2 = cv2.resize(img2, (1200, 900))

    kp2, des2 = siftF.detectAndCompute(img2, None)
    
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(des1, des2)

    distances = [m.distance for m in matches]
    similarity = np.mean(distances) if distances else float('inf')
    similarities.append((data, similarity))

similarities.sort(key=lambda x: x[1])

for i, (data, similarity) in enumerate(similarities[:5], 1):
    print(f"{i}. {data}: 유사도 = {similarity}")
    # 이미지 출력
    img = cv2.imread(os.path.join(path, data))
    cv2_imshow(img)

cv2.waitKey()
cv2.destroyAllWindows()
