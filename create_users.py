# create_users.py
from app import app, db, bcrypt
from app import User

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error creating tables: {e}")

    # Add Admin user

    try:
        hashed_password_admin = bcrypt.generate_password_hash('admin_password').decode('utf-8')
    except ValueError as e:
        print(f"Error generating hash for admin password: {e}")
    
    
    admin_user = User(email='arunp77@gmail.com', password=hashed_password_admin, is_admin=True)
    db.session.add(admin_user)

    # Add Regular user
    hashed_password_user = bcrypt.generate_password_hash('user_password').decode('utf-8')
    
    regular_user = User(email='nidhi4358@gmail.com', password=hashed_password_user, is_admin=False)
    db.session.add(regular_user)

    # Commit the changes
    db.session.commit()
