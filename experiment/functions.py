import os
import sonicstv
from PIL import Image as PILImage
from pysstv.color import MartinM1 as PySSTVMartinM1
import cv2


def saveSSTVAudio(
    baked_image: sonicstv.BakedImage, path: str, *, should_overwrite_if_existed: bool = False
):
    # # Check if given path is file, and make dir if necessary.
    if not should_overwrite_if_existed and os.path.isfile(path):
        raise RuntimeError(f"[ERR ] Cannot write to path `{path}` since it already existed.")
    os.makedirs(os.path.dirname(path), exist_ok=True)

    pil_image = PILImage.fromarray(cv2.cvtColor(baked_image.image, cv2.COLOR_BGR2RGB))
    sstv_sound = PySSTVMartinM1(pil_image, 48000, 16)
    sstv_sound.vox_enabled = True  # enable prefix sound
    sstv_sound.write_wav(path)
