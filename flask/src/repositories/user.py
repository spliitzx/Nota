""" Defines the User repository """

from models import User
from sqlalchemy.orm import load_only
import bcrypt
import string
import random


class UserRepository:

    @staticmethod
    def create(username, email, password):
        """ Create a new user """
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        secret = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))

        user = User(username=username, email=email, password=hashed, secret=secret)

        user.save()

        ret = {
            'username': user.json['username'],
            'email': user.json['email'],
            'token': user.generateToken()
        }

        return ret
