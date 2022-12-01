# Duke Rainforest Drone API

## Overview

- This API project is used for adding and retrieiving drone data.
- You can create a flight, add metadata, or upload photos.
- You can run this project locally, in which case it will create an SQLite database.
- When it's run remotely on AWS, it connects to a MySQL database.
- The API supports token authentication. However, this has been disabled for most drone routes.

## Setup

0. Make sure you have the following things installed

   - Git
   - Python >= 3.7
   - MySQL (optional)

1. Clone this repository  
   `git clone https://github.com/caseyslaught/duke-biodiversity-api.git`  
   `cd duke-biodiversity-api`

2. Create a virtual environment using Python >= 3.7  
   `virtualenv venv`  
   `source venv/bin/activate` - Mac/Linux  
   `venv\Scripts\activate` - Windows

3. Install the dependencies
   `pip install -r requirements.txt`

4. Update the database  
   `python manage.py migrate`

5. Add the following environment variables

   - DUKE_RAINFOREST_AWS_ACCESS_KEY
   - DUKE_RAINFOREST_AWS_SECRET_KEY
   - DUKE_RAINFOREST_SECRET (production)
     - this is just a random string you can make up
   - DUKE_RAINFOREST_MYSQL_PASSWORD (production)
     - ask Martin for this
   - DUKE_RAINFOREST_MYSQL_HOST (production)
     - visit RDS on AWS to find this

6. Create a superuser  
   `python manage.py createsuperuser`
   - You can use the superuser to sign into the admin dashboard

## Admin dashboard

- You can use the admin dashboard to modify objects in the database
- It's located at [localhost:8000/admin](127.0.0.1:8000/admin) if running locally

## Making requests

- To add data, use POST.
- To retrieve data, use GET.
- For authenticated requests, add Authorization header.
  - ex. Authorization: Bearer <access_token>

## Amazon Web Services

- The API is currently hosted on AWS using Elastic Beanstalk
- Elastic Beanstalk is managed service that creates EC2 instances and load balancers under the hood
- A Cloudfront distribution sits in front of the Elastic Beanstalk project so that you can connect with the API over HTTPS; you can't setup HTTPS with Elastic Beanstalk alone
- Everything is located in the us-east-1 (N. Virginia) region

### Overview of all AWS services used

- Elastic Beanstalk: hosting API including EC2 server and load balancer
- Cloudfront: CDN for serving API over HTTPS
- RDS: MySQL database (_duke-rainforest-xprize_)
- S3: File storage for drone photos (_duke-rainforest-data_)

## Project structure

This is a Django project. There are a few _apps_ within the project, such as _account_ and _drone_.

- The _account_ app contains things related to signing in.
  - Most of this functionality is not important right now as most routes do not have authentication enabled.
- The _drone_ app contains stuff related to drones, obviously.
  - serializers.py determine how data is converted into Python objects, or how Python objects are returned via HTTP.
  - models.py describes what the relational database looks like. This is an Object-Relational-Mapper. Changes made here will be relected in the SQLite or MySQL database.
  - views.py handle most of the functionality of the app. There are basically a function that you run when you request a certain URL.
  - urls.py contains mappings of URLs to views.
