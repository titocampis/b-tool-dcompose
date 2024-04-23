def retrieve_secret(secret_path):
    '''Method to retrieve the value of a secret'''
    try:
        with open(secret_path, 'r') as secret_file: return secret_file.read().strip()
    except FileNotFoundError as e:
        print(f"Error: Secret file not found: {e.filename}")
    except Exception as e:
        print(f"Error: An error ocurred parsing the secrets files\nError: {e}")
