from blog_site.terminal_blog.database.database import Database
from blog_site.terminal_blog.model.blog import Blog

__author__ = 'Prajesh Ananthan'


class Menu(object):
    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}!".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one(Blog.COLLECTION_NAME, query={'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo_in_blog_object(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title: ")
        description = input("Enter description: ")
        blog = Blog(author=self.user, title=title, description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog_posts()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(Blog.COLLECTION_NAME, query={})
        for blog in blogs:
            print("ID: {}\nTitle: {}\nAuthor: {}\n\n".format(blog['id'], blog['title'], blog['author']))

    "content"
    def _view_blog_posts(self):
        blog_to_see = input("Enter the id of the blog you want to see: ")
        blog = Blog.from_mongo_in_blog_object(blog_to_see)
        posts = blog.get_post()
        for post in posts:
            print("ID: {}\nTitle: {}\nContent: {}\nAuthor: {}\nDate: {}\n\n".format(post['id'], post['title'],
                                                                                    post['content'], post['author'],
                                                                                    post['created_date']))
