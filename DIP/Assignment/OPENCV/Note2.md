# [1.py]()
**Syntax:**
```python
cv2.imread('<imagename>', Flags);
```
this function basically read an image from a file.

The imread() function takes two arguments:

1. Image name.
2. Flag $\rightarrow$ specifies the way an image should be read.

## Flags

|Flag|Integer Value|Description|
|:--:|:-----------:|:---------:|
|cv2.IMREAD_COLOR|1|Loads a color image|
|cv2.IMREAD_GRAPYSCALE|0|Loads image in grayscale mode|
|cv2.IMREAD_UNCHANGED|-1|Loads image as such including alpha channel|

`img` is a variable that will store the grayscale values of the image in the form of a matrix.

## More

```python
print(img)
```
prints the matrix of grayscale values.

```python
cv2.imshow('Happyfish.jpg', img);
```
displays the image for $1ms$; so to keep the window up for some time we will use a function:

```python
cv2.waitKey();
```
it takes numeric argument representing the number of milliseconds. If the argument is 0 then the window will stay up until you press any key.

This function returns the ascii value of the character pressed in your keyboard.

In a 64-bit machine, it is recommended that the mask `0xFF` must be AND-ed with `cv2.waitKey()` as shown below:
```python
cv2.waitKey(0) & 0XFF
```

```python
cv2.imwrite('HappyfishCopied.jpg', img);
```
writes the image store in matrix form in `img` into a new file named `HappyfishCopied.jpg`.

```python
cv2.destroyAllWindows();
```
destroys the window in which we displayed the image.
