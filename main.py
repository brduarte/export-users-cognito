from services import cognitoService, csvService


def start():
    response = cognitoService.request_aws_cognito(user_pool_id='us-east-1_2CEagqIiL')

    if 'Users' not in response:
        print('Pool de usuário vazio')

    csvService.writerFile(response['Users'])

    while 'PaginationToken' in response:
        response = cognitoService.request_aws_cognito(user_pool_id='us-east-1_2CEagqIiL',
                                                      pagination_token=response['PaginationToken'])
        csvService.writerFile(response['Users'])


if __name__ == '__main__':
    start()
