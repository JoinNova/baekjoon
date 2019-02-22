
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import shutil
import os
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image


# 이미지 파싱하기 : 29 * 50 사이즈
def image_crop( file_name , save_path):
    os.makedirs(os.path.join("./nums"))
    img = Image.open( file_name )
    (img_w, img_h) = img.size

    # 자를 개수 지정
    range_h = 29
    range_w = 50
    # 개당 사이즈
    grid_h = (img_h/range_h)
    grid_w = (img_w/range_w)

    # 이미지 저장하기
    idx = 0
    for h in range(range_h):
        for w in range(range_w):
            bbox = (w*grid_w, h*grid_h, (w+1)*(grid_w), (h+1)*(grid_h))
            crop_img = img.crop(bbox)
            fname = "{}.png".format("{0:04}".format(idx))
            save_name = save_path + fname
            crop_img.save(save_name)
            idx += 1
    return idx

# 이미지 중앙 부분 np.array로 변환
def clustering(cnt):
    x = np.array([])
    y = np.array([])
    z = np.array([])
    C = np.array([]) # color 입히기
    for i in range(cnt):
        file_path = './nums/{}.png'.format("{0:04}".format(i))
        jpg_img_arr = mpimg.imread(file_path)
        jpg_img_arr = jpg_img_arr[3:-3, 3:-3,] # 테두리 자르기
        x = np.append(x,np.mean(jpg_img_arr[:,:,0]))
        y = np.append(y,np.mean(jpg_img_arr[:,:,1]))
        z = np.append(z,np.mean(jpg_img_arr[:,:,2]))
        C = np.append(C,[np.mean(jpg_img_arr[:,:,0]), np.mean(jpg_img_arr[:,:,1]), np.mean(jpg_img_arr[:,:,2])])

    C = C.reshape(1450, 3)
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(x,y,z, c = C)
    plt.draw()
    fig.savefig('visualize_data.png', dpi = 100)

    df = pd.DataFrame(columns=('r','g','b'))
    idx = 0
    for c in C:
        df.loc[idx] = c
        idx += 1
    data_points = df.values
    kmeans = KMeans(n_clusters=10).fit(data_points)

    # 디레터리 만들기
    for i in range(10):
        os.makedirs(os.path.join("./nums/{}".format(i)))

    cnt_num = [0]*10
    print(len(kmeans.labels_))
    # 클러스터링 별로 파일 이동
    for i in range(cnt) :
        cnt_num[kmeans.labels_[i]] +=1
        file_name = '{}.png'.format("{0:04}".format(i))
        src = './nums/'
        dir = './nums/{}/'.format(kmeans.labels_[i])
        shutil.move(src+file_name, dir+file_name)
    print(cnt_num)

if __name__ == '__main__':
    cnt = image_crop('boj15636.jpg', './nums/') # file_name과 save_path
    clustering(cnt)

'''
l=[0,174,164,140,143,135,117,128,134,141]
i=0;total=0
for _ in l:
    total+=i*_
    i+=1
print(total)
'''
