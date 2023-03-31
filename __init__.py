import custom_nodes.comfy_nodes_trojblue.image_layering as image_layering
import custom_nodes.comfy_nodes_trojblue.color_correction as color_correction


NODE_CLASS_MAPPINGS = {
    "layering": image_layering.Layering,                      # Layering
    "color_correction": color_correction.ColorCorrectionNode,  # ColorCorrectionNode

}
