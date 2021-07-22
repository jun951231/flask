from scraping.models.dataset import Dataset
from scraping.models.service import Service


class View(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, bugs, melon):
        service = self.service
        this = self.preprocessing(bugs,melon)
        print(f'The Type of This is {type(this.bugs)}')
        print(f'The head of Bugs is \n {this.bugs.head(2)}')
        print(f'The head of Melon is \n {this.melon.head(2)}')

    def preprocessing(self, bugs, melon): -> object:
        service = self.service
        this = self.dataset
        this.bugs = service.new_model(bugs)
        this.melon = service.new_model(melon)
        return this


if __name__ == '__main__':
    view = View()
    view.modelint('bugs.csv', 'melon.csv')
