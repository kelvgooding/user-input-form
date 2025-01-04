# User Input Form

## Description

User Input Form is a sample app, which using Flask as a python web framework, and a database which stores the data which is input on the landing page. Essentially, this tests the connection between the application and the database, to ensure data can be processed.

## Running app locally

Clone the repository:

```
git clone git@github.com:kelvgooding/user-input-form.git
```

Navigate to the cloned repository directory

Install any dependices required:

```
pip install -r requirements.txt
```

Start the User Input Form app:

```
python3 app.py
```

This can now be accessed via web browser - http://localhost:5000

## Running app using Docker

Clone the repository:

```
git clone git@github.com:kelvgooding/user-input-form.git
```

Navigate to the cloned repository directory

Run the following command to build the Docker image

```
sudo docker build -t user-input-form .
```

Run the following command to create and start the container:

```
sudo docker run -itd -p 5000:5000 user-input-form
```

This can now be accessed via web browser - http://localhost:5000