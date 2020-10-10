from PIL import Image
import torch
import torch.utils.data as data
from torchvision import transforms

# 画像の前処理クラス
class ImageTransform():
    def __init__(self, mean, std):
        self.data_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean, std)
            ])

    def __call__(self, img):
        return self.data_transform(img)

# 画像のDatasetクラス。PyTorchのDatasetクラスを継承
class GAN_Img_Dataset(data.Dataset):
    def __init__(self, file_list, transform):
        self.file_list = file_list
        self.transform = transform
    
    #画像枚数を返す
    def __len__(self):
        return len(self.file_list)
    
    #前処理をした画像のTensor形式データを取得
    def __getitem__(self, index):
        img_path = self.file_list[index]
        img = Image.open(img_path) # [height][width]grayscale

        #画像の前処理
        img_transformed = self.transform(img)

        return img_transformed
