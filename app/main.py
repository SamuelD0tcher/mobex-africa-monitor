from flask import Flask, render_template

from scrapers.twitter import search_twitter
from scrapers.reddit import search_reddit
from scrapers.blogs import search_blogs

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        query = "Mobex Africa"
        twitter_data = search_twitter(query)
        reddit_data = search_reddit(query)
        blog_data = search_blogs(query)
        return render_template(
            'dashboard.html',
            twitter=twitter_data['results'],
            twitter_error=twitter_data['error'],
            reddit=reddit_data['results'],
            reddit_error=reddit_data['error'],
            blogs=blog_data['results'],
            blogs_error=blog_data['error']
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

