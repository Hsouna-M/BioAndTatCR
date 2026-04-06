import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageOps
from skimage.metrics import structural_similarity as compare_ssim
from skimage import feature

def preprocess(image_path: str) -> np.ndarray:
    img = Image.open(image_path).convert("L")

    img = img.resize((300, 300))
    
    # egalisation histogram
    img = ImageOps.equalize(img)
    
    img_array = np.array(img)
    
    # 5. Binarization with threshold = 128
    _, binary = cv2.threshold(img_array, 128, 255, cv2.THRESH_BINARY)
    
    # 6. Edge extraction using FIND_EDGES filter
    img_pil = Image.fromarray(binary)
    edges = img_pil.filter(ImageFilter.FIND_EDGES)
    
    # Convert back to numpy array
    edges_array = np.array(edges)
    
    return edges_array

def Testing():
	img = Image.open("fingerprint.png").convert("L").resize((300,300))
	img_array= np.array(img)
	print(img_array)
	img = ImageOps.equalize(img)
	secode_array = np.array(img)
	print(secode_array)
	hist = img.histogram()
	print()
	print(hist)

# Check Point: 
# Im trying to understand how can you equilize an image object with this 
# img = ImageOps.equalize(img)
Testing()

