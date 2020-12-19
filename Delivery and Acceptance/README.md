### Prerequisites
Please run the .ipynb file in ML Modelling and evaluation folder, once a .pkl is generated in the following folder, the following procedure can be used.

### Project Structure
This project has four major parts :
1. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
2. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

### Running the project

1. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

2. Navigate to URL http://localhost:5000


3. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
