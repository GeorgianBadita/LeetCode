# https://leetcode.com/problems/encode-and-decode-tinyurl/

import random


class Codec:

    alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    url_map = {}

    def get_random_string(self):
        return ''.join([self.alphabet[random.randrange(0, len(self.alphabet))] for i in range(6)])

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.get_random_string()
        while key in self.url_map:
            key = self.get_random_string()

        self.url_map[key] = longUrl
        return 'http://www.tinyurl.com/' + key

    def decode(self, shortUrl: str) -> str:
        return self.url_map[shortUrl.split('/')[-1]]
