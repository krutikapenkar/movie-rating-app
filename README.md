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
git clone https://github.com/krutikapenkar/movie-rating-app.git
cd movie-rater-backend

2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Install dependencies
change database settings in Settings.py

5️⃣ Apply migrations and create superuser
python manage.py makemigrations
python manage.py migrate

Create a superuser
python manage.py createsuperuser

6️⃣ Run development server
python manage.py runserver
