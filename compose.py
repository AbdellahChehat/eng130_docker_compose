import os 

os.system("sudo docker compose up -d")
os.system("sudo docker exec -it app node seeds/seed.js")