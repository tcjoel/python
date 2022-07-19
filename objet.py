# a class is a bluprint to that each user will use
# object is an implementation of this class

class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently work as a {self.current_job_title}. You can contact them at {self.email}")

class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author
    def get_post(self):
        print(f"post: {self.message} The author of this message is {self.author}")

app_user_one = User("nn@nn.com", "Nana Janashia", "pwd1", "DevOps Engineer")
app_user_one.get_user_info()
app_user_two = User("mbop@yahoo.com", "mbopy pass", "pwd2", "Cloud Engineer")
app_user_two.get_user_info()

first_post = Post( "tomorrow is my birthay and I will go to London", "Jean Tabi")
first_post.get_post()