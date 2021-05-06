### Required Libaries to run on local host
`python3`
`pip3`
`virtualenv`
`cowsay`
`fortune`
`docker`

### Setup
All commands below assume you have already cloned the repo.
`virtualenv -p python3 env`
`source env/bin/activate`
`pip3 install -r requirements.txt`

### Running the flask app
`flask run --host=0.0.0.0 --port= {}`
within the `{}` please specify a port

### ending the flask app
sent a keyboard intterupt like 
`CTRL + C`


### Required Libaries to run on docker
`python3`
`pip3`
`virtualenv`
`cowsay`
`fortune`
`docker`

### Setup
All commands below assume you have already cloned the repo.
`docker build -t webfortune .`.

### Running in docker.
 `docker run -dp <desired_port>:5000 webfortune`.

### Quiting the docker application
`docker ps`
`docker stop {}`
`{}` is the ID of your docker continer

## Using my app
webfortune is a flask application that returns values based on the url it is feed. 
`we will assume everything below is typed after the first / within the url`

`fortune/` 
This returns a fortune.

`cowsay/` 
This must be accompined by `<message>` which will be displayed inside the linux cowsay command.

`cowfortune/` 
This will return a cowsay of fortune a random fortune.
