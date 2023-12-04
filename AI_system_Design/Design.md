# AI system Design

As a task with annotating a limited number of images from a vast unlabelled dataset, the following step-by-step process can be considered:

## 1. Understand the Problem Domain

- Understanding the problem domain and algorithmic requirements for the task given.

## 2. Define Annotation Criteria

- Clearly define criteria for selecting promising images.

## 3. Sampling

- Randomly sample a small subset for an initial overview and select random samples and perform analysis.

## 4. Clustering

- Applying some unsupervised techniques of clustering algorithms to group similar images.

## 5. Active Learning

- Implement active learning strategies based on model uncertainty.

## 6. Feedback from Existing Models

- Utilize feedback from existing AI models to identify challenging images.

## 7. Human-in-the-Loop

- Since we can't rely completely on AI models we need human annotators using a combination of automation and human judgment.

## 8. Iterative Approach

- Adopt an iterative approach where annotations lead to model improvements.

## 9. Documentation and Analysis

- Since this process is selective, documenting the reason behind image selection and perform a thorough analysis should be done.

## 10. Validation

- Finally we reserve a portion for validation and evaluate the impact on model performance to verify our selected images are good or not.

Overall the selection process involves a combination of automated techniques, human expertise, and continuous feedback loops.
