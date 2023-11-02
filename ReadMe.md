# Classroom Website

This ongoing project is a web platform built using the Django framework that is meant to help organize the classroom experience. It includes features like a communal wall for posts, multimedia lessons, and graded multiple choice questions. Each lesson contains videos and text, followed by interactive quizzes that offer up to three attempts. Students can track their progress with individual lesson grades, while teachers can monitor their students' performance. The site also features classroom enrollment by allowing teachers to create classes and provide students with unique access codes to use to be placed in their virtual classrooms.

## Demo

[Website](https://dariacasey.pythonanywhere.com/)

## About

The website is actively under development. Currently, it has most of the essential functionality implemented, but I plan on implementing more specifically for the teacher account types. This includes features where they can create their own lesson, assign due dates, and analyze classroom statistics as well as individual student statistics. The user interface is undergoing a complete redesign with the focus of optimizing user-friendliness and giving the site a more modern/sleek aesthetic.

## Features
- Current: 
    - Login/registration 
    - Student/teacher user account types 
    - Posts & comments 
    - New post indicator 
    - Create/join classes 
    - Lessons with videos 
    - Multiple choice questions 
    - Grade log 

- Upcoming: 
    - Modern user friendly UI 
    - Classroom/student statistics 
    - Ability to create custom lessons 
    - Due dates 
    

## Installation
Pre-requisites: \
    - Python (3.11.4)\
    - Pip (Package manager)
```bash
# 1. Clone the repository
git clone https://github.com/dariacasey/ClassroomSite.git

# 2. Navigate to the project directory
cd ClassroomSite

# 3. Install dependencies (Pillow, django-ckeditor python-decouple)
pip install  

# 4. Run the server and view the site on your local host 
python manage.py runserver
