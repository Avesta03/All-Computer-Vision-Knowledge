import cv2 as cv

img = cv.imread('/Users/avestaafshari-mehr/Desktop/cat.jpg') 
# Adding _large[.jpg] makes image larger, but note OpenCV has no in-built way of dealing with images > than your computer screen.

cv.imshow('Cat', img)

cv.waitKey(0) # Keyboard binding function - waits for a specific delay/time in ms for a key to be pressed.
# {0 waits infinite time for a key to be pressed}
