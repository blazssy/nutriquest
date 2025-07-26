

---

## 🥗 NutriQuest

**NutriQuest** is a full-stack nutrition tracking app that helps users log their daily food intake, monitor calories, and build healthier habits. Built with Django REST Framework and React, it offers a clean UI and robust backend for managing food items and nutrition logs.

---

## 🚀 Tech Stack

| Layer        | Technology               |
| ------------ | ------------------------ |
| Frontend     | React + Vite             |
| Backend      | Django + Django REST Framework |
| Database     | SQLite (dev) / PostgreSQL (prod) |
| Styling      | CSS / Tailwind / Chakra UI (optional) |
| API Testing  | Postman / curl           |
| Version Control | Git + GitHub          |

---

## 📦 Features

- ✅ Add, view, edit, and delete **Food Items**
- ✅ Log daily nutrition entries with calories and timestamps
- ✅ View total calorie intake per day
- ✅ RESTful API with full CRUD support
- ✅ Responsive React UI connected to backend
- 🔒 (Coming Soon) User authentication and personalized logs
- 📊 (Coming Soon) Dashboard with weekly summaries and trends

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/your-username/nutriquest.git
cd nutriquest
```

### 2. Backend Setup (Django)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Frontend Setup (React)
```bash
cd frontend/nutriquest-ui
npm install
npm run dev
```

---

## 🌐 API Endpoints

| Method | Endpoint                  | Description             |
| ------ | ------------------------- | ----------------------- |
| GET    | `/api/food-items/`        | List all food items     |
| POST   | `/api/food-items/`        | Add a new food item     |
| PUT    | `/api/food-items/{id}/`   | Update a food item      |
| DELETE | `/api/food-items/{id}/`   | Delete a food item      |
| GET    | `/api/nutrition-logs/`    | List all nutrition logs |
| POST   | `/api/nutrition-logs/`    | Add a new log entry     |

---

## 📸 Screenshots

*(Add screenshots of your UI here once ready)*

---

## 🧭 Roadmap

- [x] FoodItem CRUD (API + UI)
- [x] NutritionLog model and API
- [ ] NutritionLog UI integration
- [ ] Edit/Delete controls in React
- [ ] Form validation and error handling
- [ ] Authentication (JWT)
- [ ] Deployment to Heroku/Vercel

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is licensed under the MIT License.

