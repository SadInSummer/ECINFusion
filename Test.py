from PIL import Image
import numpy as np
import os
import torch
import cv2
import time
import imageio

import torchvision.transforms as transforms
from Networks.net import Final_MODEL as net




os.environ['CUDA_VISIBLE_DEVICES'] = '0'

device = torch.device('cuda:0')


model = net()

model_path = "./models/model_200.pth"
use_gpu = torch.cuda.is_available()
print(use_gpu)

if use_gpu:

    model = model.cuda()
    model.cuda()

    model.load_state_dict(torch.load(model_path))

else:

    state_dict = torch.load(model_path, map_location='cpu')

    model.load_state_dict(state_dict)


def fusion():

    for num in range(1):
        tic = time.time()

        path1 = './PET.bmp'
        path2 = './MRI.bmp'#MRI

        img1 = Image.open(path1).convert('L')
        img2 = Image.open(path2).convert('L')
        # img1 = cv2.imread(path1,cv2.IMREAD_GRAYSCALE)
        # img2 = cv2.imread(path2,cv2.IMREAD_GRAYSCALE)

        img1_org = img1
        img2_org = img2

        tran = transforms.Compose([transforms.ToTensor()])
        # tran = transforms.ToTensor()

        img1_org = tran(img1_org)
        img2_org = tran(img2_org)
        input_img = torch.cat((img1_org, img2_org), 0).unsqueeze(0)
        img1_org = img1_org.unsqueeze(0)
        img2_org = img2_org.unsqueeze(0)
        if use_gpu:
            input_img = input_img.cuda()
            img1_org = img1_org.cuda()
            img2_org = img2_org.cuda()
        else:
            input_img = input_img
            img1_org = img1_org
            img2_org = img2_org

        model.eval()
        out = model(img1_org,img2_org)

        d = np.squeeze(out.detach().cpu().numpy())
        result = (d* 255).astype(np.uint8)
        # imageio.imwrite('./MP_test/{}.bmp'.format(num),result)
        #cv2.imwrite('./{}.bmp'.format(num),result)
        imageio.imwrite('./MP_test/1.bmp', result)


        toc = time.time()
        print('end  {}{}'.format(num // 10, num % 10), ', time:{}'.format(toc - tic))



if __name__ == '__main__':

    fusion()
