import requests
from rich.progress import Progress
import time

startTime = time.time()
successList = []
failList = []
messageList = []

readEventType = 'endpoint'
readHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

with open('/Users/sbachta/Workspace/py-random/resources/collection.txt') as file:
    appFile = file.read().splitlines()

with Progress() as progress:
    task = progress.add_task("[green]Collecting data...", total=len(appFile))
    while not progress.finished:

        for line in appFile:
            appUrl = f'http://localhost:8080/{line}'
            response = requests.get(appUrl, headers=readHeaders)

            if response.status_code in (200, 201):
                if response.json()['messages'] is not None:
                    for message in response.json()['messages']:
                        if message['throwError'] is False:
                            messageList.append(message['name']+'\n')
                            successList.append(line+'\n')
                            break
                else:
                    failList.append(line+'\n')
            else:
                failList.append(line+'\n')

            progress.update(task, advance=1)

publishFile = open('/Users/sbachta/Workspace/py-random/resources/publish.txt', 'w')
publishFile.writelines(messageList)
publishFile.close()

successFile = open('/Users/sbachta/Workspace/py-random/resources/success.txt', 'w')
successFile.writelines(successList)
successFile.close()

failFile = open('/Users/sbachta/Workspace/py-random/resources/fail.txt', 'w')
failFile.writelines(failList)
failFile.close()

endTime = time.time()
elapsedTime = endTime - startTime
print(f'Success count: {len(successList)}')
print(f'Fail count: {len(failList)}')
print(f'Elapsed time: {elapsedTime/60:.2f} seconds')

