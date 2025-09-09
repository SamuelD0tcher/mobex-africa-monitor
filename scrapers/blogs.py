from newspaper import Article
import requests
from bs4 import BeautifulSoup

def search_blogs(query):
    url = f'https://news.google.com/rss/search?q={query.replace(" ", "+")}'
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code != 200:
            return {'results': [], 'error': 'Google News RSS is unreachable.'}
        soup = BeautifulSoup(resp.content, 'xml')
        items = soup.find_all('item')
        results = []
        for item in items[:5]:
            results.append({
                'title': item.title.text,
                'url': item.link.text
            })
        return {'results': results, 'error': None}
    except Exception as e:
        return {'results': [], 'error': f'Blogs/News error: {str(e)}'}
