# Classroom Website

This ongoing project is a web platform built using the Django framework that is meant to help organize the classroom experience. It includes features like a communal wall for posts, multimedia lessons, and graded multiple choice questions. Each lesson contains videos and text, followed by interactive quizzes that offer up to three attempts. Students can track their progress with individual lesson grades, while teachers can monitor their students' performance. The site also features classroom enrollment by allowing teachers to create classes and provide students with unique access codes to use to be placed in their virtual classrooms.

## Demo

[Website](https://dariacasey.pythonanywhere.com/)
## Table of Contents

- [Project Name](#project-name)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Features](#features)
  - [Demo](#demo)
  - [Installation](#installation)

## About

The website is actively under development. Currently, it has most of the essential functionality implemented, but I plan on implementing more specifically for the teacher account types. This includes features where they can create their own lesson, assign due dates, and analyze classroom statistics as well as individual student statistics. The user interface is undergoing a complete redesign with the focus of optimizing user-friendliness and giving the site a more modern/sleek aesthetic.

## Features
Current: 
    - Login/registration 
    - Student/teacher user account types 
    - Posts & comments 
    - New post indicator 
    - Create/join classes 
    - Lessons with videos 
    - Multiple choice questions 
    - Grade log 

Upcoming: 
    - Modern user friendly UI 
    - Classroom/student statistics 
    - Ability to create custom lessons 
    - Due dates 
    

## Installation
1. Clone repository
   
```bash
# Clone the repository
git clone https://github.com/yourusername/your-repo.git

# Navigate to the project directory
cd your-repo

# Install dependencies
npm install  # or your package manager of choice


Pre-requisites: \
    - Python (3.11.4)\
    - Pip (Package manager)

Steps: \
    1. Extract content of zip file \
    2. Navigate to project directory 

     cd directory-where-extracted-project/djangoProject/website
\
    3. Create virtual environment 

        python -m venv env 
\
    4. Activate the environment \
        - Mac/Linux 

        source env/bin/activate 
\
        - Windows 

        source env/Scripts/activate 
\
    5. Install Django 

        - pip install Django 
\
    6. Install dependencies 

        pip install Pillow 
        pip install django-ckeditor 
        pip install python-decouple 
\
    7. Run the server and view the site on your local host 

        python manage.py runserver
