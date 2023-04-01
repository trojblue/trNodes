
# comfy-custom-nodes

custom node modules for ComfyUI

## Installation

1. git clone this repo under `ComfyUI/custom_nodes`

2. install dependencies:

```bash
cd python_embeded
./python.exe -m pip install -r opencv-python scikit-image blendmodes
```

## Nodes

image_layering:
- Adds 1-3 layers of image on top of one another; will remove white background and use it as transparent layers

color_correction:
- Adjusts the color of the target image according to another image; ported from stable diffusion WebUI



## External Nodes

[WAS Node suite](https://civitai.com/models/20793/was-node-suites-comfyui) 
- Image Blend by Mask: Blend two images by a mask (but all nodes are very good)

and even look this: https://civitai.com/models/24869/comfyui-custom-nodes-by-xss