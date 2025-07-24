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

This can now be accessed via web browser - http://localhost:31001

## Running app using Docker

Clone the repository:

```
git clone git@github.com:kelvgooding/sample-app.git
```

Navigate to the cloned repository directory

The following file will need to be updated before running the images/containers:

* DB_HOST = ''
* DB_USER = ''
* DB_PASSWORD = ''

```
/modules/config.py
```

Run the following command to build the Docker images

```
sudo docker pull mariadb:latest
```
```
sudo docker build -t sample-app .
```

Run the following command to create and start the containers:

```
sudo docker run -d --name sample-app-db -e MARIADB_ROOT_PASSWORD=password -e MARIADB_DATABASE=sample-app-db -e MARIADB_USER=user -e MARIADB_PASSWORD=password -p 3306:3306 -v /mnt/usb/sample-app-db:/var/lib/mysql --restart always mariadb:latest
```
```
sudo docker exec -i sample-app-db mariadb -u root -ppassword sample-app-db < ~/repos/sample-app/scripts/sql/create_tables.sql
```
```
sudo docker exec -it sample-app-db bash
```
```
mariadb -u root -p
```
```
GRANT ALL PRIVILEGES ON `sample-app-db`.* TO 'user'@'%' IDENTIFIED BY 'password';
FLUSH PRIVILEGES;
```
```
exit;
```
```
exit
```
```
sudo docker run -itd -p 31001:31001 sample-app
```

This can now be accessed via web browser - http://localhost:31001
