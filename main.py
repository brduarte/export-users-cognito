from services import cognitoService


def start():
    response = cognitoService.request_aws_cognito(user_pool_id='us-east-1_2CEagqIiL')

    if 'Users' not in response:
        print('Pool de usuário vazio')

    manipulate_users(response['Users'])

    while 'PaginationToken' in response:
        response = cognitoService.request_aws_cognito(user_pool_id='us-east-1_2CEagqIiL',
                                                      pagination_token=response['PaginationToken'])
        manipulate_users(response['Users'])


def manipulate_users(users):
    print(len(users))
    for user in users:
        print(user)


if __name__ == '__main__':
    start()
