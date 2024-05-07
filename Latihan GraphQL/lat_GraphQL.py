import graphene

class Book(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()


data=[
    {"id":"1", "title":"bukuku 1"},
    {"id":"2", "title":"bukuku 2"},
    {"id":"3", "title":"bukuku 3"},
    {"id":"4", "title":"bukuku 4"},
    {"id":"5", "title":"bukuku 5"}
]

class Query(graphene.ObjectType):
    books = graphene.List(Book)
    book = graphene.Field(Book)

    def resolve_book(self, info):
        print(info.schema)
        return Book(id="1", title='my eyes are two')
        #return Book(id=data[2]["id"], title=data[2]["title"])
    
    def resolve_books(self, info):
        return[
            # Book(id="1", title="Buku 1 milia"),
            # Book(id="2", title="Buku 2 milia"),
            # Book(id="3", title="Buku 3 milia")
        
            Book(id=i['id'], title=i['title'])for i in data
        ]

schema= graphene.Schema(query=Query)

q ='''
{
    book {
        id
        title
    }
}
'''
s ='''
{
    books {
        id
        title
    }
}
'''
#result=schema.execute(q)
# result=schema.execute(s)
# print(result.data)

# print(data[3]["id"])
for i in data:
    print(i)
