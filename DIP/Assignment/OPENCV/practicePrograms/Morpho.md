# Morphological transformations
>These are some simple operations based on the image shape. They are nomally performed on a binary image.

_When we perform morphological transformations two things are required:_
1. Original image.
2. A structuring element(kernel).

_A kernel tells you how to change the value of any given pixel by combining it with different amounts of the neighbouring pixels._

### The kernel
_A kernel is a matrix of odd size(3, 5, 7) that applied on the image._

There are two types of morphological transformations:

1. Erosion
2. Dilation.

### Erosion
* Erodes away the boundaries of the foreground object.
* Used to diminish the features of an image.


#### Working
1. A kernel is convolved with the image.
2. A pixel in the original image is considered 1 only if all the pixels under the kernel are 1, otherwise, it is eroded(made to zero).
3. Thus all the pixels near the boundary will be discarded depending upon the size of the kernel.
4. So the thickness or the foreground of the image decreases or simply the white region decreases in the image.


### Dilation
* Increases the object area.
* Used to accentuate features.


#### Working
1. A kernel is convolved with the image.
2. A pixel element in the original image is 1 if at least one pixel under the kernel is 1.
3. It increases the white region in the image or the size of the foreground object increases.


<p align="center">
&#9678; &#9678; &#9678;
</p>
