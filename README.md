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


# SneakUp Mockup Documentation

This documentation shows each page’s **desktop** and **mobile** designs for the SneakUp e-commerce platform.

---

## 🏠 Home Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Home Page](documentation/mockups/desktop_mockups/desktop_home.png) | ![Mobile Home Page](documentation/mockups/mobile_mockups/mobile_home.png) |

### 🔍 Purpose
The Home Page introduces the user to the DUAC brand and showcases featured shoe categories like **Running**, **Casual**, **Formal**, and **Sports**. It includes promotional banners and a newsletter subscription section to drive engagement.

### ✨ Features
- **Hero Banner** with call-to-action button.
- **Featured Categories** section with clickable images.
- **Seasonal Promotion Banner** (e.g. Summer Sale).
- **Newsletter Subscription Form**.
- **Free Delivery Promo Box**.

### ⚙️ Backend Integration
- Loads product category images dynamically from media.
- Displays a dynamic welcome message based on category availability.
- Stores and validates newsletter email submissions using the `NewsletterSubscriber` model.

### ✅ Works As Expected
- Fully responsive and styled using Bootstrap.
- Desktop and mobile versions display properly.
- Email subscription uses Django validation and gives real-time user feedback.


## 🛍️ Product Listing Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Product Listing](documentation/mockups/desktop_mockups/desktop_product_listing.png) | ![Mobile Product Listing](documentation/mockups/mobile_mockups/mobile_product_listing.png) |

### 🔍 Purpose
The Product Listing Page displays all available shoes in the SneakUp store. It allows users to browse by category, filter and sort products, and preview key details before visiting the product detail page.

### ✨ Features
- **Marketing Banner** at the top with promotional text and background.
- **Category Filter Sidebar** for browsing by shoe type (e.g., Casual, Running).
- **Sorting Options** (e.g., Price Low to High, Rating).
- **Product Cards** with:
  - Image
  - Name and Price
  - Star Ratings
- **Admin Controls** (Edit/Delete) visible only to staff users.
- **Scroll to Top Button** for quick navigation.

### ⚙️ Backend Integration
- Product and category data fetched from Django models using:
  ```python
  products = Product.objects.all()
  categories = Category.objects.all()
  ```
- Filtering, sorting, and query parameters handled in the `all_products_view`.
- Star ratings rendered using custom template logic or static icons.
- Dynamic images via Cloudinary or uploaded media.
- Admin-only buttons shown conditionally with:
  ```django
  {% if request.user.is_staff %}
    <!-- Edit/Delete Buttons -->
  {% endif %}
  ```

### ✅ Works As Expected
- Fully responsive with Bootstrap layout.
- Sidebar hides on mobile; sorting appears above products.
- All links and filters work correctly.
- Admin tools are restricted and tested.



## 📦 Product Detail Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Product Detail](documentation/mockups/desktop_mockups/desktop_product_detail.png) | ![Mobile Product Detail](documentation/mockups/mobile_mockups/mobileproduct_detail.png) |

### 🔍 Purpose
The Product Detail Page provides comprehensive information about a specific shoe product. It allows customers to view product images, detailed descriptions, ratings, and select sizes and quantities before adding items to their shopping bag.

### ✨ Features
- **Breadcrumb Navigation** for easy backtracking.
- **Product Information** including name, subtitle, price, description, and category links.
- **Product Image** with fallback to default if no image exists.
- **Star Ratings** displayed visually with icons.
- **Size Selection** with free-size or selectable sizes.
- **Quantity Selector** with increment/decrement buttons.
- **Add to Bag Form** with hidden fields to handle size, quantity, and redirect.
- **Admin Controls** for editing or deleting the product (visible to staff only).
- **Shipping Info Cards** detailing fast delivery, free returns, and resell options.
- **Keep Shopping Button** for easy navigation back to product listings.

