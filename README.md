
# Animal Disease Prediction using Machine Learning

This project is a **Streamlit-based web application** that predicts animal diseases based on user-input symptoms and other parameters. It uses a trained machine learning model to provide quick, probability-based predictions for multiple animal species.

---

## Features
- Interactive **Streamlit UI** for easy user input.
- Supports **multiple animal species**.
- Accepts key features like **animal type**, **age**, and **temperature**.
- Returns the **predicted disease** and its probability.
- Can be deployed on **Streamlit Cloud** or run locally.

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/animal-disease-prediction.git
cd animal-disease-prediction
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app locally

```bash
streamlit run app.py
```

---

## Project Structure

```
animal-disease-prediction/
│
├── app.py                 # Main Streamlit app
├── model.pkl              # Trained ML model
├── label_encoders.pkl     # Encoders for categorical data
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## How It Works

1. The user selects **animal type** from a dropdown.
2. Enters **age** and **temperature** values.
3. The app **preprocesses** these inputs using label encoding and scaling.
4. The trained model predicts the most likely disease and returns the result.

---

## Deployment on Streamlit Cloud

1. Push your code to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. Set the **main file path** to `app.py`.
4. Deploy and share your app URL.

---

## Requirements

* Python 3.8+
* Streamlit
* Pandas
* Scikit-learn
* Joblib

---

## Example Prediction Flow

1. **Input:** Lion, 5 years old, 39.5°C
2. **Output:** Possible disease: *Feline Distemper* (82% probability)

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by Yash Bhardwaj as part of a Machine Learning project for animal healthcare.

