# Spam Detection System
# Overview
This project demonstrates a spam detection system using Flask and Python. The system leverages machine learning techniques, specifically a Naive Bayes model, to classify messages as spam or not spam. The project emphasizes the use of pipelining to streamline the machine learning workflow.
<br>
# Features
Web Interface: A user-friendly web interface built with Flask for users to input text and receive spam classification results.<br>
Machine Learning: Utilizes a Naive Bayes model, trained to detect spam messages.<br>
Pipelining: Integrates vectorization and classification into a seamless pipeline to simplify the process of transforming raw text into predictions.<br>
<br>
# Technologies Used
Flask: A micro web framework for building the web interface and API.<br>
Python: The primary programming language for developing the machine learning model and web service.<br>
Scikit-learn: A machine learning library used to implement the Naive Bayes model and pipelining.<br>
Pickle: Used for serializing the trained model and vectorizer.
<br>
# Project Structure
spam-detection-system/<br>
├── app/ <br>
│   ├── templates/<br>
│   │   └── index.html <br>
│   │   └── show.html <br>
│   ├── main.py <br>
│   ├── Naive_model.pkl <br>
├── data/  <br>
│   ├── spam.csv <br>
├── prepare_models/ <br>
│   └── spam_detection.ipynb <br>
├── static/ <br>
│   └── gif <br>
├── README.md <br>
<br>
# Screenshot Of Project

![image](https://github.com/6Preeti/spam_detection/assets/88951371/75c5d931-6bb9-4d18-844a-62562709c0f3)
<br>
<br>
<b>***<b>This project was showcasing the application of machine learning skills in building a practical spam detection system.
