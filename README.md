# Fluorescent nuclei image analysis
Detecting and segmenting nuclei in fluorescence microscopy images is a very common and important workflow, allowing for counting nuclei, measuring cell density in a tissue, and quantifying nuclear morphology. This repository is a demonstration of a nuclear segmentation using pre-trained artificial intelligence models, conversion to data tabular data, and subsequent data analysis.

## Raw data
The raw data consists of 200 16-bit TIFF images from U2OS cells, each with a field of view containing numerous nuclei. Each image represents the DNA channel and shows Hoechst-stained nuclei. Six sample images from the dataset are shown below. Each bright blob is a single cell nucleus.

![image](https://github.com/user-attachments/assets/a8b3a4d7-214c-4d00-afe1-9e865ddb7447)

## Nuclear segmentation
While digital image processing using common filters, edge detectors, and other classic algorithms can be used for segmentation, one StarDist's pre-trained models is able to very quickly and accurately produce nuclei labels.

```
┌─────────────────────────────────┬────────────────┬───────┬────────┬──────────────┬────────────┬──────────┐
│ filename                        ┆ img_total_area ┆ label ┆ area   ┆ aspect_ratio ┆ perimeter  ┆ solidity │
│ ---                             ┆ ---            ┆ ---   ┆ ---    ┆ ---          ┆ ---        ┆ ---      │
│ str                             ┆ i64            ┆ i64   ┆ f64    ┆ f64          ┆ f64        ┆ f64      │
╞═════════════════════════════════╪════════════════╪═══════╪════════╪══════════════╪════════════╪══════════╡
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 1     ┆ 835.0  ┆ 0.631725     ┆ 110.325902 ┆ 0.97093  │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 2     ┆ 1495.0 ┆ 0.684223     ┆ 149.296465 ┆ 0.96952  │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 3     ┆ 756.0  ┆ 0.829363     ┆ 100.911688 ┆ 0.978008 │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 4     ┆ 688.0  ┆ 0.74359      ┆ 97.740115  ┆ 0.967651 │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 5     ┆ 1090.0 ┆ 0.922205     ┆ 121.63961  ┆ 0.976703 │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 6     ┆ 760.0  ┆ 0.905834     ┆ 101.740115 ┆ 0.970626 │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 7     ┆ 1081.0 ┆ 0.774601     ┆ 122.953319 ┆ 0.972997 │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 8     ┆ 1370.0 ┆ 0.811672     ┆ 138.710678 ┆ 0.968883 │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 10    ┆ 803.0  ┆ 0.675087     ┆ 108.083261 ┆ 0.961677 │
│ IXMtest_A02_s1_w1051DAA7C-7042… ┆ 361920         ┆ 11    ┆ 834.0  ┆ 0.55059      ┆ 113.497475 ┆ 0.964162 │
└─────────────────────────────────┴────────────────┴───────┴────────┴──────────────┴────────────┴──────────┘
```
