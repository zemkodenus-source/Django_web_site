# Django Link Manager

A web application where registered users can store and manage their personal links.
Users can make their link collection public and browse links shared by other users.

## Features

- User registration and login
- Password reset via email
- Add, edit, and delete personal links
- Make your link collection public or private
- Browse public link collections of other users
- Bilingual interface (English / Ukrainian)

## Tech Stack

- Python / Django
- PostgreSQL
- HTML / CSS

## Getting Started

### Requirements

- Python 3.x
- PostgreSQL

### Installation

```bash
git clone https://github.com/zemkodenus-source/Django_web_site.git
cd Django_web_site
pip install -r requirements.txt
```

Create a `.env` file with your database credentials, then run:

```bash
python manage.py migrate
python manage.py runserver
```

Open in browser: [http://127.0.0.1:8000/en/home](http://127.0.0.1:8000/en/home)