# Number Converter - Flask Web Server

This project aims to implement a number to text converter, receiving an integer between [-99999:99999], returning a json with its full text form (portuguese language). 
The solution consists of a simple web server coded in Python framework Flask, receiving a GET method with the number in its path.


## Requirements

* Docker installed


## Install and Run

The application runs in a docker container, this means no other specific requirement needs to be installed, you just have to build the container and run it.

To build and run the container:

```sh
docker build -t n_converter . && docker run -it --name n_conv  -p 4000:4000 n_converter
```

This will create a docker image called "n_converter" and run a container named "n_conv". The application will start as the container is running.


* Obs1.: During development, it was used the docker-compose engine, for easier coding.


## The Application

* To use the application you can simply open a browser and go to `http://0.0.0.0:4000/` and put a number after the bar, it will accept any string, converting the numbers between [-99999:99999]. (It will raise errors if the input is not valid)

* Other way you can test is using `curl`. Examples:
    ```sh
    curl http://0.0.0.0:4000/1234
    $ { "extenso": "mil e duzentos e trinta e quatro" }
    ```

    ```sh
    curl http://0.0.0.0:4000/-1234
    $ { "extenso": "menos mil e duzentos e trinta e quatro" }
    ```

    ```sh
    curl http://0.0.0.0:4000/aaaa
    $ { "ERROR": "Input not an integer: cannot resolve" }
    ```

    ```sh
    curl http://0.0.0.0:4000/1000000
    $ { "ERROR": "Number is out of range" }
    ```


## Testing

Tests were made to develop the application, they're in the "test" folder and can be ran once the application is running in the container. 
It's possible to check that by executing the following in another terminal while running the application:

```sh
docker exec -it n_conv python test/test_converter.py
```

Obs.: the container running the application has to be named n_conv, otherwise the command above should be changed to fit the container name

