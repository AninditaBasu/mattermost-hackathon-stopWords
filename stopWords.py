from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def stop_words():
    URL_prefix = 'https://api.github.com/search/code?q='
    URL_suffix = '+repo:jekyll/jekyll/docs/_docs/installation'

    reportfile = open('./templates/stopWordsSearch.html', 'w')
    reportfile.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">')
    reportfile.write('<link rel="stylesheet" type="text/css" href="../static/bootstrap.min.css">')
    reportfile.write('<link rel="stylesheet" type="text/css" href="../static/common.css">')
    reportfile.write('<script src="../static/jquery.min.js"></script>')
    reportfile.write('<script src="../static/popper.min.js"></script>')
    reportfile.write('<script src="../static/bootstrap.min.js"></script>')
    reportfile.write('<title>Stop-words Search</title></head>')
    reportfile.write('<body><div class="container"><h1>Stop-words Search</h1>')

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
    try:
        reportfile.write('<p class="lead">Consider reviewing the occurrences of the following words in the documentation.</p><hr/>')
        wordpos = 0
        for word in wordlist:
            url_string = URL_prefix + word + URL_suffix
            r = requests.get(url_string)
            json_data = json.loads(json.dumps(r.json()))
            print(json_data)
            if len(json_data['items']) != 0:
                print(word)
                reportfile.write('<div class="container">')
                reportfile.write('<h2>' + word + '</h2>')
                print(explainlist[wordpos])
                reportfile.write('<p>' + explainlist[wordpos] + '</p>')
                print(json_data['total_count'], 'instances of', word)
                reportfile.write('<p>' + str(json_data['total_count']) + ' instances of <mark>' + word + '</mark> found in the following files:</p>')
                reportfile.write('<ul>')
                for line in json_data['items']:
                    for k, v in line.items():
                        if k == 'path':
                            print(v)
                            reportfile.write('<li>' + v + '</li>')
                print('--------\n')
                reportfile.write('</ul>')
                reportfile.write('</div>')
                reportfile.write('<hr/>')
            wordpos = wordpos + 1
    except:
        reportfile.write("<p class='text-danger'>&gt;&gt;&gt;&gt;&gt; If you're seeing these lines, it means you've hit the API rate limits for GitHub search and the Stopwords search was abandoned.</p>")
        #reportfile.write("<p class='text-danger'>Had the search been completed, you would've got an output shown in the following image.</p>")
        #reportfile.write('<img src="../static/stopWords.png"/>')
        reportfile.write("<p class='text-danger'>Maybe choose a smaller documentation repository for your search?</p>")
        reportfile.write("<p class='text-danger'>But then, this is just a demo and you get the general idea, I hope? &lt;&lt;&lt;&lt;&lt;")
    reportfile.write("</div></body>")
    reportfile.write("</html>")
    reportfile.close()
    return render_template('stopWordsSearch.html')

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
        #app.run()
