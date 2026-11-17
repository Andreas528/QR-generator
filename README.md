# QR Code Generator

A simple Python script that generates QR codes from URLs and automatically opens the generated images.

## Features

- Generate QR codes from HTTP and HTTPS URLs.
- Validate URL input.
- Save QR codes as PNG images.
- Automatically generate unique filenames.
- Open generated QR codes using the default image viewer.
- Supports Windows, Linux and macOS.

## Installation

Clone the repository and install the dependency:

```bash
git clone https://github.com/Andreas528/QR-generator.git
cd QR-generator
python -m pip install "qrcode[pil]"
```

## Usage

Run the script:

```bash
python main.py
```

Enter a URL when prompted. The QR code will be saved in the `generated_qr` folder and opened automatically.

## Requirements

- Python 3
- `qrcode[pil]`
