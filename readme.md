## Setup:

Refer to this guide to setup your Python environment:
https://developers.google.com/admin-sdk/directory/v1/quickstart/python

Create a project and enable the API:
https://developers.google.com/workspace/guides/create-project

Create credentials:
https://developers.google.com/workspace/guides/create-credentials

Make sure to download the Credentials as a JSON file when prompted and put the JSON file into the directory and rename it to `credentials.json`

Run this to install all requirments
`pip install -r requirements.txt`

## Use:

Simply run the script in your favorite IDE.
A browser tab will open asking you to login to a google account with the appropriate priveleges to access the Google API.

## Result:

The script will dump two files. One called "ListOfGroups.csv" and one called "GroupsAndMembersList.csv".

## Shoutout to:

https://github.com/naseemkullah/google-group-members-list-python

https://github.com/jmathai-google/all-groups-in-customer
