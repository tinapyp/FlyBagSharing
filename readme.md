# FlyBagSharing

FlyBagSharing is a Flask-based web application for sharing flight baggage among users.

## Project Description

FlyBagSharing allows users to list their flight baggage details, including departure and arrival ports, flight date and time, phone number, and description. Other users can view these listings and contact the lister for sharing baggage.

## Project Structure
```
├── app/
│   ├── static/
│   │   └── css/
│   │   └── js/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
├── migrations/
├── tests/
├── .env
├── config.py
├── requirements.txt
├── main.py
└── README.md
```

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/FlyBagSharing.git
    ```

2. Navigate to the project directory:

    ```bash
    cd FlyBagSharing
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the project root directory and define the following variables:

    ```plaintext
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgresql://user:password@localhost:5432/flybagsharing
    ```

5. Run the application:

    ```bash
    flask run
    ```

## Contributing
This project is open to contributions from developers of all skill levels! Whether you're fixing a bug, implementing a new feature, or improving documentation, your efforts can help make FlyBagSharing even better. for details about contributing, follow the [contriburing](contributing.md) doc