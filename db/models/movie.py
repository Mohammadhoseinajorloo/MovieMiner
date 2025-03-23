class TypeEngin:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"TypeEngin(name={self.name}"


class Integer(TypeEngin):
    def __init__(self):
        super().__init__("Integer")


class String(TypeEngin):
    def __init__(self, length=None):
        super().__init__("String")
        self.length = length


class Float(TypeEngin):
    def __init__(self):
        super().__init__("Float")


class DateTime(TypeEngin):
    def __init__(self):
        super().__init__("DateTime")


class Column:
    def __init__( self, column_type, **kwargs):
        self.column_type = column_type # Integer, String, Float, DateTeim
        self.constraints = kwargs

    def __repr__(self):
        return f"Column(type={self.column_type}, constraints={self.constraints}"


class Movie:
    id = Column(Integer, primary_key=True)


movie = Movie()
print(movie.id)
