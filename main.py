import os
import easyocr
from PIL import Image
import pandas as pd
from tqdm import tqdm

# Initialize the EasyOCR reader (supports multiple languages)
reader = easyocr.Reader(['en'])

# Set the directory where your images are stored
directory = r'D:\Images'
texts = ["test1", "test2", "test3"]

# Prepare a list to store the results
data = []

# Loop through the directory and process each image with a progress bar
for filename in tqdm(os.listdir(directory), desc="Processing images"):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(directory, filename)
        try:
            # Open image
            img = Image.open(image_path)

            # Use EasyOCR to extract text
            extracted_text = reader.readtext(image_path, detail=0)  # detail=0 returns only the text
            extracted_text = " ".join(extracted_text)

            # Search for matching texts in the extracted text
            for text in texts:
                if text in extracted_text:
                    data.append({
                        'Filename': filename,
                        'Matching_Text': text,
                        'Extracted_Text': extracted_text
                    })
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Create a DataFrame from the data list
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file with UTF-8 encoding
df.to_csv('output.csv', index=False, encoding='utf-8')