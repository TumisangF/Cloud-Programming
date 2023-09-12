# Cloud Programming

Welcome to the cloud programming project where I deployed a machine learning model on AWS Cloud Platform to make request and predictions via an IP address! This project showcases the process of building a machine learning model for predicting Titanic passenger survival and deploying it as a web application using Flask and Docker on AWS.


## In this project, I've accomplished the following:

1. **Machine Learning Model**: I developed a machine learning model using Python and libraries like pandas, scikit-learn, and Jupyter Notebook. This model predicts whether a Titanic passenger survived or not based on various features.

2. **Flask Web Application**: created a web application using Flask, a Python web framework. This application allows users to interact with the machine learning model by providing passenger information and receiving predictions.

3. **Docker Containerization**: I containerized the Flask web application using Docker. This approach ensures that the application and its dependencies are encapsulated in a consistent environment, making it easy to deploy.

4. **Amazon ECR**: I pushed the Docker images to Amazon Elastic Container Registry (ECR). ECR is a managed container registry service in AWS that allows us to store, manage, and deploy Docker images.

5. **AWS EC2 Deployment**: I finally deployed the Docker container on an Amazon EC2 instance, which provides scalable and resizable compute capacity. This instance runs the Flask web application and makes it accessible via a public IP address.

6. **Public Access**: The web application is made available to the public via a public IPv4 DNS address. Users can access the application through a web browser and make predictions.


## The application will then use the machine learning model to predict whether the passenger survived or not.
**Public Access**: The web application is available on this address: http://ec2-16-171-146-27.eu-north-1.compute.amazonaws.com:5000/.


## Follow these steps to replicate the project:

1. **Clone the Repository**: Clone this repository to your local environment.
   
```bash
git clone https://github.com/TumisangF/Cloud-Programming.git
```
2. **Build the Docker Image**: Build the Docker image for the web application using the provided `Dockerfile`.
```bash
# Change to the ML directory
cd '.\Machine Learning Web Application\'

# Build the docker image
docker build -t titanic-image:latest .

# To test the image. You can run the container locally.
docker run -p 5000:80 titanic-image:latest
```

3. **Push to AWS ECR**: Push the Docker image to your AWS ECR repository.
```bash
# Authenticate with ECR
aws ecr get-login-password --region AWS_REGION | docker login --username AWS --password-stdin AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com

#Tag the Docker Image
docker tag YOUR_IMAGE_NAME:TAG AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com/REPO_NAME:TAG

#Push the Docker Image
docker push AWS_ACCOUNT_ID.dkr.ecr.AWS_REGION.amazonaws.com/REPO_NAME:TAG

# Verify Image Push
aws ecr describe-images --repository-name REPO_NAME
```

## Follow these steps to replicate the Cloud Architecture:

**Change to the AWS Cloud Architecture**:
   The directory contains a dedicated IaC files that use Terraform tool to enable the clould archicture to be managable and replicable
```bash
cd '\AWS Cloud Architecture\'
```

## Making predictions.
**To predict whether a passenger survived or not using Machine learning:***
Follow this link: http://ec2-16-171-146-27.eu-north-1.compute.amazonaws.com:5000/


## Contributing

Contributions are appreciated! Follow the instructions in the CONTRIBUTING.md file if you want to contribute to the Habit Tracker project.

## Acknowledgements

I thank IU International University of Applied Sciences for allowing me the chance to work on this project and for the tools and information  provided to me .

##License
This project is licensed under the MIT License.

