from tqdm import tqdm
import os
from glob import glob
from skimage.segmentation import clear_border
from skimage import io
from skimage.measure import regionprops
import polars as pl
from joblib import Parallel, delayed
import seaborn as sns
import matplotlib.pyplot as plt

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
                "aspect_ratio": prop.axis_minor_length / prop.axis_major_length,
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


def make_figures(data_dir: str = DATA_DIR):
    df = pl.read_csv(os.path.join(DATA_DIR, "nuclear_morphology.csv"))
    print(df.head(10))

    sns.set_theme(style="whitegrid")
    sns.boxplot(
        x=df["area"], showfliers=False, color=sns.color_palette("pastel")[0]
    ).set_xlabel("area (px)")
    plt.savefig(os.path.join(DATA_DIR, "area_boxplot.png"), dpi=300)

    plt.clf()
    sns.boxplot(
        x=df["aspect_ratio"], showfliers=False, color=sns.color_palette("pastel")[1]
    ).set_xlabel("aspect ratio")
    plt.savefig(os.path.join(DATA_DIR, "aspect_ratio_boxplot.png"), dpi=300)

    plt.clf()
    sns.boxplot(
        x=df["solidity"], showfliers=False, color=sns.color_palette("pastel")[2]
    ).set_xlabel("solidity")
    plt.savefig(os.path.join(DATA_DIR, "solidity_boxplot.png"), dpi=300)


if __name__ == "__main__":

    make_figures()
