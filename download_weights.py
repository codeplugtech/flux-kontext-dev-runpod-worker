from diffusers import FluxKontextPipeline
import torch

def fetch_pretrained_model(model_name, **kwargs):
    """
    Fetches a pretrained model from the HuggingFace model hub.
    """
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return  FluxKontextPipeline.from_pretrained(model_name, **kwargs)
        except OSError as err:
            if attempt < max_retries - 1:
                print(
                    f"Error encountered: {err}. Retrying attempt {attempt + 1} of {max_retries}..."
                )
            else:
                raise


def get_diffusion_pipelines():
    """
    Fetches the FLUX.1-dev-kontext pipeline from the HuggingFace model hub.
    """
    pipe = fetch_pretrained_model("black-forest-labs/FLUX.1-Kontext-dev",torch_dtype=torch.bfloat16)

    return pipe


if __name__ == "__main__":
    get_diffusion_pipelines()