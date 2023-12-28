from django.contrib.auth.hashers import BasePasswordHasher

class PlainTextHasher(BasePasswordHasher):
    algorithm = 'plain_text'

    def encode(self, password, salt):
        return password

    def verify(self, password, encoded):
        return password == encoded

    def safe_summary(self, encoded):
        return {'algorithm': self.algorithm, 'encoded': encoded}

    def harden_runtime(self, password, encoded):
        pass

    def identify_hasher(self, encoded):
        return self.algorithm
