"""
The module to create DSL accounts per user.
----------------------------------------------

This module gets a txt file, with following headers,
`username, lastname, firstname, email`, and returns a
tab seperated txt file to supply to `AddUser` function.

Following line is what needs to be run with "root" user 
rights:

```sh
AddUser -u users.txt
```
"""

import pandas as pd


def create_users_file(raw_file):
    """
    Gets users file and saves a `tab seperated` file. May
    require to update header order based on raw_file.
    """
    # read it by order username, lastname, firstname, email
    df = pd.read_csv(raw_file, header=None)

    # sort it by proper order - username, firstname, lastname, email
    df.sort_values(by=[0,2,1,3], axis=0, inplace=True) 

    # save it to file
    df.to_csv('user.txt', sep='\t', encoding='utf-8', index=False, header=False)
