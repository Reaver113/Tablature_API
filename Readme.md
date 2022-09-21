# Tablature API

R1 - This application aims to help users learn new songs on either Guitar or Bass Guitar (with plans for additional instruments at a later date) and to catalogue learned or learning songs for musicians. Depending on the users contributions and comendations, Initiate users will be able to View and Track Song Tablature, Advanced users will be allowed to submit tabs to be uploaded to the database for checking and approval by our Modderation users. Additionally, Modderation users will be able to Edit and Remove Song Tablature as required. 

R2 - Many musicians will eventually get to a stage where they do not remember every song they know, and at the slightest jog of memory can recall how to play it in its entirety, the purpose of this program is to help with just that by tracking what songs a user has learned or are currently learning and storing it in a convient location. Tabs are also a fantastic way to start learning an instrument so this will be an excellent resource for new and up and coming musicians. Additonally, by allowing users to submit their own tabs, we are also enabling the community to contrubute and share their favroute music with eachother, inspire new and creative ideas, and help the next generation of asspiring musicians.

R3 - This application will be usuing PostgreSQL due to my experience with this particular DBMS, and although its reading speed is relativly low when compared to other database systems, its abiity to process and store complex data types can be helpfull for mapping out song tablature.

R4 - Object-Relational-Mapping, or an ORM, is a technique implmented into programs that interact with a DBMS, that allows us to use our prefered programming language, in this case Python, Making it easier for out code to be dry, updated and maintained. It also lets us quiery our database with Python commands as appose to SQL and gives us access to more automated tools like database table creation, seeding and dropping, and helps to reinforce our MVC archetecture,

R6 - Attachd ERD of the Application:
![ERD](/docs/ERD.png)