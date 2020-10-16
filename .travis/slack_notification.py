#!/usr/bin/env python3

# author: greyshell

import requests
import json

if __name__ == '__main__':

    wekbook_url = 'https://hooks.slack.com/services/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'

    data = {
        'text': '> Test Python',
        'username': 'bot',
    }

    response = requests.post(wekbook_url, data=json.dumps(
            data), headers={'Content-Type': 'application/json'})

    print('Response: ' + str(response.text))
    print('Response code: ' + str(response.status_code))