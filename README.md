# tvt_docker
## Dependency
    python3.7
    pip3
    docker

## Install project dependency
    pip3 install -r requirements.txt

## Run for task1
    python app.py 1 2 3

## Run test for taks1
    python test_app.py 

## Run application for task2
    python3 main.py
    or
    docker-compose up

## Access task2 application on url
    PUT: http://localhost:5000/sum
    input body:[1,2,'a']
    or 
    curl -H 'Content-Type: application/json' -X PUT -d '[1,2,"a"]' http://localhost:5000/sum

## Run test for task2 application:
    python3 -m pytest