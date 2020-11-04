# Getting Started with Docker

### HELLO WORLD

```sh
docker run hello-world
```

### Playing with Busybox

```sh
docker pull busybox
```

```sh
docker images
```

```sh
docker run busybox
```

```sh
docker run busybox echo "hello from busybox"
```

```sh
docker ps
```

```sh
docker ps -a
```

```sh
docker run -it busybox sh
```

```sh
docker rm $(docker ps -a -q -f status=exited)
```

```sh
docker container prune
```
 
###  Docker Images

```sh
docker images
```

```sh
docker images
```

```sh
docker pull ubuntu:18.04
```

###  Creating First Docker App

```sh
docker build -t yourusername/catnip .
```

```sh
docker run -p 8888:5000 yourusername/catnip
```

```sh
Check http://localhost:8888/
```	


### Docker on AWS - AWS Elastic Beanstalk (EB)

```sh
docker login
```

```sh
docker push yourusername/catnip
```

```sh
docker run -p 8888:5000 yourusername/catnip
```	

Upload it to AWS EB and create an application