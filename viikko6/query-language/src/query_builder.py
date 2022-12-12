from matchers import And, PlaysIn, HasAtLeast, All, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, query_builder = All()):
        self.query_builder = query_builder

    def build(self):
        return self.query_builder

    def playsIn(self, team):
        return QueryBuilder(And(self.query_builder, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.query_builder, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.query_builder, HasFewerThan(value, attr)))
    
    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))