### ⚙️ Backend Integration
- Product data fetched by `product_detail` view via product ID.
- Size options dynamically rendered based on product attributes.
- Admin controls shown conditionally using:
  ```django
  {% if request.user.is_staff %}
    <!-- Edit/Delete Buttons -->
  {% endif %}


## 🧺 Shopping Bag Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_shopping_bag.png)  
![](documentation/mockups/desktop_mockups/desktop_shopping_bag.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_shopping_bag.png)  
![](documentation/mockups/mobile_mockups/mobile_shopping_bag.png)

---

## 💳 Checkout Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_checkout_page.png)  
![](documentation/mockups/desktop_mockups/desktop_checkout_page.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_checkout_page.png)  
![](documentation/mockups/mobile_mockups/mobile_checkout_page.png)

---

## ✅ Order Confirmation Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_order_confirmation_page.png)  
![](documentation/mockups/desktop_mockups/desktop_order_confirmation_page.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_order_confirmation_page.png)  
![](documentation/mockups/mobile_mockups/mobile_order_confirmation_page.png)

---

## 👤 Profile Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_profile_page.png)  
![](documentation/mockups/desktop_mockups/desktop_profile_page.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_profile_page.png)  
![](documentation/mockups/mobile_mockups/mobile_profile_page.png)

---

## 🔐 Login Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_login.png)  
![](documentation/mockups/desktop_mockups/desktop_login.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_login.png)  
![](documentation/mockups/mobile_mockups/mobile_login.png)

---

## ✍️ Sign Up Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_sign_up.png)  
![](documentation/mockups/desktop_mockups/desktop_sign_up.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_sign_up.png)  
![](documentation/mockups/mobile_mockups/mobile_sign_up.png)

---

## ℹ️ About Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_about_page.png)  
![](documentation/mockups/desktop_mockups/desktop_about_page.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_about_page.png)  
![](documentation/mockups/mobile_mockups/mobile_about_page.png)

---

## 📞 Contact Page

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_contact_page.png)  
![](documentation/mockups/desktop_mockups/desktop_contact_page.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_contact_us_page.png)  
![](documentation/mockups/mobile_mockups/mobile_contact_us_page.png)

---

## 🧑‍💼 Product Management (Admin Only)

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_product_management.png)  
![](documentation/mockups/desktop_mockups/desktop_product_management.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_product_management.png)  
![](documentation/mockups/mobile_mockups/mobile_product_management.png)

---

## 🧭 Header Navigation

**Desktop – User Header**  
[](documentation/mockups/desktop_mockups/desktop_header_user.png)  
![](documentation/mockups/desktop_mockups/desktop_header_user.png)

**Desktop – Admin Header**  
[](documentation/mockups/desktop_mockups/desktop_header_admin.png)  
![](documentation/mockups/desktop_mockups/desktop_header_admin.png)

**Mobile – Top Navigation**  
[](documentation/mockups/mobile_mockups/mobile_top_nav.png)  
![](documentation/mockups/mobile_mockups/mobile_top_nav.png)

**Mobile – User Sidebar Nav**  
[](documentation/mockups/mobile_mockups/mobile_navigation_sidebar_user.png)  
![](documentation/mockups/mobile_mockups/mobile_navigation_sidebar_user.png)

**Mobile – Admin Sidebar Nav**  
[](documentation/mockups/mobile_mockups/mobile_navigation_sidebar_admin.png)  
![](documentation/mockups/mobile_mockups/mobile_navigation_sidebar_admin.png)

---

## 🔻 Footer

**Desktop View**  
[](documentation/mockups/desktop_mockups/desktop_footer.png)  
![](documentation/mockups/desktop_mockups/desktop_footer.png)

**Mobile View**  
[](documentation/mockups/mobile_mockups/mobile_footer.png)  
![](documentation/mockups/mobile_mockups/mobile_footer.png)

---

## 📱 Mobile Only – Bottom Navigation

**Mobile Bottom Nav**  
[](documentation/mockups/mobile_mockups/mobile_bottom_nav.png)  
![](documentation/mockups/mobile_mockups/mobile_bottom_nav.png)


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
