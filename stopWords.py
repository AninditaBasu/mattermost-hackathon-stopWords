from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def stop_words():
    URL_prefix = 'https://api.github.com/search/code?q='
    URL_suffix = '+repo:mattermost/docs'

    reportfile = open('./templates/stopWordsSearch.html', 'w')
    reportfile.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF - 8"><title>Mattermost Hackathon - Stop Words Search</title></head><body><h1>Mattermost Hackathon - Stop Words Search</h1><p>Consider reviewing the occurrences of the following words in the Mattermost documentation</p><hr/>')

    fname = './static/wordList.txt'
    wordlist = []
    explainlist = []
    print("\n")
    print('Reading the word list ...\n')
    fwordlist = open(fname, 'r')
    for line in fwordlist:
        colon = line.find(':')
        word = line[0:(colon)]
        explain = line[(colon + 1):]
        explain = explain.rstrip()
        print(word)
        print(explain)
        wordlist.append(word)
        explainlist.append(explain)
    fwordlist.close()
    print(wordlist)
    print(explainlist)
    x = len(wordlist)
    print('\nNo. of words and phrases to search for: ', x)
    wordpos = 0
    for word in wordlist:
        print(word)
        reportfile.write('<p><mark>' + word + '</mark></p>')
        print(explainlist[wordpos])
        reportfile.write('<p>' + explainlist[wordpos] + '</p>')
        url_string = URL_prefix + word + URL_suffix
        r = requests.get(url_string)
        json_data = json.loads(json.dumps(r.json()))
        print(word, 'found in:')
        reportfile.write('<p><mark>' + word + '</mark> found in:</p>')
        reportfile.write('<ul>')
        for line in json_data['items']:
            for k, v in line.items():
                if k == 'path':
                    print(v)
                    reportfile.write('<li>' + v + '</li>')
        print('--------\n')
        reportfile.write('</ul>')
        reportfile.write('<hr/>')
        wordpos = wordpos + 1
    reportfile.write("</body>")
    reportfile.write("</html>")
    reportfile.close()
    return render_template('stopWordsSearch.html')

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
        #app.run()