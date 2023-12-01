# Classification 

## Overview

This repo notebook documents and streamlit file explaining the steps taken for a binary classification project involving a small dataset of fields and roads. The project includes the use of custom small models, transfer learning with VGG, and fine-tuning with CLIP.



### Dataset Splitting

The dataset is organized into folders for each class, and it's split into training and validation sets.

### Data Augmentation

Data augmentation techniques are applied using a custom DataLoader.

## Custom Small Model
First we have used a small custom model to train two class

## Transfer Learning with VGG and MobileNet

### Dataset Preparation

The dataset is split into training and validation sets.

### Transfer Learning

Pretrained VGG is used for transfer learning. Modifications are made to the last layer(s) for binary classification.

### Training and Evaluation

The transfer learning models are trained and evaluated on the dataset.

## Fine-tuning with CLIP

### Dataset loader

Custom image text pair dataloaders are created.

### CLIP Integration

The CLIP model is loaded and fine-tuned for classification. Training and evaluation are performed.


Notebooks is self explanatory easy to use. Its in Google colab to easily train and evaluate the models 


## Usage

To run the code local perform following steps


1. pip install requirements.txt

2. jupyter notebook and open Technical_Exercise.ipynb for see the code

3. To run streamlit use this command --> streamlit run streamlit_test.py



To run the code in docker first install docker

Run -- 'docker-compose up --build'





