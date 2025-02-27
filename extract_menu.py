import os
import json
import pdfplumber
import pytesseract
from PIL import Image
import re
import ollama  # Using LLaMA 2 for better text structuring

# Set path to Tesseract-OCR (Update this based on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_image(image_path):
    """Extracts text from an image using Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

def parse_menu_with_llama(text):
    """Uses LLaMA 2 (Ollama) to structure extracted text into a JSON menu format, ensuring a valid response."""
    prompt = f"""
    Given the following restaurant menu text, return a JSON array where each object has:
    - "name": (dish name)
    - "description": (short description)
    - "ingredients": (list of ingredients)
    - "price": (if available, otherwise set null)
    - "is_vegetarian": (true/false based on dish)

    Output **ONLY** JSON without any extra text.

    Text:
    {text}
    """

    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])

    # Extract LLaMA response
    content = response.get("message", {}).get("content", "").strip()

    # Debugging: Print full response
    print("LLaMA Raw Output:\n", content)

    # Try to extract JSON using regex (handles extra text)
    match = re.search(r"\[\s*\{.*\}\s*\]", content, re.DOTALL)
    
    if match:
        json_text = match.group(0)  # Extract only JSON part
        try:
            return json.loads(json_text)  # Parse JSON
        except json.JSONDecodeError:
            print("⚠️ Error: Extracted JSON is still invalid!")
            return []
    else:
        print("⚠️ Error: No JSON detected in LLaMA's response!")
        return []
def extract_menu(file_path):
    """Extracts menu from a PDF or image and structures it into a JSON format."""
    print(f"Processing file: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.lower().endswith((".png", ".jpg", ".jpeg")):
        text = extract_text_from_image(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or Image.")

    menu_data = parse_menu_with_llama(text)

    with open("menu.json", "w", encoding="utf-8") as json_file:
        json.dump(menu_data, json_file, indent=4)

    print("✅ Menu extracted and saved to menu.json")
    return menu_data

# Example usage:
if __name__ == "__main__":
    file_path = input("Enter the menu file path (PDF or image): ").strip()
    extract_menu(file_path)
