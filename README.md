# AI and Machine Learning Projects Repository

Welcome to the repository! Below is an overview of the main projects housed here.

## Table of Contents
1. [Freight Logistics - Predicting Shipment Delays](#freight-logistics---predicting-shipment-delays)
2. [Image Descriptor POC Application](#image-descriptor-poc-application)

---

### Freight Logistics - Predicting Shipment Delays
Predicting shipment delays is essential for maintaining efficiency in freight logistics. This project focuses on building a machine learning model to forecast delays based on historical data and deploying it via an API for practical use.

#### Key Features
- **Problem Addressed**: Predicting shipment delays based on traffic, weather, and other operational factors.
- **Technologies Used**: Python, pandas, numpy, scikit-learn, FastAPI.
- **Outputs**: An API to predict delays.
- **EDA and Analysis Approaches**:
  - **Correlation Analysis**: Identify relationships between shipment delays and features like traffic and weather.
  - **Trend Visualization**: Use graphs to understand shipment patterns over time.
  - **Feature Selection**: Determine key contributors to delays using statistical methods.

#### Approaches
- **Preprocessing**: Cleaning and encoding of raw data, handling missing values, and outlier removal.
- **Model Development**:
  - Compare Logistic Regression, Decision Tree, and Random Forest models.
  - Optimize hyperparameters to improve model accuracy.
- **Deployment**: Build a FastAPI interface for real-time predictions.

---

### Image Descriptor POC Application
This web application leverages pre-trained image captioning models to generate text descriptions for uploaded images.

#### Key Features
- **Functionality**: Upload an image to receive an AI-generated text description.
- **Supported Models**:
  - BLIP Large (`Salesforce/blip-image-captioning-large`)
  - GIT Large COCO (`microsoft/git-large-coco`)
  - ViT-GPT2 (`nlpconnect/vit-gpt2-image-captioning`)
- **Technologies Used**: Next.js, React, Tailwind CSS, Hugging Face Inference API.

#### Approaches
- **Model Integration**: Connect multiple pre-trained models via Hugging Face API.
- **Frontend Development**:
  - Use React components for user interaction.
  - Design a responsive UI using Tailwind CSS.
- **Error Handling**:
  - Validate uploaded images and provide meaningful error messages.
  - Handle API errors gracefully.

---

## Repository Overview
This repository demonstrates best practices in AI and machine learning project development, emphasizing modularity, scalability, and usability. Navigate to individual project directories for in-depth details and implementation insights.

Feel free to explore, contribute, and suggest improvements!

