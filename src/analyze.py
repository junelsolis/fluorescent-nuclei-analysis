from tqdm import tqdm
import os
from glob import glob
from skimage.segmentation import clear_border
from skimage import io
from skimage.measure import regionprops
import polars as pl
from joblib import Parallel, delayed

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "u20s-data", "outputs")


def __process_label_img(label_path: str):
    label_img = io.imread(label_path)
    label_img = clear_border(label_img)

    props = regionprops(label_img)
    fname = os.path.basename(os.path.dirname(label_path))

    data = []
    for prop in props:
        data.append(
            {
                "filename": fname,
                "img_total_area": label_img.size,
                "label": prop.label,
                "area": prop.area,
                "aspect_ratio": prop.axis_major_length / prop.axis_minor_length,
                "perimeter": prop.perimeter,
                "solidity": prop.solidity,
            }
        )

    return data


def nuclear_morphology(data_dir: str = DATA_DIR):
    label_paths = glob(os.path.join(DATA_DIR, "*", "labels.tif"))

    data = Parallel(n_jobs=-1)(
        delayed(__process_label_img)(label_path) for label_path in tqdm(label_paths)
    )

    data = [item for sublist in data for item in sublist]  # type: ignore

    df = pl.DataFrame(data)
    df.write_csv(os.path.join(DATA_DIR, "nuclear_morphology.csv"))


if __name__ == "__main__":
    nuclear_morphology()
