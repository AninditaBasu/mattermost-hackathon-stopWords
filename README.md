# mattermost-hackathon-stopWords
demo for an app that finds occurrences of non-inclusive language in the Mattermost documentation

## How it works

The code in `stopWords.py` file in this repo uses the GitHub `search API` to look for words specified in the `.static\wordList.txt` file and reports the findings through the `.\templates\stopWordsSearch.html` file.

## Customisation

You can supply your own list of words (and phrases) by editing the `.static\wordList.txt` file. Specify each word or phrase on a new line.

You can specify which GitHub repo to search by  replacing `mattermost/docs` with the repo name of your choice in line 10 of the `stopWords.py` file.