from blog_site.terminal_blog.database.database import Database
from blog_site.terminal_blog.model.blog import Blog

__author__ = 'Prajesh Ananthan'

Database.initialize()
blog = Blog(author='Prajesh Ananthan', title='First blog title', description='Sample blog post')
blog.new_post()
blog.save_to_mongo()

from_database = Blog.get_content_from_mongo_in_blog_object(blog.id)
print(from_database.get_post())
