# EcoContractor Backend

This is the backend for the EcoContractor project, built using FastAPI. Built to support enterprises who want to generate lots of smart contracts on the carbon credit blockchain. Created in submission for Fintech Summit 2025

## Setup Process

Follow these steps to set up the project:

1. **Clone the repository:**

   ```bash
   git clone git@github.com:HackJanitors/ecocontractor-backend.git
   cd ecocontractor-backend
   ```

2. **Create and activate a Python virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

## Project Structure

- `main.py`: The entry point of the application.
- `app/`: Contains the main application code.
- `requirements.txt`: List of dependencies.

## Contributing

Feel free to open issues or submit pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.
