import qrcode
import os
import platform
import subprocess
from urllib.parse import urlparse

# Makes sure there are no overrides by giving a unique file name and generate the QR code
def generate_qr(url):

    output_folder = "generated_qr"
    os.makedirs(output_folder, exist_ok=True)

    file_path = os.path.join(output_folder, "qr_code.png")
    uniq = 1

    while os.path.exists(file_path):
        file_path = os.path.join(output_folder, f"qr_code_{uniq}.png")
        uniq += 1

    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()
    img.save(file_path)

    return file_path

def open_image(file_path):
    os_name = platform.system()
    absolute_path = os.path.abspath(file_path)

    if os_name == "Windows":
        os.startfile(absolute_path)

    elif os_name == "Linux":
        subprocess.Popen(["xdg-open", absolute_path])

    elif os_name == "Darwin":  
        subprocess.Popen(["open", absolute_path])

    else:
        print(f"Cannot open image automatically on this OS: {os_name}. Please open {file_path} manually.")

while True:
    # Ask for a new URL every iteration
    url = input("Enter the URL to generate QR code: ").strip()

    # Validate the URL
    if not url:
        print("Error: URL cannot be empty.")
        continue

    parsed_url = urlparse(url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.hostname:
        print("Error: Please enter a valid HTTP or HTTPS URL.")
        continue

    # Generate the QR code
    file_path = generate_qr(url)

    print(f"QR code generated and saved as: {file_path}")
    open_image(file_path)

    response = input(
        "Generate another QR code? (y/n): "
    ).strip().lower()

    if response == "n":
        print("Exiting the program.")
        break