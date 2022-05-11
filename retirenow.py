from mastodon import Mastodon
import secret

    # Then login. This can be done every time, or use persisted.
def posting(msg):
    mastodon = Mastodon(
        access_token = secret.token,
        api_base_url = secret.url
    )
    # mastodon.status_post(msg, visibility = 'private')
    mastodon.toot(msg)

if __name__ == "__main__":
    posting('hello world!')

