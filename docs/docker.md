# Docker

## Installation
Docker can be installed from the official website [here](https://www.docker.com/). For windows users, you can download and install Docker Desktop and for Linux users, you can install Docker Engine.

## Building and running the docker container
- Using docker for this application is very simple
```bash
docker build -t <image-name> .
```

- To run the docker container
```bash
docker run -p 5000:5000 <image-name>
```

**Note:** The docker engine should be running before running the above commands.\
To ensure that the docker engine is running, you can run the following command:
```bash
sudo systemctl status docker
```
Or for windows just ensure docker desktop is running.