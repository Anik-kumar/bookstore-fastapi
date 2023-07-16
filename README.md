
# pyenv commands
`pyenv shell <version>` -- select just for current shell session \
`pyenv local <version>` -- automatically select whenever you are in the current directory (or its subdirectories) \
`pyenv global <version>` -- select globally for your user account \

```shell
$ pyenv shell 3.11.4 
$ export PYENV_VERSION="3.11.4"
$ which python3                                                                                              1 ↵ ──(Sun,Jul09)─┘
  > /Users/<user-home>/.pyenv/shims/python3
$ python3 --version                                                                                              ──(Sun,Jul09)─┘
  > Python 3.11.4
```

## Create virtual environment
```shell
# Check current python version
$ python3 --version  
  > Python 3.11.4
$ python3 -m venv /Users/<user-home>/.local/share/virtualenvs/fast-api-venv

# Activate python for current project
$ source /Users/<user-home>/.local/share/virtualenvs/fast-api-venv/bin/activate
$ which python3 
  > /Users/<user-home>/.local/share/virtualenvs/fast-api-venv/bin/python3
$ python3 --version                                                                                            
  > Python 3.11.4
$ which pip                                                                                                     
  > /Users/<user-home>/.local/share/virtualenvs/fast-api-venv/bin/pip

$ pip install poetry 

$ source /Users/<user-home>/.local/share/virtualenvs/fast-api-venv/bin/activate

$ which poetry
  > /Users/<user-home>/.local/share/virtualenvs/fast-api-venv/bin/poetry
  
$ poetry add fastapi 
$ poetry add "uvicorn[standard]" gunicorn

```
https://fastapi.tiangolo.com/deployment/server-workers/

Run 
```shell
$ poetry run uvicorn main:app --reload
$ poetry run uvicorn src.main:app --reload
$ poetry run gunicorn src.main:app --workers 3 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080
$ ps -ef | grep "uvicorn.workers.UvicornWorker"
```

## Build project
```shell
$ make build
```

## Check Lint
```shell
$ make lint
```

## Run latest build image
```shell
$ make run
```

Check the container by running `docker container ls -a` \
CONTAINER ID   IMAGE                          COMMAND                  CREATED         STATUS                        PORTS                    NAMES
678106d2d9f5   fast-api-project:latest        "/bin/sh -c 'poetry …"   9 minutes ago   Up 9 minutes                  0.0.0.0:8080->8080/tcp   fast-api_fast-api-service_1


Check `GET http://0.0.0.0:8080/docs` and `GET http://0.0.0.0:8080/items/123`


