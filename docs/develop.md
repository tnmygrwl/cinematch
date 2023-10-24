# Development

This guide will help you set up and run the CineMatch project on your local machine.

## Getting Started

- Node.js and npm installed on your machine.
- Python 3.8 or higher installed on your machine (preferably Python 3.12).

## Project Structure

The project is divided into two main parts in a monorepo structure:

- `frontend`: This is where the Vue.js application resides.
- `backend`: This is where the FastAPI application resides.

## Frontend Setup

The frontend of the project is built using Vue.js 3. To set up and run the frontend, follow these steps:

1. Navigate to the frontend directory.

2. Install the project dependencies by running the following command:

```bash
npm install
```

3. To start the development server, run:

```bash
npm run serve
```

The Vue.js application will now be running on <http://localhost:8080>.

## Backend Setup

The backend of the project is built using FastAPI. To set up and run the backend, follow these steps:

1. Navigate to the backend directory.

2. It's recommended to create a virtual environment for the project. You can do this by running:

```bash
python3 -m venv env
```

3. Activate the virtual environment:

- On Windows, run: `env\Scripts\activate`
- On Unix or MacOS, run: `source env/bin/activate`

4. Install the project dependencies:
   
```bash
cd backend
pip install .
```

5. To start the development server, run:

```bash
uvicorn main:app --reload
```

The FastAPI application will now be running on <http://localhost:8000>.

## Running Tests

To run the tests for the backend, navigate to the backend directory and run:

```bash
pytest
```

Note: We're probably going to move to [`just`]("https://github.com/casey/just") for testing and installing dependencies.

## Contributing

When contributing to this project, please ensure that any frontend code is written using Vue.js 3 as per the project requirements. For the backend, we're using FastAPI, SQLAlchemy, and Pydantic. Please refer to the relevant code snippets for examples of how to structure your code.

If you have any questions or need further assistance, feel free to reach out. Happy coding!
