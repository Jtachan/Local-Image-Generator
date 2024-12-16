"""Script to generate images locally."""
import argparse
import torch
from diffusers import StableDiffusion3Pipeline

large_model = "stabilityai/stable-diffusion-3.5-large"


def command_line_interface():
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Local image generator using StableDiffusion."
    )
    parser.add_argument(
        "--cpu", action="store_true", help=""
    )


if __name__ == '__main__':
    pipe = StableDiffusion3Pipeline.from_pretrained(large_model,
                                                    torch_dtype=torch.bfloat16)
    pipe.enable_attention_slicing()
    pipe = pipe.to("cuda")

    prompt = (
        "A wok with stir-fry broccoli stems in a water-color art style. The broccoli"
        " must also be in the wok with garlic cloves, carrots and sesame seeds. All "
        "these vegetables have been cooked together and the final image must be nice "
        "to the eye, as well as inviting to try the dish."
    )

    results = pipe(
        prompt,
        num_inference_steps=20,
        guidance_scale=3.5,
        height=512,
        width=512
    )

    images = results.images

    # Save or display the images
    for i, img in enumerate(images):
        img.save(f"image_{i}.png")  # Save each image
