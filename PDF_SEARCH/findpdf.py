import os
import easyocr
from pdf2image import convert_from_path
import numpy as np
import re
from unidecode import unidecode   

folder_path = r"đường dẫn ở đây"

user_input = input("Nhập từ khóa cần tìm: ")

def normalize(text):
    text = unidecode(text)
    text = text.lower()
    text = text.replace("0", "o").replace("1", "i")
    text = re.sub(r"[^a-z\s]", "", text)
    return text

name_keywords = normalize(user_input).split()

reader = easyocr.Reader(['en'], gpu=True)


def is_match(text, keywords):
    words = text.split()
    return all(k in words for k in keywords)


def scan_pdf(pdf_path):
    page = 1

    while True:
        try:
            images = convert_from_path(
                pdf_path,
                dpi=300,
                first_page=page,
                last_page=page
            )

            if not images:
                break

            img = np.array(images[0])
            results = reader.readtext(img, detail=0)

            print(f"[DEBUG] {pdf_path} - page {page}")

            for i in range(len(results)):
                combined = " ".join(results[i:i+3])
                norm = normalize(combined)

                if is_match(norm, name_keywords):
                    print("\n[+] FOUND")
                    print(f"    Name: {user_input}")
                    print(f"    File: {pdf_path}")
                    print(f"    Page: {page}")
                    print(f"    Text: {combined}\n")

            page += 1

        except Exception as e:
            print(f"[ERROR] {e}")
            break


for file in os.listdir(folder_path):
    if file.lower().endswith(".pdf"):
        full_path = os.path.join(folder_path, file)
        scan_pdf(full_path)
