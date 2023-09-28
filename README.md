Installation Process
To install this app please follow this below steps:

Run Backend
1. Create a virtual environment `virtualenv venv`
2. And activate it `source venv/bin/activate`(for ubuntu) `venv\Scripts\activate`(for windows)
3. Then change the directory to server/ and install dependencies `pip install -r requirements.txt`
4. Migrate to database `python manage.py migrate`
5. Now run the server `python manage.py runserver`

Run Front-end
1. Change the directory to client/
2. Install dependencies `npm install`
3. Now start the server `npm run dev`