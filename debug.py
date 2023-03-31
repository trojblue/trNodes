from PIL import Image
import numpy as np



def alpha_cutout(img, threshold=100, dist=5):
    arr = np.array(np.asarray(img))  # 获取图像数据，使用了numpy
    r, g, b, a = np.rollaxis(arr, axis=-1)

    mask = ((r > threshold)
            & (g > threshold)
            & (b > threshold)
            & (np.abs(r - g) < dist)  # 将接近白色背景的也替换掉
            & (np.abs(r - b) < dist)
            & (np.abs(g - b) < dist)
            )
    arr[mask, 3] = 0

    img = Image.fromarray(arr, mode='RGBA')  # 转换为图像格式
    return img

def cutout_csdn():

    threshold = 100
    dist = 5
    img = Image.open("img.png").convert('RGBA')  # 增加Alpha通道

    img = alpha_cutout(img, threshold, dist)


    img.show()


if __name__ == '__main__':
    cutout_csdn()
    # image = "img.png"
    # do_cutout(image)
