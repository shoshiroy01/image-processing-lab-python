import cv2
import matplotlib.pyplot as plt

image1 = cv2.imread('img1.jpg')   

image_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)  
plt.axis('off')        
plt.title('Original Image')  
plt.show()             

print('Image shape:', image_rgb.shape)

pixel_value = image1[100, 100]  
print('Pixel value at (100,100):', pixel_value)

gray_image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  

print('Grayscale Image shape:', gray_image.shape)

plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.title('Gray Scale Image')
plt.show()

resize = cv2.resize(image_rgb, (300, 300))

plt.imshow(resize)
plt.axis('off')
plt.title('Resized Image (300 x 300)')
plt.show()

crop = image_rgb[100:400, 100:400]

plt.imshow(crop)
plt.axis('off')
plt.title('Cropped Image')
plt.show()

cv2.imwrite('gray_output.jpg', gray_image)

print('Grayscale image saved as gray_output.jpg')
