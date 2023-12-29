# Classroom Website

This ongoing project is a web platform built using the Django framework that is meant to help organize the classroom experience. It includes features like a communal wall for posts, multimedia lessons, and graded multiple choice questions. Each lesson contains videos and text, followed by interactive quizzes that offer up to three attempts. Students can track their progress with individual lesson grades, while teachers can monitor their students' performance. The site also features classroom enrollment by allowing teachers to create classes and provide students with unique access codes to use to be placed in their virtual classrooms.

## Demo
The UI has been changed since launching this. The core functionalities are mostly the same, but more have been implemented. The live site will be updated soon.
[Website](https://dariacasey.pythonanywhere.com/)

## About

The website is actively under development. Currently, it has most of the essential functionality implemented, but I plan on implementing more specifically for the teacher account types. This includes features where they can create their own lesson, assign due dates, and analyze classroom statistics as well as individual student statistics. The user interface is undergoing a complete redesign with the focus of optimizing user-friendliness and giving the site a more modern/sleek aesthetic.

## Features
- Login/registration 
- Student/teacher user account types 
- Posts & comments 
- New post indicator 
- Create/join classes 
- Lessons with videos 
- Multiple choice questions 
- Grade log
- Classroom grade statistics
 
## Visual Overview 
Discussion Wall: 
<img width="1440" alt="Screenshot 2023-12-29 at 5 41 03 PM" src="https://github.com/dariacasey/ClassroomSite/assets/128617643/e62a4cbc-3ea0-479c-8d3c-5385df739f88">

Lesson Gallery: 
<img width="1440" alt="Screenshot 2023-12-29 at 5 34 39 PM" src="https://github.com/dariacasey/ClassroomSite/assets/128617643/47ba9989-2503-4096-bff9-97a34b96ceb4">

Multiple Choice Questions: 
<img width="1440" alt="Screenshot 2023-12-29 at 5 39 51 PM" src="https://github.com/dariacasey/ClassroomSite/assets/128617643/3fe977dd-88b2-4177-a0c0-4696e59ba21e">

Post Detail: 
<img width="1440" alt="Screenshot 2023-12-29 at 5 44 00 PM" src="https://github.com/dariacasey/ClassroomSite/assets/128617643/ea5f1a5f-c29c-443e-85c2-b9e6455df593">

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
