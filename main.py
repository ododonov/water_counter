import os, cv2, pytesseract

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "counter.jpg")

img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Распознавание текста
custom_config = r'--oem 3 --psm 7 outputbase digits'
text = pytesseract.image_to_string(img, config=custom_config)

print("Распознанное значение:", text.strip())