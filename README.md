# BLOGS

## AUTHOR
- [Derrick Kiprop](https://github.com/derrokip34)

## PROJECT DESCRIPTION
This is an app where one can sign up and post blogs from different categories. A user can also update or delete their posts and comment on the posts

## SETUP AND USAGE INSTRUCTIONS
### Prerequisites
- A web browser
- Github account
- Terminal
- Python3.6
- Text editor software

#### Clone or download the zip file of this repository
- Clone by typing in the following command `git clone https://github.com/derrokip34/Blog.git`
- If you've downloaded the zip extract it in your preferred destination

#### Navigate into the project directory

#### Install python3.6 if not yet installed

##### Install virtual environment by typing the following command
`python3.6 -m venv --without-pip virtual`

#### Activate virtual environment
`source virtual/bin/activate`

#### Install pip
`curl https://bootstrap.pypa.io/get-pip.py | python`

#### Install dependencies by typing the following command
`pip install -r requirements.txt`

#### Edit your start.sh file with your MAIL_USERNAME,MAIL_PASSWORD & SECRET_KEY as follows
- `export MAIL_USERNAME={your email address}`
- `export MAIL_PASSWORD={your email password}`
- `export SECRET_KEY={your secret key}`

`python3.6 manage.py server`

#### Change the config_name in manage.py file to development
`app = create_app('config_name')`

#### Run the command below to make the start.sh file executable
`chmod a+x start.sh`

#### Run the following command in your terminal
`./start.sh`

#### Open 'http://127.0.0.1:5000/' in your browser and enjoy your app

## [BLOG Live site](https://blog-34.herokuapp.com/)

## BDD
### Input required
- User's details when signing up, logging in, or updating their profile
- Posts

### Behaviour
- The app will store a user's details in a database whe signing in and fetch them when logging in
- Posts posted will also be stored in a database

### Output
- The app will display a all posts on the home page and the posts page
- The app will also display a user's profile info on their profile page

## TECHNOLOGIES USED
- HTML
- CSS
- Bootstrap
- Material Design Bootstrap
- Python3.6
- Markdown
- Heroku
- PostgreSQL

## BUGS
There are no known bugs at the moment
In case of any bugs contact me at derrokip34@gmail.com

## LICENSE & COPYRIGHT INFORMATION
[MIT License](https://github.com/derrokip34/Blog/blob/master/license.md)
