# Python Script README
This script is capable of extracting data from https://www.pascalcoste-shopping.com/soins-cheveux/cheveu-normal.html and load it to mysql database

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/wael-sudo2/Test1.git

2. Pull Docker images:
    ```bash
   docker pull mysql
   docker pull waelhkiri/testcrawler:v1.0

3. You can choose to run the script in two ways:

- using Docker Compose (Recommended)

    - This method is ideal for development and testing as it allows you to easily manage dependencies and configurations
    open a terminal under the project directory and type in the command
    ```bash
    docker-compose up --build

- Using the Uploaded Docker Hub Image:
    - if you prefer a more streamlined approach, you can leverage the pre-built image uploaded to Docker Hub but make sure to use this configuration as you docker compose file
    **Sample docker-compose.yml**

    ```yaml

    version: '3.8'

    services:
    mysql:
        image: mysql:latest
        restart: always
        environment:
        MYSQL_ROOT_PASSWORD: test1pw
        MYSQL_DATABASE: extracted_data
        ports:
        - "3306:3306"
        volumes:
        - ./mysql-data:/var/lib/mysql

    app:
        image: waelhkiri/testcrawler:v1.0
        depends_on:
        - mysql

4. Check your sql database using:
 ```bash
    docker exec -it test1-mysql-1  mysql -u root -p
    password:test1pw