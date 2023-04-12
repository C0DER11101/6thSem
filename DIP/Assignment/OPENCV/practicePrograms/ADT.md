# Adaptive thresholding.
>It's a method where the threshold value is calculated for the smaller regions. This is not global for every pixel.

## adaptiveThreshold()

|Enumerator|   |
|:--------:|:-:|
|ADAPTIVE_THRESH_MEAN_C|the threshold value $T(x, y)$ is a mean of the $blockSize \times blockSize$ neighborhood of $(x, y)$ minus C|
|ADAPTIVE_THRESH_GAUSSIAN_C|the threshold value $T(x, y)$ is a weighted sum(cross correlation with a Gaussian window) of the $blockSize \times blockSize$ neighborhood of $(x, y)$ minus C. The default sigma(standard deviation) is used for the specified blockSize.|

<p align="center">
&#9678; &#9678; &#9678;
</p>
