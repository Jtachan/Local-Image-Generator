# Local-Image-Generator

AI image generator prepared to be run locally using hugging-face.

## Setup

### Pre-requirements

- **Python version** Due to Pytorch requirements, the version must be 3.9-3.12.
- **CUDA** (for Nvidia GPU):<br>Follow the instructions of the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) to install CUDA.
- **[Hugging Face](https://huggingface.co/)**: Some steps are required:
  1. _Account_: Create an account if you don't have one already.
  2. _Stable Diffusion License_: The model [stable-diffusion-3.5-large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) will be used as the image generator. When the page of this model is open for the first time, the license agreement will appear to grant us access.
  3. _Token_: Go to ["Access Tokens"](https://huggingface.co/settings/tokens) and create a token with the access of reading the content of public repositories.

> Note: The CUDA installation is only required when not running the model with the CPU.

### Installation

First, install the **python requirements** with the following command:

```bash
pip install -r requirements.txt
```

Then, install **Pytorch**. Go to the [_Start Locally_](https://pytorch.org/get-started/locally/) page.
There, set all the specifications of you computer, copy the pip-command and run it.

> Note: It is important Pytorch is the last installed package.
 
### Before running

**Log into** your hugging-face account with the following command:

```bash
huggingface-cli login
```

This 
