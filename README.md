## Blogly
### Using Python, SQL, SQLAlchemy, and Flask
This little app is basic blog functionality - where a user can create a profile (no authentication provided), create a post, and give the post different tags.
Each model (user, post, tag) can be edited and saved to the database, and can also be deleted. The purpose of this exercise was to practice various table relationships with SQL. As of now there isn't any error handling besides basic form validations.

Each main app functionality is tested within the Tests folder.

#### **models.py** 
This file contains the db _models_ used within the app, including a model for User, Post, Tag, and the M2M table PostTag, which maps various tags to one post.

#### **app.py** 
This file contains the routes and view functions for the app.

#### **templates**
This folder contains all of the html pages accessible through the app, including a _base.html_ from which each other page inherits.

#### **Tests**
This folder contains two files - **test_app.py**, which tests the GET and POST routes and view functions from **app.py**, and **test_models.py**, which runs tests on the models from **models.py**

### Note: There is a **seed.py** file included. If you'd like to play around with the functionality, be sure to seed the database.