import os
from glob import glob
from tqdm import tqdm
from skimage import io
from stardist.models import StarDist2D
from csbdeep.utils import normalize
import numpy as np
from analyze import nuclear_morphology, make_figures


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "u20s-data")


def main():
    model = StarDist2D.from_pretrained("2D_versatile_fluo")

    img_paths = sorted(glob(os.path.join(DATA_DIR, "images", "*.tif")))

    for img_path in tqdm(img_paths):
        dir_path = os.path.join(
            DATA_DIR, "outputs", os.path.basename(img_path).split(".")[0]
        )
        os.makedirs(
            dir_path,
            exist_ok=True,
        )

        img = io.imread(img_path)

        labels, _ = model.predict_instances(normalize(img))  # type: ignore

        io.imsave(os.path.join(dir_path, "raw_image.tif"), img, check_contrast=False)
        io.imsave(
            os.path.join(dir_path, "labels.tif"),
            labels.astype(np.uint32),  # type: ignore
            check_contrast=False,
        )

    nuclear_morphology()
    make_figures()


if __name__ == "__main__":
    main()
