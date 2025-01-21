class Article:

    def __init__(self, **kwargs):
        self.filds = kwargs

    def get_filds(self):
        return list(self.filds.keys())

    def get_values(self):
        return list(self.filds.values())
