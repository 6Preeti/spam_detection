# Spam Detection System
# Overview
This project demonstrates a spam detection system using Flask and Python. The system leverages machine learning techniques, specifically a Naive Bayes model, to classify messages as spam or not spam. The project emphasizes the use of pipelining to streamline the machine learning workflow.

# Features
Web Interface: A user-friendly web interface built with Flask for users to input text and receive spam classification results.
Machine Learning: Utilizes a Naive Bayes model, trained to detect spam messages.
Pipelining: Integrates vectorization and classification into a seamless pipeline to simplify the process of transforming raw text into predictions.

# Technologies Used
Flask: A micro web framework for building the web interface and API.
Python: The primary programming language for developing the machine learning model and web service.
Scikit-learn: A machine learning library used to implement the Naive Bayes model and pipelining.
Pickle: Used for serializing the trained model and vectorizer.
