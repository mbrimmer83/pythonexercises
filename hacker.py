import json
import md5

accounts = open('accounts.json', 'r')
users = json.loads(accounts.read())
accounts.close()

common_word = open('common_words.txt')
words = common_word.read().split('\n')
common_word.close()

decrypted_passwords = {}
decrypted_accounts = {}

def pass_cracker():
    for word in words:
        m = md5.new()
        m.update(word)
        encrypted_password = m.hexdigest()
        decrypted_passwords.update(encrypted_password:{'common_word': word, 'encrypted_password': encrypted_password})


        # for account in users
        #     the_user_account_pass = account['user']
        #     if account['password'] == password['user']['encrypted_password']:


pass_cracker()
print decrypted_passwords
