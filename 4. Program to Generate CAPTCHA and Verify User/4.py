# captcha_demo.py
import random
import string
import os
from captcha.image import ImageCaptcha
from PIL import Image

def random_captcha_text(length=5):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_captcha_image(text, filename="captcha.png"):
    image_captcha = ImageCaptcha(width=280, height=90)
    data = image_captcha.generate(text)
    image = Image.open(data)
    image.save(filename)
    return filename

def main():
    captcha_text = random_captcha_text(5)
    filename = generate_captcha_image(captcha_text, "captcha.png")
    print("CAPTCHA generated and saved as:", filename)
    
    # Open the image automatically on Windows
    try:
        os.startfile(filename)
    except Exception:
        print("Open the file manually:", os.path.abspath(filename))

    user_input = input("Enter the CAPTCHA text exactly as shown (case-sensitive): ").strip()
    if user_input == captcha_text:
        print("Verification: SUCCESS.")
    else:
        print("Verification: FAILED.")

if __name__ == "__main__":
    main()
