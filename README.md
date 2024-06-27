# Parking System

This is a vehicle registration system project developed with Flask and SQLAlchemy. The system allows adding, viewing, updating, and deleting vehicle information, including license plate number, owner's name, and phone number.

## Features

- Register, edit, list, and remove cars and contact owner


## Project Structure

```bash
    soccer_manager/
    │
    ├── backend/
    │   ├── config.py
    │   ├── run.py
    │   ├── app/
    │   │   ├── models.py
    │   │   ├── routes.py
    │   └── requirements.txt
    │   └── Dockerfile
    │
    ├── frontend/
    │   ├── run.py
    │   ├── app/
    │   │   ├── __init__.py
    │   │   ├── routes.py
    │   │   ├── templates/
    │   │   │    ├── base.html
    │   │   │    ├── index.html
    │   │   │    ├── vehicle_form.html
    │   │   │    ├── vehicle_list.html
    │   └── requirements.txt
    │   └── Dockerfile
    │
    ├── docker-compose.yml
    └── README.md
```

## Technologies Used

- Python
- Flask
- Docker
- mySql

## Installation and Setup

To run the application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Pedro-Prado-Dev/Parking-System.git
   cd Parking-System
   ```
2. **Docker run:**
    ```bash
    docker-compose up --build
    ```


## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
