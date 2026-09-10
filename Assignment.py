import cv2
import matplotlib.pyplot as plt

img_bgr = cv2.imread('img1.jpg') 

if img_bgr is None:
    print("Error: Could not load image. Check the file path.")
else:
    
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    height, width, channels = img_bgr.shape
    print(f"Image Dimensions: {height}x{width} with {channels} color channels")

    pixel_val = img_rgb[0, 0] 
    print(f"RGB value at top-left pixel (0,0): {pixel_val}")

    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    print("\nFirst 3x3 pixel grid (Grayscale numeric values):")
    print(img_gray[:3, :3])

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title('RGB Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.show()