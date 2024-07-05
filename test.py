import requests
from requests.auth import HTTPBasicAuth

# SharePoint site and authentication configuration
username = 'your-username'
password = 'your-password'
sharepoint_site = 'https://mdigital.sharepoint.com/'
folder_path = 'sites/LSABAPTeam/Shared Documents/YourFolder'
api_endpoint = f"/_api/web/GetFolderByServerRelativeUrl('{folder_path}')/Files"

# Fetch the files from SharePoint folder
def fetch_sharepoint_files(sharepoint_site, api_endpoint, username, password):
    headers = {
        'Accept': 'application/json;odata=verbose'
    }
    response = requests.get(f'{sharepoint_site}{api_endpoint}', headers=headers, auth=HTTPBasicAuth(username, password))
    response.raise_for_status()
    return response.json()

# Main function
def main():
    try:
        # Fetch the files from SharePoint folder
        files_data = fetch_sharepoint_files(sharepoint_site, api_endpoint, username, password)
        print("Files data fetched.")

        # Process the files data
        for file in files_data['d']['results']:
            print(f"File Name: {file['Name']}, File URL: {file['ServerRelativeUrl']}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
