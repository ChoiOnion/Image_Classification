# Image_Classification
openCV를 이용하여 이미지를 분류하는 코드


src1에 기준이 되는 이미지를 로드하고 img1에 그레이스케일로 저장한다.
SIFT 객체에 img1의 특징점과 디스크립터를 추출하고, dataset에 저장된 사진들과의 유사도를 저장하여 가장 유사한 이미지 상위 5개를 출력한다.


bfMatcher와 FlannBasedMatcher 두 가지를 실행해 본 결과, 영상 검색 결과에는 큰 차이가 없었으나 처리 속도 면에서 FlannedBasedMatcher가 훨씬 빨랐다.

bfMatcher
![image](https://github.com/user-attachments/assets/a0931027-e628-4af6-ac74-58bd729aea5c)
![image](https://github.com/user-attachments/assets/aa99aa85-8fa7-476e-9364-8408b85bd710)
![image](https://github.com/user-attachments/assets/3d1e30dc-709f-489a-8700-464d1600ec02)


![image](https://github.com/user-attachments/assets/00391e36-992a-40e6-ba7a-cf272a4c57cf)
![image](https://github.com/user-attachments/assets/59bc7b19-dd89-451a-b748-728293532b50)
![image](https://github.com/user-attachments/assets/e3072c8f-6165-4988-be67-de51709bbede)


FlannBasedMatcher
![image](https://github.com/user-attachments/assets/083cf046-7b8a-4c5b-8c09-96e3a6fbd311)
![image](https://github.com/user-attachments/assets/a1f9f329-511a-4a11-8ec9-ac3717662b96)
