Setup NodeApp in Docker container

1. Create new folder 
2. Create new Dockerfile in folder
3. Add any file you want to that folder (in this case app and environment folders)
To the Dockerfile add the following script:
  ```
  FROM nginx

  LABEL MAINTAINER=eng130_abdellah

  COPY app /home/
  COPY environment /home/

  EXPOSE 80
  EXPOSE 3000

  RUN apt-get update
  RUN apt-get install -y
  RUN apt-get install software-properties-common -y
  RUN apt-get install npm -y

  CMD ["nginx", "-g", "daemon off;"]
  WORKDIR /home/app
  RUN npm install
  CMD ["npm", "start"]
  ```
4. Build the node app
5. docker build -t nodeapp .
6. Run the app to make sure it works locally
7. docker run -d -p 80:3000 
8. Stop the container
9. docker stop ID
10. Commit the changes we made to "node"
11. docker commit ID abdullah12321/eng130_abdellah:latest
12. Push the changes
13. docker push abdullah12321/eng130_abdellah:latest
14. To check if all is good
15. Delete the image
16. docker rm ID -f
17. Run the image from DockerHub
18. docker run -d -p 80:3000 abdullah12321/eng130_abdellah:latest
19. If you now go to "localhost" in your browser, you should see your app