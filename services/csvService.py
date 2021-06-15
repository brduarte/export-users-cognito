import csv


def writerFile(users, created_header=False):
    with open('users.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'given_name', 'family_name', 'middle_name', 'nickname', 'preferred_username', 'profile',
                      'picture', 'website', 'email', 'email_verified', 'gender', 'birthdate', 'zoneinfo', 'locale',
                      'phone_number', 'phone_number_verified', 'address']

        writer = csv.DictWriter(csvfile, fieldnames)
        users = format_data_users(users)

        if created_header:
            writer.writeheader()

        writer.writerows(users)


def format_data_users(users):
    for index, user in enumerate(users):
        user = {
            "name": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'name'), ''),
            "email": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'email'), ''),
            "gender": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'gender'), ''),
            "locale": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'locale'), ''),
            "profile": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'profile'), ''),
            "picture": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'picture'), ''),
            "address": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'address'), ''),
            "website": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'website'), ''),
            "zoneinfo": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'zoneinfo'), ''),
            "nickname": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'nickname'), ''),
            "birthdate": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'birthdate'), ''),
            "given_name": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'given_name'), ''),
            "family_name": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'family_name'), ''),
            "middle_name": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'middle_name'), ''),
            "phone_number": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'phone_number'), ''),
            "email_verified": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'email_verified'), ''),
            "preferred_username": next(
                (attribute['Value'] for attribute in user['Attributes'] if attribute['Name'] == 'preferred_username'),
                ''),
            "phone_number_verified": next(
                (attribute['Value'] for attribute in user['Attributes'] if
                 attribute['Name'] == 'phone_number_verified'), ''),
        }
        users[index] = user

    return users
