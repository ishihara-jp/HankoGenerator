import os
import glob
import numpy as np
import skimage.util
import skimage.io
import skimage.transform

out_size = 64 # 最終出力サイズ（横、縦）
img = skimage.io.imread('data/low/hanko.jpg')
print(img.shape)
# (3307, 2340, 3)
#ここで割り切れない中途半端なサイズだとエラーが出るので、リサイズ
img_ = skimage.transform.resize(img, (64*14, 64*10), anti_aliasing=True)
img_gray = skimage.color.rgb2gray(img_) #グレースケール変換
print(img_gray.shape)
#(3307, 2340)
blocks = skimage.util.view_as_blocks(img_gray, (img_gray.shape[0]//14, img_gray.shape[1]//10)).squeeze()
print(blocks.shape)
# (14, 10, 64, 64)
path_to_out = 'data/low/hanko/' #出力先
os.makedirs(path_to_out, exist_ok=True) #無ければ作成
file_list = glob.glob(path_to_out + "hanko*jpg") #存在チェック＆削除
for f in file_list: os.remove(f)
idx = 0
for i in range(14):
    for j in range(10):
        skimage.io.imsave(path_to_out + 'hanko{:0=3}.jpg'.format(idx), blocks[i,j])
        idx += 1
print("fin.")