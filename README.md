# game-graphs

# Running
To run just run `docker-compose up`

This will start up a postgres db and the api server listening at `http://localhost:8000` as well as an angular ui at `http://localhost:4200`

The easiest way to interact with the api directly is by using the UI at `http://localhost:8000/docs`


# API Tests
To test the api run `docker-compose run --rm --entrypoint=nose2 api` while the db is still running