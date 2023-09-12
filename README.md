# Cloud Programming

Welcome to the cloud programming project where I deployed a machine learning model on AWS Cloud Platform to make request and predictions via an IP address! This project showcases the process of building a machine learning model for predicting Titanic passenger survival and deploying it as a web application using Flask and Docker on AWS.


## In this project, I've accomplished the following:

1. **Machine Learning Model**: I developed a machine learning model using Python and libraries like pandas, scikit-learn, and Jupyter Notebook. This model predicts whether a Titanic passenger survived or not based on various features.

2. **Flask Web Application**: created a web application using Flask, a Python web framework. This application allows users to interact with the machine learning model by providing passenger information and receiving predictions.

3. **Docker Containerization**: I containerized the Flask web application using Docker. This approach ensures that the application and its dependencies are encapsulated in a consistent environment, making it easy to deploy.

4. **Amazon ECR**: I pushed the Docker images to Amazon Elastic Container Registry (ECR). ECR is a managed container registry service in AWS that allows us to store, manage, and deploy Docker images.

5. **AWS EC2 Deployment**: I finally deployed the Docker container on an Amazon EC2 instance, which provides scalable and resizable compute capacity. This instance runs the Flask web application and makes it accessible via a public IP address.


Clone the repository to a computer locally.

```bash
git clone https://github.com/TumisangF/Habit-Tracking-App.git
```
Navigate to the habit tracker directory.
```bash
cd Habit-Tracking-Application
```

## Usage
Follow the following steps to run the application

1. Run the following script
```python
python .\cli.py
```
As soon as the application launches, a menu of options will be displayed. Actions such as viewing habits, adding habits, crossing off to-do items, and obtaining analytics are all available for selection.

Observe the prompts and enter the information required as instructed by the application's interface.

For running the tests run the following commmand
```python
python -m pytest .\habitTrackerTest.py
```

Have fun monitoring your behavior and evaluating your development!


## Contributing

Contributions are appreciated! Follow the instructions in the CONTRIBUTING.md file if you want to contribute to the Habit Tracker project.

## Acknowledgements

I would like convey my profound appreciation  to Dr. Max Pumperla for his advice, expertise, and ongoing assistance throughout the project. The design and functioning of the application has been significantly affected by his helpful feedback.


I thank IU International University of Applied Sciences for allowing me the chance to work on this project and for the tools and information  provided to me .

##License
This project is licensed under the MIT License.

