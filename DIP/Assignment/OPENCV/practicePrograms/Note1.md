# How to read, write and show images in OpenCV
> OpenCV $\rightarrow$ Open source Computer Vision.

```python
cv2.imread('imagename', Flag);
```

# Flag(The second argument of imread())

There are 3 flags:

|flag|integer value|description|
|:--:|:-----------:|:---------:|
|cv2.IMREAD_COLOR|1|Loads a color image|
|cv2.IMREAD_GRAYSCALE|0|Loads image in grayscale mode|
|cv2.IMREAD_UNCHANGED|-1|Loads image as such including alpha channel|

# Storing the image in the form of matrix in another variable

For that, simply write:
```python
img=cv2.imread('imagename', Flag);
```

`print(img)` will print the grayscale values of each pixel of that image.

# Displaying an image

```python
cv2.imshow('imagename', img);
```

This method displays the image.

$1^{st}$ argument: $\rightarrow$ title of the window in which the image will be displayed.
$2^{nd}$ argument: $\rightarrow$ the image variable in which the image was stored in the form of matrix(in our case, `img`).

**Note**: _It displays the image only for 1 ms._

# Making the image stay for certain amount of time.

```python
cv2.waitKey(time in milliseconds);
```
This method keeps the image on the screen for the specified amount of milliseconds.

```python
cv2.waitKey(5000);
```
Here, it keeps the image on the screen for 5 seconds.

```python
cv2.waitKey(0);
```
This will keep the image on the screen until a key is pressed.

`waitKey()` returns the **ASCII** value of the key pressed.

Also, in 64-bit machines, it is recommended AND the mask `0xFF` with `cv2.waitKey();` as shown below:

```python
cv2.waitKey(0) & 0xFF;
```

# Destroying the window
```python
cv2.destroyAllWindows();
```
This method simply destroys all the windows which we had created.

# Writing an image to a file
```python
cv2.imwrite('name of new file', image variable);
```
$1^{st}$ argument $\rightarrow$ Name of the new image file(can be any name).
$2^{nd}$ argument $\rightarrow$ image variable to which we had saved the read image(using `imread()`).

<p align="center">
&#9678; &#9678; &#9678;
</p>
