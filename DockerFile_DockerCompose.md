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

