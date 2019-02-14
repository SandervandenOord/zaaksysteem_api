# Testcase Zaaksysteem Backend

Python Flask Api to use a simple calculator
Returns JSON with the result of the calculation

Can be reached via: 0.0.0.0:5000/calculator/5 + 3

Build Docker image as follows:
docker build -t calcdock .
docker run -p 5000:5000 calcdock

Swagger documentation for api in following directory:
0.0.0.0:5000/api/v1

