# Smoothing/blurring
>Used to remove noise from the image.

## Homogeneous filter
>It's the most simple filter, each output pixel is the mean of its kernel neighbors.

In image processing, a kernel, convolution matrix, or mask is a small matrix. It is used for blurring, sharpening, embossing, edge-detection and more.

In this filter, we have kernel:

$K = \frac{1}{K_{width}.K_{height}} \times the\ matrix\ that\ contains\ all\ 1s\ which\ has\ a\ dimension\ K_{width} \times K_{height}$

So if the we want to use a kernle of $5 \times 5$, then the kernel will look like this:

$K = \frac{1}{25} \times\ the\ 5 \times 5\ matrix\ containing\ all\ the\ 1s$

_In one-dimensional signals, images also can be filtered with various low-pass filters(LPF), high-pass filters(HPF)._

* _The LPF helps in removing the noise or blurring the image._

* _HPF helps in finding the edges in the images._




<p align="center">
&#9678; &#9678; &#9678;
</p>
