:

---

# Web App Storefront

## Overview

The Web App Storefront is an e-commerce platform designed to provide a seamless shopping experience for users. It allows customers to browse, purchase products, manage their shopping carts, and track order history. Store owners can easily manage products and orders through a user-friendly interface.

## Goals

The primary goals of this web app are as follows:

1. **User Registration and Authentication:**

   - Allow users to create accounts with valid email addresses and secure passwords.
   - Implement user authentication and authorization to protect user data.

2. **Product Management:**

   - Enable store owners to add, edit, and delete product listings.
   - Organize products into categories for easy navigation.

3. **Product Display:**

   - Display products on the homepage in carousels based on various criteria (e.g., top sellers, random, by category).
   - Provide detailed product information and the ability to add products to the shopping cart.

4. **Shopping Cart:**

   - Allow users to add and remove items from their shopping carts.
   - Calculate and display the total price of items in the cart.
   - Provide a seamless shopping experience, including the ability to continue shopping or proceed to checkout.

5. **Payment Processing:**

   - Collect payment and shipping information securely.
   - Integrate a payment gateway (e.g., Stripe) for processing payments.
   - Generate order receipts for users.

6. **User Dashboard:**

   - Create a personalized dashboard for users to view order history, account settings, and potentially receive product recommendations.
   - Implement functionality for users to cancel or request refunds for orders.

7. **Navigation and User Interface:**
   - Design a user-friendly navigation bar with links to different parts of the app (e.g., homepage, user dashboard, cart).
   - Ensure a responsive and visually appealing user interface.

## Requirements

The following are the core requirements for the Web App Storefront:

- **Backend Technologies:**

  - Flask for building the server.
  - SQLAlchemy for database interactions.
  - Flask-Bcrypt for password hashing.
  - Flask-Migrate for database migrations.
  - JWT for user session management.

- **Frontend Technologies:**

  - React for building the user interface.
  - React Router for client-side routing.
  - CSS for styling the application.
  - Integration with external libraries or frameworks for UI components (e.g., Bootstrap, Material-UI).

- **Database:**

  - Use SQLite for development and consider using a production-ready database like PostgreSQL for deployment.

- **Deployment:**

  - Deploy the Flask backend to a hosting platform (e.g., Heroku, AWS, or DigitalOcean).
  - Deploy the React frontend to a static file hosting service (e.g., Netlify or Vercel).
  - Configure the frontend to make API requests to the deployed backend.
  - Optionally, set up a custom domain and SSL for secure communication.

- **Monitoring and Maintenance:**
  - Implement logging and monitoring to detect and address issues.
  - Regularly update dependencies and perform maintenance as required.

## Getting Started

To run the Web App Storefront locally, follow these steps:

1. Clone the repository to your local machine.
2. Set up a virtual environment and install the required Python packages.
3. Initialize the database and apply migrations.
4. Set environment variables for configuration (e.g., database URL, secret keys).
5. Install Node.js dependencies for the frontend.
6. Start both the Flask backend and React frontend.
7. Access the app in your web browser.

Detailed installation and usage instructions will be provided in the project's documentation.

## Contributors

- [Rae Stanton](https://github.com/rae-stanton)
- [Jason Connolly](https://github.com/jConn4177)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---
