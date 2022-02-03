### 1.Deployment with Docker

Docker is used to ship our application with separate interface, for quick delivery. The Client system need not have to install the packages manually required to run the application , instead can run docker and pull the software as images from the docker-hub.

#### Docker file

This file has necessary steps to be performed when docker image is built and used to run the docker container. Here is the sample docker file for the FASTAPI project 

#### Docker image

These are templates for creating container,  images needed for the application are pulled from the docker-hub.

#### Docker container

Docker container is used, when we want to ship our application that runs in the same way across different OS platforms. Here the code with its package dependencies are added in the requirements.txt file and is put inside the docker container with docker images. So the client system can run the docker container with all the packages installed and infrastructure are pulled from docker-hub as images.

#### Docker Installation

Download and install the docker desktop for your OS from the link [link](https://www.docker.com/products/docker-desktop)

Check if the installation is successful with the following command from the terminal.

```docker -v```

**Build docker image with the following command**

Navigate to the directory, where the Dockerfile is present and run the following command

```dockerfile
docker build -t <docker-image-name> .
```

**Run the docker container with the following command**

Navigate to the directory, where the Dockerfile is present and run the following command

```dockerfile
docker run --name <docker-container-name> -p 8080:8080 <docker-image-name>
```

#### 

### 2.Available API Operations

The FASTAPI has the following set of POST APIs for inserting data into the PostgreSQL database.



### 3.Query Data

