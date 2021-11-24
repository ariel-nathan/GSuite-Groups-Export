from __future__ import print_function
import pandas as pd

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/admin.directory.group.readonly'

groupIDList = []
FinalList = []

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('admin', 'directory_v1', http=creds.authorize(Http()))

def getGroupMembers(group):
    groupName = group[0]
    groupKeyID = group[1]

    request = service.members().list(groupKey=groupKeyID)
    response = request.execute()
    print(response)

    if response and 'members' in response:
        instances = response['members']
        for instance in instances:
            try:
                #print(instance['email'])
                FinalList.append([groupName,instance['email']])
            except:
                print("execption")
                pass
    else:
        #print('There are no members to list in this group.')
        pass
    df = pd.DataFrame(FinalList, columns=['Group', 'Member'])
    df.to_csv('GroupsAndMembersList.csv')
    print("Done")


def getGroupsList():
    groupList = []

    nextPageToken = None
    while True:
        results = service.groups().list(customer='my_customer', maxResults=200, pageToken=nextPageToken).execute()
        groups = results.get('groups', [])

        for group in groups:
            groupList.append([u'{0}'.format(group['email']),group['id']])

        nextPageToken = results.get('nextPageToken')
        if nextPageToken is None: 
            # We've reached the last page and there are no more groups
            break

    df = pd.DataFrame(groupList, columns=['Group','GroupKeyID'])
    df.to_csv('ListOfGroups.csv')
    print("Attempting to retrieve group members of each group")
    for group in groupList:
        getGroupMembers(group)

getGroupsList()