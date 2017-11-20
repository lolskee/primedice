import requests

class BetError(Exception):
    pass

class PrimeDice:
    def __init__(self, api_key):
        self.BASE_URL = 'https://api.primedice.com/api/'
        self.api_key = api_key

    def get_user_info(self):
        """
        Get the user info associated with the provided api key.
        :return: request object containing user info
        """
        url = self.BASE_URL +'users/1?api_key=' + self.api_key
        req = requests.get(url)
        return req

    def make_bet(self, bet_amount, target_number=49.5, condition='<',
                 verbose=False, return_request=False):
        """
        Place a bet on PrimeDice.
        :param bet_amount: amount to wager in satoshis
        :param target_number: number targeting to get above or below, from 0 to 100
        :param condition: greater than or less than, string
        :param verbose: if True include print statements
        :param return_request: if True return request object
        :return: True if wager won, False if wager lost
                 (or requests object if return_request=True)
        """
        url = self.BASE_URL + 'bet?api_key=' + self.api_key
        payload = {
            'amount': str(bet_amount),
            'target': str(target_number),
            'condition': condition
        }
        req = requests.post(url, data=payload)
        if req.status_code == 200:
            if verbose:
                print("Bet successfully placed...")
                print("Target:", condition, target_number)
                print("Number Rolled:", req.json()['bet']['roll'])
                if req.json()['bet']['win']:
                    print("Wager won --- profit =", req.json()['bet']['profit'], "satoshi")
                elif not req.json()['bet']['win']:
                    print("Wager lost --- profit =", req.json()['bet']['profit'], "satoshi")
            if return_request:
                return req
            elif req.json()['bet']['win']:
                return True
            elif not req.json()['bet']['win']:
                return False
        else:
            raise BetError("An error occurred while placing your bet:", req.text)
