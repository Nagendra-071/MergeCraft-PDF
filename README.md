# 📄 MergeCraft PDF

MergeCraft PDF is a clean, intuitive, and highly responsive web application built with Python and Streamlit that allows users to upload multiple PDF files, custom-rearrange their merging sequence seamlessly, and download the combined document instantly.

---

## ✨ Features

* **Bulk Uploading**: Upload up to 10 PDF documents simultaneously via drag-and-drop or file browsing.
* **Dynamic Reordering**: View the current index sequence of your files and intuitively type a custom order (e.g., `2 1 3`) to match your exact structural needs.
* **Robust Processing**: Built-in streaming pointer resets (`file.seek(0)`) prevent browser crashes or empty data streams during rapid updates or reruns.
* **In-Memory Security**: Files are processed safely within internal memory buffers (`io.BytesIO`) rather than exposing local system directories or storing user data on disk.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Streamlit (Web UI wrapper)
* **Core Library:** pypdf (PDF parsing & merging engines)

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed on your local machine. You can download it from [python.org](https://www.python.org/).

### 2. Installation & Setup
Clone this repository to your local machine or copy the files into your local project environment:

```bash
# Navigate to your folder
cd "C:\LEARNED\Kaam ke\pdf merger"

# Install the required dependencies
pip install streamlit pypdf