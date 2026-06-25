# DecodeLabs-Internship-Project-4

## Overview

This project demonstrates a basic Text Recognition system using Optical Character Recognition (OCR). The application extracts text from an image using Python, OpenCV, and Tesseract OCR.

## Features

* Reads text from images
* Preprocesses images for improved recognition
* Uses Tesseract OCR for text extraction
* Displays recognized text in the terminal

## Technologies Used

* Python
* OpenCV
* Pytesseract
* Pillow

## Project Structure

```text
DecodeLabs-Internship-Project-4/
│
├── app.py
├── requirements.txt
├── sample_image.png
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Moosa26/DecodeLabs-Internship-Project-4.git
```

Move into the project directory:

```bash
cd DecodeLabs-Internship-Project-4
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Tesseract OCR:

Windows:

Download and install Tesseract OCR, then add its installation path to the system environment variables.

Linux:

```bash
sudo apt install tesseract-ocr
```

## Usage

Place an image containing text in the project folder and name it:

```text
sample_image.png
```

Run the application:

```bash
python app.py
```

Example Output:

```text
Recognized Text:

Welcome to DecodeLabs Internship Program
```

## Learning Outcomes

* Image preprocessing with OpenCV
* OCR based text recognition
* Working with pre trained AI tools
* Basic computer vision workflow

## Conclusion

This project implements a simple OCR pipeline that converts image based text into machine readable text using widely adopted AI libraries.


## Author

Built by Muhammad Moosa Hasan as part of the DecodeLabs AI Industrial Training Program, Batch 2026.
