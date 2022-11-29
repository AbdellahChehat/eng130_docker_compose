# Automating full pipeline 

**Using  :**

- GitHub
- WebHooks
- Jenkins 
- Docker (Images, compose, etc)
- AWS 

 The task at hand is to build a Jenkins Pipeline to automate Docker Build and Push to docker hub. Then pull and deploy onto an EC2 instance.


 Dependencies needed. 

- Install Jenkins 
- AWS account 
- Create a key pair 


### Job List : 


### Set up webhook on GitHub: 


1. In your GitHub repository go to Settings and select Webhooks

2. Select Add webhook

3. For the Payload URL you must put http://<jenkins-url>/github-webhook/

4. For Content Type select application/json.


### Job 1: Pull code from dev branch and test 

- Discard old builds
    - Max # of build : 3
- Github project
    - Insert GitHub HTTPS repo link
- Source Code Management
    - Insert SSH Repo link
    - Provide the SSH private Key which should be connected to your Github repo in Credentials
    - Branches to build : */dev
- Build Triggers
    - Select GitHub hook trigger for GITScm polling
- Build
    - Execute shell: test code
- Post-build Actions
    - Select the Projects to build
    - Trigger only if build is stable




   