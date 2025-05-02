# **Simple QR Code Generator** **🚀**

***Welcome to the Simple QR Code Generator project ! This beginner-friendly Python project uses the*** `segno` ***library to create QR codes from any link you provide. It's super easy to use, modern and perfect for learning the basics of Python and QR code generation. Let's dive in ! 🎉***

## What is this project about ? 🤔

This project allows you to:

- Input any URL or text.
- Generate a QR code as a PNG image.
- Save the QR code to your project folder.

The generated QR code can be scanned by any QR code reader to access the provided link. It's a fun way to explore Python and create something useful !

## Folder Structure 📂

To keep things organized, structure your project folder like this:

```
qr-code-generator/
├── main.py          # The main Python script for generating QR codes
├── README.md        # This file
```

## Prerequisites ✅

Before you start, make sure you have:

- **Python 3.x** installed on your computer. Download it from python.org if you haven't already.
- A code editor like VS Code, PyCharm, or even a simple text editor.
- Basic knowledge of running Python scripts.

## Installation Steps 🛠️

Follow these steps to set up and run the project:

1. **Clone or Download the Repository**

   - Clone this repo using:

     ```bash
     git clone https://github.com/your-username/qr-code-generator.git
     ```

   - Or download the ZIP file and extract it.

2. **Navigate to the Project Folder**

   - Open your terminal or command prompt and move to the project folder:

     ```bash
     cd qr-code-generator
     ```

3. **Install the** `segno` **Library**

   - Run the following command to install the `segno` library:

     ```bash
     pip install segno
     ```

4. **Verify Installation**

   - Ensure `segno` is installed by running:

     ```bash
     pip show segno
     ```

   - You should see details about the installed `segno` package.

## How to Run the Project ▶️

1. **Open the Terminal in the Project Folder**

   - Make sure you're in the `qr-code-generator` folder.

2. **Run the Script**

   - Execute the `main.py` script:

     ```bash
     python main.py
     ```

3. **Enter a Link**

   - When prompted, type a valid URL (e.g., `https://www.example.com`) or any text.
   - Press **Enter**.

4. **Check the Output**

   - A file named `qrcode.png` will be created in the project folder.
   - Open it to see your QR code !

5. **Scan the QR Code**

   - Use any QR code scanner (like your phone's camera or a dedicated app) to verify the link.

## Troubleshooting 🛑

Ran into issues? Here are some common problems and fixes:

- **Error:** `ModuleNotFoundError: No module named 'segno'`

  - This means `segno` isn't installed. Run `pip install segno` again and ensure you're using the correct Python environment.

- **QR Code Not Generated**

  - Ensure you entered a valid link or text.
  - Check if you have write permissions in the project folder.
  - Verify that `qrcode.png` isn't open in another program.

- **Python Command Not Found**

  - Make sure Python is installed and added to your system's PATH. Try running `python3 main.py` instead of `python main.py`.

- **Blank or Corrupted QR Code**

  - Ensure the `segno` library is up-to-date: `pip install --upgrade segno`.
  - Try reducing the `scale` value in `main.py` (e.g., change `scale=5` to `scale=3`).

If you still face issues, feel free to open an issue on this repo !

## Made By

This project was created with 💖 by **B P ARYAAN \[ ARYAAN-DEV \]**\
Want to contribute or have suggestions ? Feel free to fork this repo or submit a pull request ! 😊

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details.

Happy coding and enjoy generating QR codes !
