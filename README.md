# **Search Text in Images or Find Text in Images**

This script enables the user to extract text from images using Optical Character Recognition (OCR) and search for specific text patterns within the extracted text. It processes all images in a specified directory, identifies matches, and exports the results to a CSV file.

## **Features**

* **Text Extraction**: Uses the `EasyOCR` library to extract text from images.  
* **Text Search**: Searches for predefined strings in the extracted text.  
* **Batch Processing**: Processes all images in a given directory.  
* **CSV Output**: Saves the results, including filenames and matching texts, into a CSV file.

## **Requirements**

Make sure you have the following libraries installed before running the script:

* `easyocr`  
* `Pillow` (Python Imaging Library)  
* `pandas`  
* `tqdm`

You can install these packages using pip:

bash

Copy code

`pip install easyocr pillow pandas tqdm`

## **How to Use**

1. **Set Up the Directory**:  
   * Place all the images you want to process in a directory.  
   * Update the `directory` variable in the script with the path to your image directory.  
2. **Predefine Search Texts**:  
   * Add the text strings you want to search for in the `texts` list.  
3. **Run the Script**:

Execute the script in your Python environment:  
bash  
Copy code  
`python main.py`

*   
4. **Check the Output**:  
   * After running, the script generates a CSV file named `output.csv` containing the results:  
     * **Filename**: Name of the image file.  
     * **Matching\_Text**: The text string that was matched.  
     * **Extracted\_Text**: Full text extracted from the image.

## **Output Format**

The CSV file (`output.csv`) will have the following structure:

| Filename | Matching\_Text | Extracted\_Text |
| ----- | ----- | ----- |
| image1.jpg | test1 | This is a test1 text |
| image2.png | test2 | Sample text test2 |

## **Error Handling**

* If the script encounters an error while processing an image, it prints the error message and continues to the next image. This ensures the script doesn't stop due to a single problematic file.

## **Customization**

**Languages**: Update the `reader` initialization line to support additional languages. For example:  
python  
Copy code  
`reader = easyocr.Reader(['en', 'fr'])  # English and French`

*   
* **File Extensions**: Modify the `if filename.endswith(...)` line to include additional image formats if needed.

## **Example**

python

Copy code

`# Directory containing images`

`directory = r'D:\Images'`

`# Text to search for`

`texts = ["example", "sample", "demo"]`

`# Output file`

`output.csv`

Run the script, and it will process all images in `D:\Images`, searching for "example", "sample", or "demo" in the extracted text and saving the results to `output.csv`.

