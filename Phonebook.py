import ast


class phonebook:

    def __init__(self) -> None:
        self._book = dict()

    def __repr__(self):
        return f"{self._book.items()}"

    def add(self, entries):

        # this allows the input to retain its set data structure easily
        data = ast.literal_eval(input('Enter entries: '))

        while len(data) != int(entries):
            data = input(f'Enter {entries} entries: ')

        for x in data:
            self._book.update({x[0]: x[1]})

        return self

    def query(self, query):
        if self._book.get(query):
            return self._book.get(query)
        else:
            return "Not Found"


book = phonebook()

book.add(3)
# added {(33,'red'), (44,'blue'), (55,'purp')}

print(book)
print(book.query(33))
print(book.query(89))
