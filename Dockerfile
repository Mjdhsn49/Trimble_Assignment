# Use an official PyTorch runtime as a parent image
FROM anibali/pytorch:2.0.1-cuda11.8


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make ports 8888 and 8501 available to the world outside this container
EXPOSE 8888
EXPOSE 8501

# Run jupyter and streamlit when the container launches
CMD ["bash", "-c", "jupyter notebook --ip='*' --port=8888 --no-browser --allow-root & streamlit run Technical_Exercise/streamlit_test.py & wait"]
