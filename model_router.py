class ModelRouterPlugin:
    """
    An example node

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

    FUNCTION = "execute"
    CATEGORY = "trNodes"
    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "CONDITIONING", "CONDITIONING")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "conditioning1": ("CONDITIONING",),
                "conditioning2": ("CONDITIONING",),
            }
        }

    def execute(self, model=None, clip=None, vae=None, conditioning1=None, conditioning2=None):
        print(model, clip, vae)

        return model, clip, vae, conditioning1, conditioning2




class LongerModelRouterPlugin:
    """
    An example node

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

    FUNCTION = "execute"
    CATEGORY = "trNodes"
    RETURN_TYPES = ("MODEL", "CLIP", "VAE", "CONDITIONING", "IMAGE", "LATENT", "CONDITIONING")

    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.
        """
        return {
            "required": {},
            "optional": {
                "model": ("MODEL",),
                "clip": ("CLIP",),
                "vae": ("VAE",),
                "conditioning1": ("CONDITIONING",),
                "image": ("IMAGE",),
                "latent": ("LATENT",),
                "conditioning2": ("CONDITIONING",),
            }
        }


    def execute(self, model=None, clip=None, vae=None, conditioning1=None, image=None, latent=None, conditioning2=None):

        print(model, clip, vae)
        return (model, clip, vae, conditioning1, image, latent, conditioning2)

