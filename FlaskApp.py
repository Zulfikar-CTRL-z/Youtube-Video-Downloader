from flask import Flask, render_template, request
from pytubefix import YouTube
from pytubefix.exceptions import RegexMatchError



app =Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/search", methods=['POST'])
def search():
    url = request.form['url']



    if request.method == "POST":
        try:
            link = YouTube(str(url))
            return render_template("search.html", titl=link.title,tmbn=link.thumbnail_url, url=url)
        except RegexMatchError:
            return render_template("search.html", error="Invalid Url !!! ")


@app.route("/download", methods=['POST'])
def download():
    url = request.form
    link = YouTube(str(url))
    if request.method == "POST":
        ytStream = link.streams.get_lowest_resolution()
        ytStream.download(filename="YTdownloader.mp4")
        return render_template("download.html")

if __name__=="__main__":
    app.run(port=8000, debug=True)