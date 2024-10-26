# **FlaskForge**

## **Description**

**FlaskForge** is a comprehensive web application built using the Flask framework. It demonstrates a complex project structure suitable for scalable and secure web development. The application includes user authentication, database interactions, modular blueprints, dynamic templates, and static file handling.

[ChatGPT o1 Link](https://chatgpt.com/share/66e36240-c588-8009-83f7-5f97101479be)

## **Features**

- **User Authentication**: Secure registration, login, and logout functionalities using `Flask-Login` and password hashing.
- **Database Integration**: Utilizes `SQLAlchemy` ORM for seamless interaction with a relational database.
- **Modular Structure**: Implements blueprints to organize the application into reusable and maintainable components.
- **Dynamic Templates**: Uses `Jinja2` templating engine for rendering dynamic HTML pages.
- **Static File Handling**: Serves CSS, JavaScript, and images to enhance the frontend experience.
- **Database Migrations**: Manages database schema changes with `Flask-Migrate`.

## **Project Structure**

```plaintext
FlaskForge/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── main/
│       │   └── index.html
│       └── base.html
├── migrations/
├── venv/
├── config.py
├── requirements.txt
└── run.py
```

## **Installation**

### **Prerequisites**

- **Python 3.6+** installed on your system.
- **Virtual Environment** package (`venv` or `virtualenv`).

### **Setup Instructions**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Vikranth3140/FlaskForge.git
   cd FlaskForge
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**

   - **Secret Key**: In `config.py`, set a secure `SECRET_KEY`.
     ```python
     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secure-secret-key'
     ```
   - **Database URI**: Configure the `SQLALCHEMY_DATABASE_URI` for your database.
     ```python
     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
     ```

5. **Initialize the Database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Running the Application**

   ```bash
   flask run
   ```

   Access the application at [http://localhost:5000](http://localhost:5000).

## **Usage**

- **Home Page**: Visit `/` or `/index` to view the homepage.
- **Register**: Navigate to `/auth/register` to create a new account.
- **Login**: Go to `/auth/login` to sign in.
- **Dashboard**: Access `/dashboard` after logging in to view user-specific content.
- **Logout**: Use the logout option to end your session securely.

## **License**

This project is licensed under the [MIT License](LICENSE).

## **Acknowledgments**

- **Flask Documentation**: [Flask Official Documentation](https://flask.palletsprojects.com/)
- **Miguel Grinberg's Blog**: For extensive Flask tutorials and guidance.
- **Community Contributors**: Thanks to everyone who has contributed to the Flask ecosystem.