# Flask Uploading Files

This project demonstrates how to upload and serve files using a Flask web application.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/flask-uploading-files.git
    cd flask-uploading-files
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask application:

    ```sh
    python run.py
    ```

2. Access the service:

    Open your web browser and go to [http://localhost:8080](http://localhost:8080)

### API Endpoints

- **GET /**: Displays the file upload form and the list of uploaded files.
- **POST /upload**: Handles file upload and stores the file on the server.
- **GET /files/<filename>**: Serves the uploaded file.

## Built With

- Flask - The web framework used

## Acknowledgments

- Inspired by the Spring Boot guide for uploading files
