# Installation of the app

## Option 1: Directly pull the docker image from Docker Hub

### Pre-requisites
- Docker installed on your machine
- Ensure that the docker engine is running

### Steps
1. Pull the docker image from Docker Hub
    ```bash
    docker pull aumpauskar/f1-flaskapp:latest
    ```

2. Run the docker image
    ```bash
    docker run -p 5000:5000 aumpauskar/f1-flaskapp:latest
    ```

3. Open the web app in your browser
    ```
    http://localhost:5000
    ```

## Option 2: Build the docker image from the source code

### Pre-requisites
- Docker installed on your machine
- Ensure that the docker engine is running
- Git installed on your machine

### Steps
1. Clone the repository
    ```bash
    https://github.com/AumPauskar/f1-telem-webapp.git
    cd f1-telem-webapp/
    ```

2. Build the docker image
    ```bash
    docker build -t f1-flaskapp .
    ```

3. Run the docker image
    ```bash
    docker run -p 5000:5000 f1-flaskapp
    ```

4. Open the web app in your browser
    ```
    http://localhost:5000
    ```

## Option 3: Run the app native on your machine

### Pre-requisites
- Python 3.8 or higher installed on your machine
- Pip installed on your machine
- Git installed on your machine

### Steps
1. Clone the repository
    ```bash
    https://github.com/AumPauskar/f1-telem-webapp.git
    cd f1-telem-webapp/
    ```

2. Create a virtual environment (optional)
    ```bash
    python3 -m venv env
    ```

    - Activate the virtual environment
        ```bash
        source env/bin/activate
        ```

    - Activate the virtual environment (windows)
        ```bash
        .\env\Scripts\activate.bat
        ```

3. Install the dependencies

    - Option 1: Install the dependencies from the manually (faster and **recommended**)\
        **Linux**
        ```bash
        pip3 install flask==3.0.*
        pip3 install fastf1
        pip3 install gunicorn
        ```
        **Windows**
        ```bash
        pip install flask==3.0.*
        pip install fastf1
        pip install waitress
        ```

4. Run the app
    ```bash
    flask run
    ```
