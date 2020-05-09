from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,SelectField,PasswordField
from wtforms.validators import Required,Email,EqualTo

class Blogform(FlaskForm):
    blog_title = StringField('Blog title',validators=[Required()])
    content = TextAreaField('Post your blog',validators=[Required()])
    category = SelectField('Blog Category',choices=[('Sports-Blog','Sports'),('Travel-Blog','Travel'),('Fitness-Blog','Fitness'),('Fashion-Blog','Fashion'),('Food-Blog','Food'),('Political-Blog','Politics')],validators=[Required()])
    submit = SubmitField('Submit your post')

class UpdateForm(FlaskForm):
    first_name = StringField('Your first name')
    last_name = StringField('Your last name')
    bio = TextAreaField('Tell us something about you')
    submit = SubmitField('Update bio')

class CommentForm(FlaskForm):
    comments = TextAreaField('Leave a comment below',validators=[Required()])
    submit = SubmitField('Submit your comment')