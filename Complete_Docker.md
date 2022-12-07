## What is Docker ? 

- Docker is an open source platform that enables developers to build, deploy, run, update and manage containers—standardized, executable components that combine application source code with the operating system (OS) libraries and dependencies required to run that code in any environment.


### Useful Docker Commands

```
  Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Options:
      --config string      Location of client config files (default "/Users/faduma/.docker")
  -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and default context set with "docker context use")
  -D, --debug              Enable debug mode
  -H, --host list          Daemon socket(s) to connect to
  -l, --log-level string   Set the logging level ("debug"|"info"|"warn"|"error"|"fatal") (default "info")
      --tls                Use TLS; implied by --tlsverify
      --tlscacert string   Trust certs signed only by this CA (default "/Users/faduma/.docker/ca.pem")
      --tlscert string     Path to TLS certificate file (default "/Users/faduma/.docker/cert.pem")
      --tlskey string      Path to TLS key file (default "/Users/faduma/.docker/key.pem")
      --tlsverify          Use TLS and verify the remote
  -v, --version            Print version information and quit

Management Commands:
  builder     Manage builds
  buildx*     Docker Buildx (Docker Inc., v0.9.1)
  compose*    Docker Compose (Docker Inc., v2.12.2)
  config      Manage Docker configs
  container   Manage containers
  context     Manage contexts
  dev*        Docker Dev Environments (Docker Inc., v0.0.3)
  extension*  Manages Docker extensions (Docker Inc., v0.2.13)
  image       Manage images
  manifest    Manage Docker image manifests and manifest lists
  network     Manage networks
  node        Manage Swarm nodes
  plugin      Manage plugins
  sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
  scan*       Docker Scan (Docker Inc., v0.21.0)
  secret      Manage Docker secrets
  service     Manage services
  stack       Manage Docker stacks
  swarm       Manage Swarm
  system      Manage Docker
  trust       Manage trust on Docker images
  volume      Manage volumes

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  build       Build an image from a Dockerfile
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  events      Get real time events from the server
  exec        Run a command in a running container
  export      Export a container's filesystem as a tar archive
  history     Show the history of an image
  images      List images
  import      Import the contents from a tarball to create a filesystem image
  info        Display system-wide information
  inspect     Return low-level information on Docker objects
  kill        Kill one or more running containers
  load        Load an image from a tar archive or STDIN
  login       Log in to a Docker registry
  logout      Log out from a Docker registry
  logs        Fetch the logs of a container
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  ps          List containers
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  rmi         Remove one or more images
  run         Run a command in a new container
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  search      Search the Docker Hub for images
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  version     Show the Docker version information
  wait        Block until one or more containers stop, then print their exit codes

  Run 'docker COMMAND --help' for more information on a command.
  
```

- `docker --version` - should get the version 20.11
- `docker - gets` the cheat sheet for docker
- `docker pull hello-world` - downloads the hello-world container
- `docker images` - displays the images you have
- `docker run hello-world` - runs the image we downloaded before
- `docker ps` - shows images currently running
- `docker ps -a` - draws ALL the processes that are running at the moment
- `docker run -p 2368:2368 ghost` - will pull and then run it in one go and select the correct port
- `docker rm [docker id] -f` - to force delete docker that is running
- `docker run -p 80:80 nginx` - to launch nginx
- `docker run -d -p 80:80 nginx`- d stands for detatch mode so we will get the terminal back when run
- `docker logs [container id]` - shows the logs of the running process
- `docker run -d -p 4000:4000 docs/docker.github.io` - downaloads container and can run in the background. run localhost:4000
- `docker stop [process id]` - stops the process running with all the
- `docker start [process id]` - starts the process where it left off
- `docker exec -it [process id] bash` - be able to execute shell commands in the process provided

---
### How to remove Container 

- `docker rm [docker id] -f` 

### How to create/run Container

- `docker run -d -p PORT_LOCAL:PORT_APP image_name` e.g `docker run -d -p 80:80 nginx`

### How to Stop Container 

- `docker stop container_ID` 

### Uploading to Docker:

**Log in** 

- First step is to ensure that logged into docker locally throught the desktop 
- If not login using creditials `docker login`

**Commit Changes**

- command is `docker commit CONTAINER_ID USERNAME/REPO_NAME:TAG`
- very important to have the username in there, it is what tells docker where to put the commit
- `docker commit CONTAINER_ID Abdellah12321/eng130_test:V.1`


**Then, push to Docker Hub**

- just run `docker push CONTAINER_ID USERNAME/REPO_NAME:TAG`
- i.e. replace commit with push
- NOTICE: for pushing mentioning the tag also puts that tag on there for people when pulling
- NOTE: if the repo doesn't exist within Docker Hub, Docker will create it and add the image you want to push

**Pull and Running Instances**

- `docker run -d -p PORT_LOCAL:PORT_APP CONTAINER_ID USERNAME/REPO_NAME:TAG`
  
### Automate build of image using Dockerfile

In order to build images automatically you will need a dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. This page describes the commands you can use in a Dockerfile.

Here is the format of the Dockerfile:

`INSTRUCTION arguments` The instruction is not case-sensitive. However, convention is for them to be UPPERCASE to distinguish them from arguments more easily.

For more information on Dockerfiles check out official Docker Documentation [Click here](https://docs.docker.com/engine/reference/builder/)



### Multi-Stage Build

- Using the development image can be useful for testing and additional configuration, but the image size may be relatively large. Once everything is working with the development image, multi-stage builds can be used to create a lightweight image, without having to write a new Dockerfile.

- Add another stage with a more lightweight image (FROM node:alpine) and copy any necessary files from the first stage, and then run any necessary commands. For the node app, multi-stage builds reduced the image size from ~805MB to ~250MB.

```
CMD ["node", "app.js"]

FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install -g npm@7.20.6

COPY --from=app /usr/src/app /usr/src/app

EXPOSE 3000

CMD ["node", "app.js"]

```

### Docker Compose 

- Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration

- Written in yaml

**Docker File Structure**

<img width="442" alt="Screenshot 2022-11-22 at 16 59 22" src="https://user-images.githubusercontent.com/115224560/204245052-29207a5b-51aa-4ab6-a968-b14036f184fe.png">



**app dockerfile**

```
FROM node AS app

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install -g npm@7.20.6

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]

FROM node:alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install -g npm@7.20.6

COPY --from=app /usr/src/app /usr/src/app

ENTRYPOINT [ "seed-database.sh" ]

EXPOSE 3000

CMD ["node", "app.js"]

```

**db dockerfile**

```
FROM mongo:latest

WORKDIR /usr/src/db/

COPY ./mongod.conf /etc/

EXPOSE 27017

CMD ["mongod"]

```

**Docker_Compose.yaml**

```
version: "3.9"
volumes:
  db:
services:
  db:
    container_name: db
    image: mongo:4.0.4
    ports:
      - "27017:27017"
    volumes:
      - ./db/mongod.conf:/etc/mongod.conf

  app:
    container_name: app
    build: ./app
    restart: always
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=mongodb://172.18.0.2:27017/posts
    depends_on:
      - db

```

**Python script to automate seeding**

```
import os 

os.system("sudo docker compose up -d")
os.system("sudo docker exec -it app node seeds/seed.js")

```

