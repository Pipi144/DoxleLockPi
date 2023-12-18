import requests
import sys
import json
address = "http://192.168.1.109:9000"
def verify_data(data):
    print("DATA TYPE:", type(data))
    print("DATA:",data)
    dump = json.dumps(data)
    data_json = json.loads(dump)
    print("DATA JSON:", data_json)
    if data:
        api_url = f"{address}/qr/verify/"
        try:
            print("DATA TYPE:", type(data_json))
            response = requests.post(api_url, json = data_json, headers=head)
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
    
    
        
