# Vendor Shop Management

This is a Django-based project for managing vendors and shops. It includes features like user authentication, shop management, and a public API for searching nearby shops.

---

## **Table of Contents**
1. [Features](#features)
2. [Installation](#installation)
3. [Running the Project](#running-the-project)
4. [Accessing the Application](#accessing-the-application)
5. [API Endpoints](#api-endpoints)
6. [Contributing](#contributing)
7. [License](#license)

---

## **Features**
- **User Authentication:** Register, login, and manage users (vendors).
- **Shop Management:** Create, read, update, and delete shops.
- **Public API:** Search for nearby shops using latitude, longitude, and radius.
- **Admin Portal:** Manage users, groups, and shops via the Django admin interface.

---

## **Installation**

### **Prerequisites**
- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL/MySQL/SQLite (depending on your database choice)

### **Steps**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/vendor-shop-management.git
   cd vendor-shop-management
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   Update the `DATABASES` setting in `settings.py` with your database credentials.

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **Running the Project**
   - **Start the Development Server:**
     ```bash
     python manage.py runserver
     ```
   - **Access the Application:**
     Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### **Accessing the Application**

#### **User Portal**
- **Login URL:** [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)
- **Shop List:** [http://127.0.0.1:8000/shops/](http://127.0.0.1:8000/shops/)
- **Create Shop:** [http://127.0.0.1:8000/shops/create/](http://127.0.0.1:8000/shops/create/)
- **Edit Shop:** `http://127.0.0.1:8000/shops/edit/<shop_id>/`
- **Delete Shop:** `http://127.0.0.1:8000/shops/delete/<shop_id>/`

#### **Admin Portal**
- **Admin Login URL:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Manage Users:** [http://127.0.0.1:8000/admin/auth/user/](http://127.0.0.1:8000/admin/auth/user/)
- **Manage Groups:** [http://127.0.0.1:8000/admin/auth/group/](http://127.0.0.1:8000/admin/auth/group/)
- **Manage Shops:** [http://127.0.0.1:8000/admin/shops/shop/](http://127.0.0.1:8000/admin/shops/shop/)

### **Public API**
- **Nearby Shops:** `http://127.0.0.1:8000/api/nearby/?lat=<latitude>&lon=<longitude>&radius=<radius>`
- **Example:** [http://127.0.0.1:8000/api/nearby/?lat=12.34&lon=56.78&radius=10](http://127.0.0.1:8000/api/nearby/?lat=12.34&lon=56.78&radius=10)

### **API Endpoints**

#### **Shop API**
- **List Shops:** `GET /api/shops/`
- **Create Shop:** `POST /api/shops/`
- **Retrieve Shop:** `GET /api/shops/<id>/`
- **Update Shop:** `PUT /api/shops/<id>/`
- **Delete Shop:** `DELETE /api/shops/<id>/`

#### **Nearby Shops API**
- **Search Nearby Shops:** `GET /api/nearby/?lat=<latitude>&lon=<longitude>&radius=<radius>`

### **Contributing**
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

### **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

### **Contact**
For any questions or feedback, please contact:

- **Abhishek kushwaha**
- **Email:** agi.abhishekk@gmail.com

