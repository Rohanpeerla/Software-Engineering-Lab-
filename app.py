from flask import Flask, render_template

app = Flask(__name__)

news_articles = [
    {"title": "Global Markets Crash", "category": "Business", "image": "screenshot_2025_04_04_210538.png", "url": "/news/1"},
    {"title": "AI is Changing the World", "category": "Technology", "image": "screenshot_2025_04_04_210320.png", "url": "/news/2"},
    {"title": "Elections 2025: Latest Updates", "category": "Politics", "image": "screenshot_2025_04_04_210755.png", "url": "/news/3"},
]

@app.route("/")
def home():
    return render_template("index.html", articles=news_articles)

@app.route("/news/<int:news_id>")
def news_detail(news_id):
    article = news_articles[news_id - 1]
    return render_template("news_detail.html", article=article)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)