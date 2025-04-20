# main.py

import urllib.request
import json
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Send a chat input to Azure ML endpoint.")
    parser.add_argument('-m', '--message', type=str, required=True, help='Message to send')
    args = parser.parse_args()

    # Prepare the input data
    input_data = {
        "chat_history": [],
        "chat_input": args.message
    }

    body = str.encode(json.dumps(input_data))

    # Your Azure endpoint and API key
    url = 'https://dvillacreses1234-8208-ggexp.eastus2.inference.ml.azure.com/score'
    api_key = ''

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    # Make the request
    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        res = result.decode('utf-8')
        print(json.loads(res)['chat_output'])
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        print(error.info())
        print(error.read().decode("utf8", 'ignore'))

if __name__ == "__main__":
    main()
