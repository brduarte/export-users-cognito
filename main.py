from services import cognitoService, csvService


def start():
    user_pool_id = str(input('Enter the cognito user pool id: '))
    response = cognitoService.request_aws_cognito(user_pool_id)
    number_users = len(response['Users'])
    print_display(number_users)

    csvService.delete_file(user_pool_id)

    if 'Users' not in response:
        print('Empty user pool')

    csvService.writerFile(response['Users'], file_name=user_pool_id, created_header=True)

    while 'PaginationToken' in response:
        response = cognitoService.request_aws_cognito(
            user_pool_id,
            pagination_token=response['PaginationToken']
        )
        csvService.writerFile(response['Users'], file_name=user_pool_id)
        number_users += len(response['Users'])
        print_display(number_users)

    print('File delivered to project root folder with user pool name', user_pool_id, sep=': ')


def print_display(total_value):
    print(f'Migrated Users [{total_value}]')


if __name__ == '__main__':
    start()
