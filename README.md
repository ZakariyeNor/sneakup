# SneakUp 👟

## 📄 Project Description

**SneakUp** is a full-stack e-commerce web application for sneaker lovers. It allows users to browse, search, and purchase limited-edition footwear and apparel. It features a secure checkout process, dynamic product listings, account management, and admin product control. The project showcases strong UX planning across the Five Planes of UX and a mobile-first, responsive design.

---

![SneakUp Banner](documentation/mockups/desktop_mockups/desktop_home.png)

![badge](https://img.shields.io/badge/status-in%20development-blue)
![badge](https://img.shields.io/badge/django-4.2-green)
![badge](https://img.shields.io/badge/react-ready-yellow)
![badge](https://img.shields.io/badge/deployment-heroku-purple)
![badge](https://img.shields.io/badge/license-MIT-lightgrey)

---


## 🖼️ Site Mockups

### Desktop Views

- ![Home Page](documentation/mockups/desktop_mockups/desktop_home.png)
- ![About Page](documentation/mockups/desktop_mockups/desktop_about_page.png)
- ![Product Listing Page](documentation/mockups/desktop_mockups/desktop_product_listing.png)
- ![Product Detail Page](documentation/mockups/desktop_mockups/desktop_product_detail.png)
- ![Shopping Bag](documentation/mockups/desktop_mockups/desktop_shopping_bag.png)
- ![Checkout Page](documentation/mockups/desktop_mockups/desktop_checkout_page.png)
- ![Order Confirmation](documentation/mockups/desktop_mockups/desktop_order_confirmation.png)
- ![User Profile](documentation/mockups/desktop_mockups/desktop_profile_page.png)

### Mobile Views

- ![Home Page](documentation/mockups/mobile_mockups/mobile_home.png)
- ![About Page](documentation/mockups/mobile_mockups/mobile_about_page.png)
- ![Product Detail Page](documentation/mockups/mobile_mockups/mobile_product_detail.png)
- ![Shopping Bag](documentation/mockups/mobile_mockups/mobile_shopping_bag.png)
- ![Checkout Page](documentation/mockups/mobile_mockups/mobile_checkout_page.png)
- ![Order Confirmation](documentation/mockups/mobile_mockups/mobile_order_confirmation.png)
- ![Profile Page](documentation/mockups/mobile_mockups/mobile_profile_page.png)

---

## 🧠 UX Design – The Five Planes

### 1. Strategy Plane

- **Purpose**: Build a user-focused online shop for streetwear sneakers and apparel.
- **Business Goal**: Provide an intuitive, stylish shopping experience to drive conversions and build brand loyalty.

### 2. Scope Plane

- **User Features**:
  - Browse, filter, and search sneakers.
  - Add items to shopping bag.
  - Checkout securely with Stripe.
  - View order confirmation and history.

- **Admin Features**:
  - CRUD operations for products.
  - Access order and customer info.

### 3. Structure Plane

- **Navigation**:
  - Primary nav: Home, Shop, About, Bag, Profile.
  - Burger nav on mobile.

- **User Flow**:
  - Register → Browse → Add to Bag → Checkout → Confirmation

### 4. Skeleton Plane

- **Layout**:
  - Two-column layout for checkout.
  - Card-style product listings.

- **Interactions**:
  - Toasts for bag updates and errors.
  - Responsive mobile header with slide-in nav.

### 5. Surface Plane

- **Fonts**: Bebas Neue, Barlow, Open Sans.
- **Colors**:
  - Primary: #000000 (Black)
  - Secondary: #ffffff (White)
  - Accent: #ff0000 (Red)
- **Visual Identity**: Bold, urban, minimal.

---

## 👥 User Stories

| ID | Title             | As a...   | I want to...                | So that...                     |
|----|-------------------|-----------|-----------------------------|--------------------------------|
| 1  | Browse Products   | Shopper   | view a list of products     | I can find items I like        |
| 2  | Filter by Size    | Shopper   | filter shoes by size        | I only see what fits me        |
| 3  | Add to Bag        | Shopper   | add products to my bag      | I can purchase them later      |
| 4  | Edit Cart         | Shopper   | remove or change items      | I can manage my purchase       |
| 5  | Checkout          | Shopper   | securely pay for my order   | I can complete my transaction  |
| 6  | View Orders       | Shopper   | view my order history       | I can track past purchases     |
| 7  | Manage Products   | Admin     | add/edit/delete products    | I can manage the catalog       |
| 8  | Secure Access     | Admin     | access admin-only views     | my data is protected           |

---

## ✨ Features

### Core Features

- Account registration & login
- Responsive product listing
- Add to shopping bag
- Stripe payment integration
- Order history and confirmation
- Admin dashboard for product management

### Future Enhancements

- Wishlist/favorites system
- Reviews and ratings
- Inventory alerts
- Mobile app with React Native
- AI-based product recommendations

---

## 🛠️ Tools & Technologies

![Django](https://img.shields.io/badge/django-4.2-green)
![PostgreSQL](https://img.shields.io/badge/database-postgresql-blue)
![Stripe](https://img.shields.io/badge/payments-stripe-blueviolet)
![React Ready](https://img.shields.io/badge/frontend-react-ready-yellow)
![Heroku](https://img.shields.io/badge/deployment-heroku-purple)
![Bootstrap](https://img.shields.io/badge/css-bootstrap-7952b3)
![TailwindCSS](https://img.shields.io/badge/css-tailwind-06b6d4)
![GitHub Projects](https://img.shields.io/badge/workflow-github--projects-orange)
![Cloudinary](https://img.shields.io/badge/media-cloudinary-lightblue)
![Whitenoise](https://img.shields.io/badge/static--files-whitenoise-grey)

---

## 🧬 Database Design

![ERD Diagram](documentation/database/ERD.png)

---

## 🧑‍💻 Agile Development & Process

### MoSCoW Prioritization

- **Must**: Add to cart, checkout, register/login
- **Should**: Filter/search, responsive layout
- **Could**: Wishlists, user reviews
- **Won’t Yet**: Live chat, international shipping

### GitHub Project Board

Tasks are tracked using:
- Epics
- Issues
- Milestones
- Labels (e.g., `bug`, `enhancement`, `UI`)

---

## ✅ Testing

Please refer to the [TESTING.md](TESTING.md) file for:

- Manual testing (desktop & mobile)
- Automated test coverage
- Stripe integration test cases
- Form validation feedback
- Toast message display
- Accessibility testing

---

## 🚀 Deployment

### Live Site

[SneakUp on Heroku](https://your-sneakup-project.herokuapp.com)

### Key Steps:

- PostgreSQL setup via Heroku
- Cloudinary for media storage
- Static files served via WhiteNoise
- Environment variables managed with `.env`
- Production build using `collectstatic`

### Local Development

```bash
git clone https://github.com/your-username/sneakup.git
cd sneakup
pip install -r requirements.txt
python manage.py runserver
