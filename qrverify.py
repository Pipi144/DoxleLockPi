import requests
import sys
import json
address = "http://192.168.1.109:8000"
def verify_data(data):
    result = data.get("name")
    if result:
        api_url = f"{address}/qr/verify/{result}"
        try:
            response = requests.get(api_url)
            response.raise_for_status() #Raise exception for HTTP non 2--
            
            
            api_result = response.json()
            print("API RESULT:", api_result)
            return api_result
        except requests.exceptions.RequestException as e:
            print(f"APT REQUEST FAILED: {e}")
            return False
    else:
        return False
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("data passed in:", )
        sys.exit(1)

    json_data = sys.argv[1]
    serialized_data = json.loads(json_data)

    verify_data(serialized_data)
    
    
        
