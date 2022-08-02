
API URL Endpoints

| ENDPOINT | HTTP METHOD | CRUD METHOD | RESULT|
|----------|-------------|-------------|-------|
|qr_gen/:id |GET |READ | Fetch all user QR Codes from all categories|
|qr_gen/:id/category|GET|READ|Fetch all user QR Codes from a category|
|qr_gen/:id/category/:id|GET|READ|Fetch one user QR Code from a category|
|qr_gen/:id/category/create|POST|CREATE|Create a new QR code|
|qr_gen/:id/category/:id/delete|DELETE|DELETE|Delete one user QR Code from a category|
|qr_gen/:id/category/delete|DELETE|DELETE|Delete all user QR Code from a category|
|qr_gen/:id/delete|DELETE|DELETE|Delete all user QR Code|
|qr_gen/:id/category/update|PUT|UPDATE|Update one user QR Code from a category|
