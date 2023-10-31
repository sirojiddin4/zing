E-Learning Management Tool
Project Overview
This is an e-learning management tool that helps educators to manage academic credits for students. The tool is built with Django and allows for tracking student progress, managing lesson credits, and analyzing academic performance within groups.

Features
Group Search: Enables the search for specific groups.
Credit Table: Displays the credit details of students in a particular group.
Credit Management: Allows educators to edit the credits of each student.
Performance Analysis: Sorts students based on credit percentages and average credits.
Installation
To get the project up and running on your local machine:

Clone the project repository.
Install the necessary Python and Django packages.
Run the Django migrations to create your database schema.

pip install django
python manage.py migrate

Usage
Start the Django development server with:

shell
Copy code
python manage.py runserver
Then navigate to the home page, and use the following endpoints:

/: The home page of the application.
/search_group/: To search and select a group.
/credit_table/<group_id>/: To view the credit table of a selected group.
/edit_credit/<student_id>/<group_id>/: To edit the credit details for a student.
Customization
The application can be customized to cater to different educational structures by modifying the Group, Lesson, Credit, and Student models as per the requirements.

Contributing
Contributions are welcome. Feel free to clone, modify, and make pull requests to this repository with your enhancements.

License
This project is open-source and available to anyone for any use, modification, or distribution without restriction.
