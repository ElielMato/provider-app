from werkzeug.security import generate_password_hash, check_password_hash

class Security:

    @staticmethod
    def encrypt_password(password:str) -> str:
        password_encrypted = generate_password_hash(password.password)
        return password_encrypted

    @staticmethod
    def check_password(password_encrypted, plain_password) -> bool:
        return check_password_hash(password_encrypted, plain_password)
    #'scrypt:32768:8:1$6xyt9YBhaD5Y5nWw$6c16f427790c3b108ff478ad36b47a991cfd152fb53b50e7e0cef17411d9f89ddfcea40b53ec177d02d1f272f7504bbbe3d5d4f6fc2fbaec68133db7ca350da1' == 'scrypt:32768:8:1$6xyt9YBhaD5Y5nWw$6c16f427790c3b108ff478ad36b47a991cfd152fb53b50e7e0cef17411d9f89ddfcea40b53ec177d02d1f272f7504bbbe3d5d4f6fc2fbaec68133db7ca350da1