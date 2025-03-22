# Ollama Setup Guide

This guide explains how to install **Ollama**, pull the **TinyLlama** model, and run a Python script that interacts with the locally running Ollama server.

---

## **1. Install Ollama**
If Ollama is not already installed, run the following command:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

After installation, verify that Ollama is installed:

```bash
ollama --version
```

If Ollama is not running, start it using:

```bash
ollama serve
```

---

## **2. Pull the TinyLlama Model**
TinyLlama is a lightweight model suitable for low-spec machines. Pull it using:

```bash
ollama pull tinyllama
```

To verify that TinyLlama is installed, list available models:

```bash
ollama list
```

---

## **3. Clone the Repository**
If you have a repository containing the chat script, clone it using:

```bash
git clone <repository_url>
cd <repository_name>
```

If you don’t have a repository, create a Python script as shown in Step 4.

---



---

## **4. Install Required Python Packages**
If `requests` is not installed, install it using:

```bash
pip install requests
```

---

## **5. Run the Script**
Start a chat session with TinyLlama by running:

```bash
python chat_ollama.py
```

Example interaction:
```
You: What is Python?
Ollama: Python is a high-level programming language known for its readability...
You: exit
Goodbye!
```

---


### Now you are ready to use Ollama with TinyLlama! 🚀

