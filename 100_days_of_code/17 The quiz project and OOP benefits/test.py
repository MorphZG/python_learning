class User:
    "simple user class"

    def __init__(self, user_id, username):
        print('User being created...')
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        '''add followers to user and following to self'''
        user.followers += 1
        self.following += 1


user_1 = User('001', 'Zoran')
user_2 = User('002', 'Jack')


user_1.follow(user_2)
print(user_1.followers, user_2.followers)
print(user_1.following, user_2.following)

#tags: practice