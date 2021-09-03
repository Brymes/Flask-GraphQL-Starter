import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import Test

#Types
class Test(SQLAlchemyObjectType):
    class Meta:
        model = Test

# Mutation
class Test(graphene.Mutation):
    class Arguments:
        pass
        
    return Test(status=status, msg=message)pass

class Mutations(graphene.ObjectType):
    test = Test.Field()

class Query(graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutations)
