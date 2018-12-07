

class DomainSpecific:
    def __init__(self, text):
        self.quotes = (text.count("\'") + text.count("\"")) // 2
        self.links = text.count('http') // 2
    
    def __str__(self):
        result = 'Total Quoted Phrases: ' + str(self.quotes) + '\n'
        result += 'Total Link Count: ' + str(self.links)
        return result

    def to_list(self):
        return [self.quotes, self.links]
