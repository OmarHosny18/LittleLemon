Little Lemon Restaurant API Endpoints

Homepage:
/

Menu API:
GET /api/menu/
POST /api/menu/
GET /api/menu/<id>/
PUT /api/menu/<id>/
PATCH /api/menu/<id>/
DELETE /api/menu/<id>/

Booking API (Requires Authentication):
GET /restaurant/booking/tables/
POST /restaurant/booking/tables/
GET /restaurant/booking/tables/<id>/
PUT /restaurant/booking/tables/<id>/
DELETE /restaurant/booking/tables/<id>/

Authentication (Djoser):
POST /auth/users/ (User Registration)
POST /auth/token/login/ (Login - Get Token)
POST /auth/token/logout/ (Logout)
POST /auth/users/reset_password/

Alternative Token Endpoint:
POST /api/api-token-auth/
