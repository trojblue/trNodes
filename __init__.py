import custom_nodes.trNodes.image_layering as image_layering
import custom_nodes.trNodes.color_correction as color_correction
import custom_nodes.trNodes.model_router as model_router
import custom_nodes.trNodes.shortcut_nodes as shortcut_nodes


NODE_CLASS_MAPPINGS = {
    "trLayering": image_layering.Layering,                      # Layering
    "trColorCorrection": color_correction.ColorCorrectionNode,  # ColorCorrectionNode
    "trRouter": model_router.ModelRouterPlugin,          # ModelRouterPlugin
    "trRouterLonger": model_router.LongerModelRouterPlugin,  # ModelRouterPlugin
}
