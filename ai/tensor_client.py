import json
import numpy as np
import requests
# The server URL specifies the endpoint of your server running the linear_model
# model with the name "linear_model" and using the predict interface.
SERVER_URL = 'http://localhost:8501/v1/models/linear-model:predict'

def main():
  predict_request = '{"instances" : [ [0.0], [1.0], [2.0] ]}'
  # Send few actual requests and report average latency.
  total_time = 0
  num_requests = 10
  index = 0
  for _ in range(num_requests):
    response = requests.post(SERVER_URL, data=predict_request)
    response.raise_for_status()
    total_time += response.elapsed.total_seconds()
    prediction = response.json()
    print (prediction)
  print('Prediction class: {}, avg latency: {} ms'.format(
      np.argmax(prediction), (total_time * 1000) / num_requests))

if __name__ == '__main__':
  main()

