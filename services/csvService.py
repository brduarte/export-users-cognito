import csv


def writerFile(users=''):
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'given_name', 'family_name', 'middle_name', 'nickname', 'preferred_username', 'profile',
                      'picture', 'website', 'email', 'email_verified', 'gender', 'birthdate', 'zoneinfo', 'locale',
                      'phone_number', 'phone_number_verified', 'address', 'updated_at', 'cognito:mfa_enabled',
                      'cognito:username']
        writer = csv.DictWriter(csvfile, fieldnames)



if __name__ == '__main__':
    writerFile()
