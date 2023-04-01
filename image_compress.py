# import torch
# from PIL import Image
# import numpy as np
#
#
# jpg_quality_input = ("INT", {"default": 95,
#                "min": 50,
#                "max": 100,
#                "step": 1})
# class JpgConvertNode:
#     @classmethod
#     def INPUT_TYPES(s):
#         return {
#             "required": {
#                 "original_image": ("IMAGE",),
#                 "jpg_quality": jpg_quality_input
#             },
#
#         }
#
#     RETURN_TYPES = ("IMAGE",)
#     FUNCTION = "to_jpg"
#     CATEGORY = "trNodes"
#
#     def tensor_to_pil(self, img):
#         if img is not None:
#             i = 255. * img.cpu().numpy().squeeze()
#             img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
#         return img
#
#     def apply_color_correction(self, correction, original_image):
#
#         # https://github.com/AUTOMATIC1111/stable-diffusion-webui/blob/22bcc7be428c94e9408f589966c2040187245d81/modules/processing.py#L44
#
#         correction_target = cv2.cvtColor(np.asarray(correction.copy()), cv2.COLOR_RGB2LAB)
#
#         image = Image.fromarray(cv2.cvtColor(exposure.match_histograms(
#             cv2.cvtColor(
#                 np.asarray(original_image),
#                 cv2.COLOR_RGB2LAB
#             ),
#             correction_target,
#             channel_axis=2
#         ), cv2.COLOR_LAB2RGB).astype("uint8"))
#
#         image = blendLayers(image, original_image, BlendType.LUMINOSITY)
#         return image
#
#     def png_to_jpg(self, png_file, jpg_file, quality=75):
#         with Image.open(png_file) as img:
#             img = img.convert('RGB')
#             img.save(jpg_file, format='JPEG', quality=quality)
#     def color_correct(self, original_image, jpg_quality):
#         original_image = self.tensor_to_pil(original_image)
#
#
#         target_image = self.tensor_to_pil(target_image)
#
#
#         return (target_image,)
#
# NODE_CLASS_MAPPINGS = {
#     "JpgConvertNode": JpgConvertNode
# }
