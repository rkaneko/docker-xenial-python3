The Docker image for running python3 script on Ubuntu:xenial.
===

### build the Docker image

```bash
$ cd ${THIS_REPO_ROOT}

$ sudo docker build -t your-name/xenial-python3:latest .

# show images
$ sudo docker images
```

### use the python3 repl on a docker image instance

```bash
$ sudo docker run -it --rm --name python3-repl your-name/xenial-python3:latest
```

### Run your python3 script

- See `sample` dir.
