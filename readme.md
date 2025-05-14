

---

````markdown
# 🔍 Phishing URL Detection System

This is a Flask-based web application that uses a machine learning model to classify URLs as **Legitimate** or **Phishing**. It provides a modern UI built with Tailwind CSS and is deployable on platforms like **Render**.

---

## 🚀 Features

- ✅ Detects if a URL is phishing or legitimate
- 🧠 Utilizes a trained **Random Forest Classifier**
- 💡 Extracts meaningful features from URLs
- 🎨 Clean, responsive frontend using **Tailwind CSS**
- 🌐 RESTful API for backend communication
---

## 🧠 How It Works

The model extracts the following features from a URL:

- URL length
- Number of dots, slashes, hyphens, `@`, `=`, `&`, etc.
- Subdomain and TLD length
- IP address presence
- Special characters and digits count

The extracted features are used as input to a **Random Forest Classifier** trained on labeled URL data.

---

## 🛠️ Technologies Used

| Category         | Stack                                      |
|------------------|---------------------------------------------|
| **Frontend**     | HTML, JavaScript, Tailwind CSS              |
| **Backend**      | Flask, Python                               |
| **ML Model**     | Scikit-learn (RandomForestClassifier)       |
| **Data Handling**| Pandas, NumPy                               |

---

## 🧪 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/awasthiesDev/Phishing-URL-detection.git
cd phishing-url-detector
````

### 2. Install Dependencies

Make sure Python is installed, then run:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---


## 📁 File Structure

```
phishing-url-detector/
│
├── app.py                      # Flask application
├── phishing_random_forest_model.pkl  # Trained model
├── templates/
│   └── index.html              # Frontend HTML
├── static/
│   ├── script.js               # Frontend JS
│   └── Challenges-of-Phishing-Detection-2.jpg # Background
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🧠 Future Improvements

* Add support for real-time link preview/screenshot
* Integrate URL shortening service check
* Include model confidence level as a percentage

---

## 🙌 Acknowledgements

* [Tailwind CSS](https://tailwindcss.com)
* [Scikit-learn](https://scikit-learn.org/)

---

## 📫 Contact

**Anupam Awasthi**

[GitHub](https://github.com/awasthiesDev) 

```

---

```
