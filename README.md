# BibliotecaVM

This was my first real project, is a simple personal library manager made with flask and bootstrap. Keep a registry of your books and let you made all CRUD operations.

Originaly a live version was deployed on heroku server, now is down and I am working on a new version with more functionality and newer tecnologies.

Btw if want to test it you can follow this steps:

## Prerequisites

First of all you need to install:

- [PostgreSQL](https://www.postgresql.org/download/)
- [Python 3](https://www.python.org/downloads/)

## How to use

1. After clone this repository to your local create a .env file inside environment:

    ```python
    # environment/.env

    FLASK_DATABASE=postgresql://[user]:[password]@localhost/[database]
    FLASK_SECRET_KEY=[Your secret key]
    ```

2. Create venv environment and install dependencies

    ```bash
    ~ > python3 -m venv venv
    ~ > ./venv/Scripts/activate
    (venv) ~ > pip3 install -r requirements.txt
    ```

3. Just run and enjoy

    ```python
    ~ > python3 index.py
    ```

## Built With

- [Bootstrap](https://getbootstrap.com/) - Used to generate web view
- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - The web application framework
- [PostgreSQL](https://maven.apache.org/) - Database sistem

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details
