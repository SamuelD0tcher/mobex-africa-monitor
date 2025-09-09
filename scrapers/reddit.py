import praw

def search_reddit(query):
    try:
        reddit = praw.Reddit(
            client_id='06xaH4aCPwi3Rxiu-p3T8A',
            client_secret='O2DgmHkt2-pjB1mmA663VDaSxfnWjg',
            user_agent='mobex-africa-monitor by u/Mysterious_Shower339'
        )
        results = []
        for submission in reddit.subreddit('all').search(query, limit=5):
            results.append({
                'title': submission.title,
                'url': submission.url
            })
        return {'results': results, 'error': None}
    except Exception as e:
        return {'results': [], 'error': f'Reddit error: {str(e)}'}
