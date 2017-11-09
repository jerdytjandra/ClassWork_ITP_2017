class Author(object):
    def __init__(self, name, email, gender):
        self.name = name
        self.email = email
        self.gender = gender

    def author_info(self):
        print("Author:", self.name, "\n\tEmail:", self.email, "\n\tGender:", self.gender)
