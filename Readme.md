# Tablature API

THE ISSUE
---
Many musicians will eventually get to a stage where they do not remember every song they know, and at the slightest jog of memory can recall how to play it in its entirety, the purpose of this program is to help with just that by storing a list of sheet music in a convient and easy to access location. Tabs are also a fantastic way to start learning an instrument so this will be an excellent resource for new and up and coming musicians. Additonally, by allowing users to submit their own tabs, we are also enabling the community to contrubute and share their favroute music with eachother, inspire new and creative ideas, and help the next generation of asspiring musicians. This application aims to help users learn new songs on either Guitar or Bass Guitar with diffrent string setups and tunings, and to catalogue learned or learning songs for musicians. Tabs can also be searched for either via their artist_id, album_id, instrument_id, or tuning_id. Depending on the users contributions and comendations, "Standard" users will be able to View Song Tablature, "Uploader" users will be allowed to submit tabs to be uploaded to the database for checking and approval by our "Moderator" users. Additionally, Moderator users will be able to Edit and Remove Song Tablature as required. 

The Nitty-Gritty
---
This application will be usuing PostgreSQL due to my experience with this particular DBMS, and although its reading speed is relativly low when compared to other database systems, its abiity to process and store complex data types can be helpfull for mapping out song tablature. We will also be using Object-Relational-Mapping, or an ORM, is a technique implmented into programs that interacts with a DBMS, that allows us to use our prefered programming language, in this case Python, Making it easier for our code to be dry, updated and maintained. It also lets us quiery our database with Python commands as appose to SQL and gives us access to more automated tools like database table creation, seeding and dropping, and helps to reinforce our MVC archetecture.


We will also require external packages and resources, here is a list of all the third party services that are rquired for this API:  
* Bycrypt - Allows us to hash our passwords and add an extra layer of security  
* JWT - Allows us to have user authentication and give unique bearer tokens based on user information    
* Marshmallow - An ORM framework, allowing us to convert datatypes betweeen Python and PostgresQL    
* SQLAlchemy - Provides an ORM as well as a data mapper that allows us to generate SQL statments, works in hand with Psycopg2  
* Psycopg2 - PostgeSQL to Python database adpater, Used to Send SQL statments to the database  

ERD and explination of models:
---
![ERD](/docs/ERD.png)
For the models we will use in the database, The, Artist must exist first, an Album can not exist without an Artist, and a Tab can not exist with an Album. There can be Multiple Tabs to an Album, and multiple Albums to an Artist. However, there can NOT be multiple Artists to an Album, or multiple Albums to a Tab. Each Tab model will also relate to no more than one Tuning and Instrument model, while both Tuning and Instrument models can relate to multiple Tabs. Users will also be able to Upload multiple Tabs, but a Tab can not relate to multiple Users.

List of all endpoints with the API and expected responses:
---
![API Endpoint Diagram](/docs/Endpoints.png)

Planning and Deployment
---
You can track the development of the API here: https://github.com/Reaver113/Tablature_API

OR

See the Planning and Task Tracking here : https://trello.com/b/ToQThaKi/tablatureapi  
Final Trello board screenshot:
![Trello Board](/docs/dev_init.png)