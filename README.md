# Medical ASR

This project is a Medical Automatic Speech Recognition (ASR) system.

## Installation Guide

### Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (Anaconda or Miniconda)

### Setting Up the Environment

1. Clone the repository:

    ```
    git clone https://github.com/sociocom/medical-asr.git
    ```

2. Create the conda environment:

    ```
    cd backend
    conda env create -f environment.yml
    ```

3. Activate the conda environment:

    ```
    conda activate medical-asr
    ```

### Running the Application

#### Running the Backend

1. Navigate to the backend directory:

    ```
    cd backend
    ```

2. Start the backend server:

    ```
    python app.py
    ```

3. The backend server should now be running on `http://localhost:5000`.

#### Running the Frontend

1. Open a new terminal and navigate to the frontend directory:

    ```
    cd frontend
    ```

2. Install frontend dependencies:

    ```
    npm install
    ```

3. Start the frontend application:

    ```
    npm run dev
    ```

4. Open your browser and navigate to `http://localhost:3000/sample-chat`.