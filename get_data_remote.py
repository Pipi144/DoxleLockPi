import requests
import sys
import json
address = "http://192.168.1.109:8000"

def verify_data():
    api_url = f"{address}/getKey"
    try:
        response = requests.get(api_url)
        response.raise_for_status() #Raise exception for HTTP non 2--
        
        
        api_result = response.json()
        print("API RESULT:", api_result)
        return api_result
    except requests.exceptions.RequestException as e:
        print(f"APT REQUEST FAILED: {e}")
        return False
      
if __name__ == "__main__":

    verify_data()