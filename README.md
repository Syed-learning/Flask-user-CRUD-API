# REST API - User Management (Flask)

##  Objective
Create a simple **REST API** that manages user data with CRUD (Create, Read, Update, Delete) operations.

---

##  Tools Used
- **Python** → Programming language  
- **Flask** → Web framework for building the API  
- **Postman** → Tool to test API endpoints  

---

##  Deliverables
- A Flask app (`app.py`) with endpoints:  
  - `POST /users` → Create a new user  
  - `GET /users` → Get all users  
  - `GET /users/<id>` → Get user by ID  
  - `PUT /users/<id>` → Update user details  
  - `DELETE /users/<id>` → Delete a user  
- User data stored in an **in-memory dictionary** (no database).  

---

##  Installation & Setup

1. Clone this project or create a new folder and add `app.py`.
2. Install Flask:
   ```bash
   pip install flask


##  Testing
This API was tested using **Postman**.  
You can import the provided Postman Collection (`User-crud-API.postman_collection.json`) to quickly test all endpoints.


###  Import into Postman
1. Open Postman  
2. Click **Import** → Upload `User-crud-API.postman_collection.json`  
3. Run the saved requests (POST, GET, PUT, DELETE) directly


