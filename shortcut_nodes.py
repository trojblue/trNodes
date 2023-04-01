# import numpy as np
# from PIL import Image
# from PIL.PngImagePlugin import PngInfo
# import json
from nodes import VAEDecode, SaveImage
import os


"""
NOT WORKING
"""
class SaveVAEImageNode():
    """
    DECODE and show Image sample; Also export the image as an optional param to be saved

    Class methods
    -------------
    INPUT_TYPES (dict):
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`):
        The type of each element in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """

    def __init__(self, device="cpu"):
        self.device = device
        self.decode_handler = VAEDecode()
        self.image_handler = SaveImage()

    RETURN_TYPES = ()
    FUNCTION = "do_decode_and_preview"
    CATEGORY = "trNodes"
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "samples": ("LATENT",),
            "vae": ("VAE",)}
        }

    def _do_decode(self, vae, samples):
        return (vae.decode(samples["samples"]),)

    def _do_save_image(self, image, filename_prefix="ComfyUI", prompt=None, extra_pnginfo=None):
        return self.image_handler.save_images(image, filename_prefix, prompt, extra_pnginfo)

    def do_decode_and_preview(self, vae, samples, filename_prefix="ComfyUI", prompt=None, extra_pnginfo=None):
        image = self._do_decode(vae, samples)
        ui_out = self._do_save_image(image, filename_prefix, prompt, extra_pnginfo)
        return (ui_out, image)



