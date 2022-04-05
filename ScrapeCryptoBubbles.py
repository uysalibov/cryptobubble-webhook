import requests

class CryptoBubbles:

    # cryptobubbles.net backend api url
    CRYPTOBUBBLES_API_URL = "https://cryptobubbles.net/backend/data/bubbles1000.usd.json"

    def __init__(self, best_of:int = 1000):
        self.best_of = best_of
        self.session = requests.Session()

    def get_data(self) -> list:
        """
            Get top 1000 coin from CryptoBubbles
        """
        raw_data = self.session.get(CryptoBubbles.CRYPTOBUBBLES_API_URL)
        return sorted(raw_data.json(), key=lambda coin: coin["rank"])[:self.best_of]

    def sort_data(self, data:list) -> list:
        """
            Sort scraped data by hourly performance score
        """
        return sorted(data, key=lambda coin: coin["performance"]["hour"], reverse=True)