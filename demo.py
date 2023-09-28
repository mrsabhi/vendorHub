import json

file_path = 'data.json'


# Load the JSON file
def load_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


# Read the JSON file using an input key
def read_json_file_with_key(file_path, key):
    data = load_json_file(file_path)
    if data is not None:
        value = data.get(key, "Key not found in the JSON file")
        return value


input_key = input("Enter a key: ")

result = read_json_file_with_key(file_path, input_key)

print(result)
