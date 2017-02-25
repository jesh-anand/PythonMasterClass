from blog_site.terminal_blog.database.database import Database

__author__ = 'Prajesh Ananthan'


class Post(object):
    def __init__(self, blog_id, title, content, author, date, post_id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.post_id = post_id

    def save_post_in_mongo_db(self):
        Database.insert(collection='posts', data=self.json)

    def json(self):
        return {
            'id': self.post_id,
            'blog_id': self.blog_id,
            'title': self.title,
            'post_id': self.post_id,
            'created_date': self.created_date,
            'content': self.content
        }
