import json
import requests
import csv

import os

if not os.path.exists("data"):
 os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter

    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            repoUrl = 'https://api.github.com/repos/' + repo

            # Get source languages from repo
            repoDetails, _ = github_auth(repoUrl, lsttokens, 0)
            languagesUrl = repoDetails['languages_url']
            languageObj, _ = github_auth(languagesUrl, lsttokens, 0)
            sourceLanguages = list(languageObj.keys())

            commitsUrl = repoUrl + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break
            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                filesjson = shaDetails['files']
                author = shaDetails['commit']['author']['name']
                timestamp = shaDetails['commit']['author']['date']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    # Split the extension and grab it
                    fileExtension = os.path.splitext(filename)[1]

                    # Check file extension and if language is a source language (specifically for rootbeer repository)
                    if (fileExtension == '.java' and 'Java' in sourceLanguages) or (fileExtension == '.kt' and 'Kotlin' in sourceLanguages):
                        # for each file that has been touched, instead of
                        # incrementing a count, append the author and timestamp
                        # to the filename such that each file in the dict is
                        # associated with authors and their respective
                        # timestamps
                        dictfiles[filename] = dictfiles.get(filename, [])
                        dictfiles[filename].append((author, timestamp))
                        print(f"{filename} - Author: {author}, Timestamp: {timestamp}")
            ipage += 1
    except:
        print("Error receiving data")
        exit(0)
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
# lstTokens = ["fd02a694b606c4120b8ca7bbe7ce29229376ee",
                # "16ce529bdb32263fb90a392d38b5f53c7ecb6b",
                # "8cea5715051869e98044f38b60fe897b350d4a"]
lstTokens = ["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"]

dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictfiles)))

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/file_' + file + '.csv'
authorOutput = 'data/authors_' + file + '.csv'

rows = ["Filename", "Touches"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)
for filename, count in dictfiles.items():
    # count consists of a list of authors and timestamps
    # Getting the length returns the total times a file has been touched
    rows = [filename, len(count)]
    writer.writerow(rows)
fileCSV.close()

rows = ["Filename", "Author", "Timestamp"]
authorCSV = open(authorOutput, 'w')
writer = csv.writer(authorCSV)
writer.writerow(rows)
for filename, count in dictfiles.items():
    for author, timestamp in count:
        rows = [filename, author, timestamp]
        writer.writerow(rows)
fileCSV.close()

print('Files data written to:', fileOutput)
print('Authors data written to:', authorOutput)
