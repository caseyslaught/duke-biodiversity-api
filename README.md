# Duke Biodiversity Monitoring API

## Overview

- This API is used for add observations from drones, camera traps, and audio recorders.
- This API is also used to serve these observations a frontend or client application.
- This API will soon forward new observations to ArcGIS Online.
- This API implements token authentication. Users send their email and password and receive an access/refresh token pair.

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
   - DUKE_RAINFOREST_MYSQL_HOST (production)

## Make a request

- To add data, use POST.
- To retrieve data, use GET.
- For authenticated requests, add Authorization header.
  - ex. Authorization: Bearer <access_token>

## Add dummy data

Adding dummy data will create random objects in your database to use for testing.  
`python manage.py add_dummy_data`

## Push changes to AWS

- Open a pull request in Github
- Ask Casey to review and update - casey.slaught@duke.edu
