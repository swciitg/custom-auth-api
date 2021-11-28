This repository is the RESTful implementation(python-Django) of the frequently used Authetication Services in SWC IITG projects.
Please keep the secret keys discreet and put them in a separate file and add that file in .gitignore. Collect the respective credential files from the Core team to do the testing locally.

> Outlook Authentication Service
----> This service is implemented using the graph API of MSAuth, the reference can be found here: https://docs.microsoft.com/en-us/graph/tutorials/python?tutorial-step=1
----> To run this service locally, you need to get the oauth_setting.yml file from the Core Team and place it in the outlookAuth directory (alongside the auth_helper.py file)