# langchain-prompt

A LangChain-powered AI application that leverages the **Qwen / Qwen-3 0.6B** model to deliver exceptional text generation capabilities.

---

## 📌 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Demo / Screenshots](#demo--screenshots)  
4. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation](#installation)  
   - [Configuration](#configuration)  
   - [Running the App](#running-the-app)  
5. [Usage](#usage)  
   - [Basic Usage](#basic-usage)  
   - [Advanced Usage](#advanced-usage)  
6. [Project Structure](#project-structure)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Acknowledgements](#acknowledgements)  
10. [Contact](#contact)

---


## ✅ Overview

`langchain-prompt` is a Python application built with **LangChain** that integrates the **Qwen / Qwen-3 0.6B** model to generate high-quality text for various use cases.  
It is ideal for experimenting with LLM prompts, creating automation workflows, and learning how to use LangChain effectively.

---

## ✨ Features

- Lightweight and easy-to-run Python implementation using LangChain  
- Integration with Qwen / Qwen-3 0.6B for state-of-the-art text generation  
- JSON-based prompt templates for easy customization and reuse  
- Modular structure for future expansion (additional models, prompt strategies)

---

## 📷 Demo / Screenshots

<img width="1908" height="872" alt="image" src="https://github.com/user-attachments/assets/dbb210da-3618-45ff-a2f9-1f32ddc4af2b" />
<img width="1887" height="853" alt="image" src="https://github.com/user-attachments/assets/98d07fee-8b03-4b0a-864e-95113f2d2a06" />



---

## 🚀 Getting Started

### ✅ Prerequisites

- Python **3.8+**  
- **Git** for cloning the repository  
- API credentials for Qwen / LangChain (if required)

### ✅ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rajeshwar-singh/langchain-prompt.git
   cd langchain-prompt
   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. pip install -r requirements.txt

### ✅ Configuration
- If API keys or environment variables are needed, create a .env file:
   ```bash
   QWEN_API_KEY="your_api_key_here"

### ✅ Running the App
  To start the Streamlit application, run:
   
   streamlit run Langchain-Prompts\prompts_ui.py
   
---

## 💻 Usage

### ✅ Basic Usage
- Select a prompt template from **`template.json`**
- Run the app and provide input as requested
- Get AI-generated responses using **Qwen / LangChain**

### ✅ Advanced Usage
- **Modify templates**: Customize `template.json` for new use cases
- **Add models**: Extend the app to support other LangChain-compatible LLMs
- **Batch processing**: Automate prompt execution through CLI scripts or Python scripts

---

## 📂 Project Structure

langchain-prompt/
├── Langchain-Prompts/            
│   └── prompts_ui.py             
├── template.json                 
├── requirements.txt            
├── README.md                    
└── venv/  

---

## 🤝 Contributing
Contributions are welcome!
 1. Fork this repo
    
 2. Create a feature branch:
    ```bash
    git checkout -b feature/YourFeature
    
 3. Commit your changes:
    ```bash
    git commit -m "Add YourFeature"
    
 4. Push to your branch:
    ```bash
    git push origin feature/YourFeature

 5. Open a Pull Request

---

## 📜 License
This project is licensed under the **MIT License**

---

## 🙌 Acknowledgements
- LangChain
   – for simplifying LLM integrations

- Qwen Model
   – for advanced natural language processing
---

## 📬 Contact
- Created and maintained by **Rajeshwar Singh**.
- For feedback or questions, open an issue or connect via [GitHub Profile](https://github.com/rajeshwar-singh)





