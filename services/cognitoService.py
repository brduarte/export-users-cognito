import boto3
from boto3 import exceptions


def request_aws_cognito(user_pool_id, pagination_token=""):
    client = boto3.client('cognito-idp')

    if any(pagination_token):
        response = client.list_users(
            UserPoolId=user_pool_id,
            Limit=60,
            PaginationToken=pagination_token
        )
    else:
        response = client.list_users(
            UserPoolId=user_pool_id,
            Limit=60,
        )

    return response
