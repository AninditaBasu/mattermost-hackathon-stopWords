# mattermost-hackathon-stopWords

PoC for an app that finds occurrences of non-inclusive language in the Mattermost documentation. [See demo on Heroku](https://mattermost-hackathon-stopwords.herokuapp.com/).

## Why was it made

To participate in the Mattermost 2019 hackathon :slightly_smiling_face:

The aim is to look at the Mattermost documentation and find (and review and, if needed, remove or rephrase) words and phrases that might not promote accessibility, diversity, or inclusiveness.

The app can also be used as a consistency checker for spellings (for example, `plug-in` vs. `plugin` or `color` vs. `colour`) and phrasing (for example, `we recommend` vs. `it is recommended`).

## How it works

The code in `stopWords.py` file uses the GitHub `search API` to look for words specified in the `.static\wordList.txt` file and reports the findings through the `.\templates\stopWordsSearch.html` file.

## How to use

1. Clone this repo, and customise the files to your requirements:

   - `.static\wordList.txt`: Supply your own list of words and phrases by editing the . Specify each word or phrase on a new line, and add an explanation about why the word or phrase is undesirable and what can be used in its stead. The format is: `<word or phrase>: <explanation or suggestion> new_line`
   - `stopWords.py`: Specify which GitHub repo to search by replacing `mattermost/docs` with the repo name of your choice in line 10.

2. Create an app on Heroku and link your cloned repo to that app.
