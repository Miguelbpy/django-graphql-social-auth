import graphene

import graphql_social_auth

from . import mixins
from .testcases import GraphQLSocialTestCase


class SocialAuthTests(mixins.SocialAuthTestsMixin, GraphQLSocialTestCase):

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.relay.SocialAuth.Field()

    def execute(self, input):
        query = '''
        mutation SocialAuth($input: SocialAuthInput!) {
          socialAuth(input: $input) {
            social {
              uid
              extraData
            }
            clientMutationId
          }
        }'''

        return self.client.execute(query, input=input)


class SocialAuthJWTTests(mixins.SocialAuthTestsMixin,
                         mixins.SocialAuthJWTTestsMixin,
                         GraphQLSocialTestCase):

    class Mutations(graphene.ObjectType):
        social_auth = graphql_social_auth.relay.SocialAuthJWT.Field()

    def execute(self, input):
        query = '''
        mutation SocialAuth($input: SocialAuthJWTInput!) {
          socialAuth(input: $input) {
            social {
              uid
              extraData
            }
            token
            clientMutationId
          }
        }'''

        return self.client.execute(query, input=input)
