import csv


def writerFile(users):
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'given_name', 'family_name', 'middle_name', 'nickname', 'preferred_username', 'profile',
                      'picture', 'website', 'email', 'email_verified', 'gender', 'birthdate', 'zoneinfo', 'locale',
                      'phone_number', 'phone_number_verified', 'address']
        writer = csv.DictWriter(csvfile, fieldnames)

        users = format_data_users(users)

        writer.writeheader()
        for user in users:
            writer.writerow(
                user
            )


def format_data_users(users):
    for index, user in enumerate(users):
        user = {
            "name": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'name'), ''),
            "given_name": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'given_name'), ''),
            "family_name": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'family_name'), ''),
            "middle_name": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'middle_name'), ''),
            "nickname": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'nickname'), ''),
            "preferred_username": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'preferred_username'),
                ''),
            "profile": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'profile'),
                            ''),
            "picture": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'picture'),
                            ''),
            "website": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'website'),
                            ''),
            "email": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'email'),
                          ''),
            "email_verified": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'email_verified'), ''),
            "gender": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'gender'),
                           ''),
            "birthdate": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'birthdate'), ''),
            "zoneinfo": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'zoneinfo'), ''),
            "locale": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'locale'),
                           ''),
            "phone_number": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'phone_number'), ''),
            "phone_number_verified": next((attribute['Value'] for attribute in user['Attributes'] if
                                           attribute['Name'] == 'phone_number_verified'), ''),
            "address": next((attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'address'),
                            ''),
        }
        users[index] = user

    return users


if __name__ == '__main__':
    writerFile([])
