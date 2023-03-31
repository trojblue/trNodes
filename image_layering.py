import torch
import numpy as np
from PIL import Image
import subprocess
import sys
try:
    import blend_modes
except ModuleNotFoundError:
    # install pixelsort in current venv
    subprocess.check_call([sys.executable, "-m", "pip", "install", "blend-modes"])
    import blend_modes

import torch
import numpy as np
from PIL import Image

class Layering:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "base_image": ("IMAGE",),
                "add_layer1": ("IMAGE",)},
            "optional": {
                "add_layer2": ("IMAGE", {"default": None}),
                "add_layer3": ("IMAGE", {"default": None}),
                "key_color": ("TUPLE", {"default": (255, 255, 255)}),
                # "alpha1": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                # "alpha2": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                # "alpha3": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "apply_blend"
    CATEGORY = "trojblue_folder"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def alpha_cutout(self, img, threshold=80, dist=10):
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


    def create_transparent_image(self, image, key_color, alpha):
        transparent_image = Image.new('RGBA', image.size, (0, 0, 0, 0))
        for x in range(image.width):
            for y in range(image.height):
                pixel = image.getpixel((x, y))
                if pixel != key_color:
                    transparent_image.putpixel((x, y), (*pixel[:3], int(255 * alpha)))
        return transparent_image


    def apply_blend(self, base_image, add_layer1, alpha1, add_layer2=None, alpha2=1.0, add_layer3=None, alpha3=1.0, key_color=(255, 255, 255)):
        base_image = self.tensor_to_pil(base_image[0]).convert('RGBA')
        add_layers = [(add_layer1, alpha1), (add_layer2, alpha2), (add_layer3, alpha3)]
        add_layers = [(self.tensor_to_pil(layer[0]).convert('RGBA'), alpha) for layer, alpha in add_layers if layer is not None]

        for image, alpha in add_layers:
            image = image.resize(base_image.size, Image.ANTIALIAS)
            transparent_image = self.alpha_cutout(image)
            base_image = Image.alpha_composite(base_image, transparent_image)

        base_image = base_image.convert('RGB')

        # convert to tensor
        out_image = np.array(base_image).astype(np.float32) / 255.0
        out_image = torch.from_numpy(out_image).unsqueeze(0)

        return (out_image,)

NODE_CLASS_MAPPINGS = {
    "Layering": Layering,
}



