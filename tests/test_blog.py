import unittest
from app.models import Blog,User
from flask_login import current_user
from app import db

class TestBlogs(unittest.TestCase):

    def setUp(self):
        self.user_Derrick = User(username="derrokip34",password="zlatan",email="derrokip@gmail.com")
        self.new_blog = Blog(blog_title="Batman",blog_content="I am the night",category="Movie",user=self.user_Derrick.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.blog_title,"Batman")
        self.assertEquals(self.new_blog.blog_content,"I am the night")
        self.assertEquals(self.new_blog.category,"Movie")
        self.assertEquals(self.new_blog.user_id,self.user_Derrick.id)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())>0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        pitches = Pitch.query.all()
        self.assertTrue(len(blogs)==1)