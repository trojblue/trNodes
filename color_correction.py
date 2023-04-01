import torch
from PIL import Image
import numpy as np
import cv2
from skimage import exposure
from blendmodes.blend import blendLayers, BlendType

class ColorCorrectionNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TARGET_IMAGE": ("IMAGE",),
                "reference": ("IMAGE",),
                "inverse selection": (["False", "True"],),
            },

        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "color_correct"
    CATEGORY = "trNodes"

    def tensor_to_pil(self, img):
        if img is not None:
            i = 255. * img.cpu().numpy().squeeze()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def apply_color_correction(self, correction, original_image):

        # https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/22bcc7be428c94e9408f589966c2040187245d81/modules/processing.py#L44

        correction_target = cv2.cvtColor(np.asarray(correction.copy()), cv2.COLOR_RGB2LAB)

        image = Image.fromarray(cv2.cvtColor(exposure.match_histograms(
            cv2.cvtColor(
                np.asarray(original_image),
                cv2.COLOR_RGB2LAB
            ),
            correction_target,
            channel_axis=2
        ), cv2.COLOR_LAB2RGB).astype("uint8"))

        image = blendLayers(image, original_image, BlendType.LUMINOSITY)
        return image

    def color_correct(self, original_image, target_image, inverse_selection="False"):
        original_image = self.tensor_to_pil(original_image)
        target_image = self.tensor_to_pil(target_image)

        if inverse_selection == "False":
            corrected_image = self.apply_color_correction(target_image, original_image)
        else:
            corrected_image = self.apply_color_correction(original_image, target_image)

        # convert to tensor
        corrected_image = corrected_image.convert('RGB')
        out_image = np.array(corrected_image).astype(np.float32) / 255.0
        out_image = torch.from_numpy(out_image).unsqueeze(0)

        return (out_image,)

