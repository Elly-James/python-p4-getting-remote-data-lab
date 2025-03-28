import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
        

    def load_json(self):
        response_body = self.get_response_body()
        converted_data = json.loads(response_body)
        return converted_data
    


if __name__ == "__main__":
    URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    requester = GetRequester(URL)
    response_body = requester.get_response_body()
    converted_data = requester.load_json()
    print(f"Response Body: {response_body}")
    print(f"Converted Data: {converted_data}")







# below is implemented for error handling 




# import requests
# import json

# class GetRequester:

#     def __init__(self, url):
#         self.url = url

#     def get_response_body(self):
#         try:
#             response = requests.get(self.url)
#             response.raise_for_status()  # Raises an HTTPError for bad responses
#             return response.text
#         except requests.exceptions.RequestException as e:
#             print(f"An error occurred: {e}")
#             return None

#     def load_json(self):
#         try:
#             response_body = self.get_response_body()
#             if response_body:
#                 return json.loads(response_body)
#             return None
#         except json.JSONDecodeError as e:
#             print(f"JSON decoding error: {e}")
#             return None

# if __name__ == "__main__":
#     URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
#     requester = GetRequester(URL)
#     response_body = requester.get_response_body()
#     converted_data = requester.load_json()
#     print(f"Response Body: {response_body}")
#     print(f"Converted Data: {converted_data}")
