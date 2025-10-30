**🎬 Movie Rater Backend (Django + REST Framework)**

This is the backend API for the Movie Rater project — built using Django and Django REST Framework.
It powers the movie rating web app, providing APIs for authentication, movies, categories, and user ratings.

**🧩 Tech Stack**

1) Backend Framework: Django 5
2) API Framework: Django REST Framework (DRF)
3) Database: MySQL 
4) CORS Handling: django-cors-headers
5) Authentication: Token-based Auth (DRF)

**📂 Project Structure**
movie_rating-app/
│
├── api/                   # API app containing views, models, serializers
├── movierater/            # Main Django project (settings, urls, wsgi)
├── media/                 # Uploaded media files
├── static/                # Static files after collectstatic
├── venv/                  # Virtual environment
├── manage.py              # Django CLI management file
├── requirements.txt       # Python dependencies

**⚙️ Setup Instructions**

1️⃣ Clone the repository
1) git clone https://github.com/krutikapenkar/movie-rating-app.git 
2) cd movie-rater-backend

2️⃣ Create and activate virtual environment
1) python -m venv venv
2) source venv/bin/activate   # On Mac/Linux
3) venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
1) pip install -r requirements.txt

4️⃣ Install dependencies
1) change database settings in Settings.py

5️⃣ Apply migrations and create superuser
1) python manage.py makemigrations
2) python manage.py migrate

Create a superuser
1) python manage.py createsuperuser

6️⃣ Run development server
1) python manage.py runserver
