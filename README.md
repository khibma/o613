# o613

A python flask app that talks to the Clash Royale API

Semi operational @ https://o613.azurewebsites.net/

## Steps to create and deploy

https://www.jamessturtevant.com/posts/Deploying-Python-Website-To-Azure-Web-with-Docker/#add-a-dockerfile

Deploy Python API Azure Containers: https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python

Azure outbound IP Address: https://docs.microsoft.com/en-us/azure/app-service/app-service-ip-addresses

Clash Royale Developer API: https://developer.clashroyale.com

docker dashboard: https://cloud.docker.com/swarm/khibma/repository/docker

Updating Python code in docker: https://stackoverflow.com/questions/47938864/how-to-update-docker-images

# Docker updates
```
Start the windows docker service
Run from commmand:
  docker build -f Dockerfile -t o613:latest .
  docker images
  docker tag ### khibma/o613
  docker push khibma/o613
```