# Django Project: Learning E-commerce Website

This Django project is a simple e-commerce website created for learning purposes. It includes features such as authentication, a home page displaying products, adding products to the cart, viewing a single product, and viewing the user's profile.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/learning-ecommerce.git
   ```

2. Navigate to the project directory:

   ```bash
   cd learning-ecommerce
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # for Mac/Linux
   env\Scripts\activate  # for Windows
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Load sample data (optional):

   ```bash
   python manage.py loaddata sample_data.json
   ```

## Usage

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Open your browser and visit `http://localhost:8000` to access the home page.

3. Register a new user account or use the provided sample user credentials:

   - Username: `user`
   - Password: `password`

4. Explore the different sections of the website:

   - **Home**: Displays a list of available products.
   - **Product Detail**: Click on a product to view its details.
   - **Cart**: Add products to the cart and proceed to checkout.
   - **Profile**: View and update user profile information.

## Technologies Used

- Django: Python web framework for building the application.
- HTML/CSS: Frontend markup and styling.

## Project Structure

The project's structure follows Django's recommended layout:

- `user/`: Main Django project directory.
- `products/`: Django app containing product-related functionality.
- `cart/`: Django app for handling the shopping cart functionality.
- `templates/`: HTML templates for rendering the website pages.
- `static/`: Static files such as CSS and JavaScript.
- `media/`: Directory to store uploaded user files.


Please note that the UI design of this project is minimal and not focused on aesthetics, as it was developed for learning purposes.

If you have any questions or need further assistance, feel free to reach out. Happy learning!
