# SneakUp 👟

## [Sneak Up Sneakers](https://sneakup-904b7ffd186f.herokuapp.com/)

### Project Description

**SneakUp** is a full-stack e-commerce web application for sneaker lovers. It allows users to browse, search, and purchase limited-edition footwear and apparel. It features a secure checkout process, dynamic product listings, account management, and admin product control. The project showcases strong UX planning across the Five Planes of UX and a mobile-first, responsive design.

---

![SneakUp Banner](documentation/mockups/amiresponsive.png)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ZakariyeNor/sneakup)](https://www.github.com/ZakariyeNor/sneakup/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/ZakariyeNor/sneakup)](https://www.github.com/ZakariyeNor/sneakup/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/ZakariyeNor/sneakup)](https://www.github.com/ZakariyeNor/sneakup)
![badge](https://img.shields.io/badge/status-in%20development-blue)
![badge](https://img.shields.io/badge/django-4.2-green)
![badge](https://img.shields.io/badge/deployment-heroku-purple)

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


## 🛒 Shopping Bag Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Shopping Bag](documentation/mockups/desktop_mockups/desktop_shopping_bag.png) | ![Mobile Shopping Bag](documentation/mockups/mobile_mockups/mobile_shopping_bag.png) |

### 🔍 Purpose
The Shopping Bag Page allows users to review their selected products before checkout. Users can see product details, modify quantities and sizes, view delivery info, and proceed to payment.

### ✨ Features
- **List of Products** with images, name, selected size, and quantity.
- **Quantity Update Controls** with increment/decrement functionality.
- **Dynamic Messages** prompting users to sign up/login for free delivery.
- **Order Summary** showing subtotal, delivery cost, VAT, and total.
- **Checkout Button** directs users to the checkout page.
- **Empty Bag State** with a prompt to keep shopping.

### ⚙️ Backend Integration
- Bag data stored in session and updated via `add_to_bag` and `update_bag` views.
- Product quantities validated (1-10) before adding to bag.
- Handles products with and without size options, storing sizes as nested dict entries.
- Updates or removes items from the bag dynamically with user feedback via Django messages.
- Redirects users back to previous page after adding or updating items.
- Uses Django’s `get_object_or_404` for robust product retrieval.
- Includes partial templates for quantity update controls for reuse.

### ✅ Works As Expected
- Responsive design with Bootstrap, visually consistent on desktop and mobile.
- Clear user feedback on quantity changes and bag updates.
- Dynamic free delivery messaging based on current order total.
- Seamless integration between session storage and frontend display.
- Robust handling of edge cases like zero quantity or missing sizes.


## 🛒 Checkout Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Checkout](documentation/mockups/desktop_mockups/desktop_checkout_page.png) | ![Mobile Checkout](documentation/mockups/mobile_mockups/mobile_checkout_page.png) |

### 🔍 Purpose
The Checkout Page allows customers to securely provide their shipping and payment details to complete a purchase. It also displays a detailed order summary with itemized pricing, VAT, and delivery costs.

### ✨ Features
- **User Details & Shipping Form:** Collects first name, last name, email, phone number, and full address.
- **Save Info Option:** Lets authenticated users save shipping info to their profile.
- **Stripe Payment Fields:** Secure card input fields (card number, expiry, CVC) via Stripe Elements.
- **Order Summary:** Lists items with quantity, size, subtotal, VAT, delivery, and grand total.
- **Profile Mode:** Displays order details without payment fields when accessed from user profile.
- **Navigation Buttons:** Adjust bag, return to profile, or go back to shopping.

### ⚙️ Backend Integration
- Handled by the `checkout` view in Django.
- On **GET**:
  - Retrieves bag from session.
  - Creates Stripe PaymentIntent for order total.
  - Pre-fills form with user profile info if authenticated.
- On **POST**:
  - Validates submitted order form.
  - Saves Order and OrderLineItems for both free-size and sized products.
  - Associates Stripe payment ID (`stripe_pid`) with the order.
  - Redirects to the `checkout_success` page upon success.
- Uses `OrderForm` and crispy-forms for clean form rendering.

### 🛠️ Frontend Integration (JavaScript)
- Loads Stripe public key and client secret securely.
- Creates Stripe Elements for card number, expiry, and CVC with custom styling.
- Displays inline validation errors for each card input field.
- On form submission:
  - Disables inputs and submit button.
  - Sends AJAX POST to cache checkout data.
  - Calls `stripe.confirmCardPayment` to process payment.
  - Handles payment success by submitting the form.
  - Shows error messages and re-enables inputs on failure.

## 📦 Order Confirmation Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Order Confirmation](documentation/mockups/desktop_mockups/desktop_order_confirmation_page.png) | ![Mobile Order Confirmation](documentation/mockups/mobile_mockups/mobile_order_confirmation_page.png) |

### 🔍 Purpose
The Order Confirmation Page shows a detailed summary of a completed order. It confirms the purchase, displays order number, items purchased, shipping and billing information, and encourages customers to continue shopping.

### ✨ Features
- **Order Summary** with product images, names, subtitles, quantities, and sizes.
- **Shipping Details** including name, email, phone, full address, and optional fields.
- **Billing Information** showing order total, delivery cost, and grand total.
- **Responsive Layout** adapting details view for desktop and mobile.
- **Post-Purchase Marketing Section** with a thank you message and a call-to-action button to continue shopping.

### ⚙️ Backend Integration
- Order retrieved by `order_number` from URL.
- Links order to authenticated user’s profile and optionally saves shipping info.
- Clears shopping bag data from the session on success.
- Displays success message with order number and confirmation email.

## 👤 Profile Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Profile page desktop](documentation/mockups/desktop_mockups/desktop_profile_page.png) | ![Profile page](documentation/mockups/mobile_mockups/mobile_profile_page.png) |

### 🔍 Purpose
The Profile Page allows users who are logged in to manage their personal account details, delivery information, and view their order history all in one place. Users can update their delivery address, verify email settings, and access detailed order information.

### ✨ Features
- **Personal Info Tab:** Displays username and email with a welcome message.
- **Delivery Information Tab:** Editable delivery address form powered by a Django ModelForm with Crispy Forms.
- **Order History Tab:** Table listing past orders with order number, date, total, and link to detailed order view.
- **Tabbed Interface:** Bootstrap nav-tabs for smooth tab switching.
- **Email Verification Badge:** Shows email verification status with a quick link to email settings.
- **Buttons and Links:** Back to home and view order details.
- **Responsive Layout:** Uses Bootstrap grid and utility classes.
- **Custom CSS and JS:** Includes `profile.css` and `profile.js` for styling and interactivity.

### ⚙️ Backend Integration
- This page requires the user to be logged in.
- Fetches the logged-in user’s Profile model instance.
- Passes `profile_form` (a Django ModelForm for Profile) and `orders` queryset into the template context.
- Handles form submission via POST to update profile delivery information.
- Orders are linked through the `profile.orders.all()` reverse relation.
- Order detail links route to an order detail view for inspecting individual orders.


## 🔐 Login Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Login](documentation/mockups/desktop_mockups/desktop_login.png) | ![Mobile Login](documentation/mockups/mobile_mockups/mobile_login.png) |

### 🔍 Purpose
The Login Page allows existing users to authenticate and access their accounts securely.

### ✨ Features
- Customized Django authentication login template.
- Includes fields for username/email and password.
- "Remember Me" option to maintain login session.
- Links to password reset and sign up pages.
- Responsive design using Bootstrap for desktop and mobile.
- Custom CSS styling to match site branding.

### ⚙️ Backend Integration
- Uses Django’s built-in authentication backend.
- Form submission posts to the standard Django login view.
- Displays error messages for invalid login attempts.
- Redirects authenticated users to their profile or previous page.

---

## ✍️ Sign Up Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Sign Up](documentation/mockups/desktop_mockups/desktop_sign_up.png) | ![Mobile Sign Up](documentation/mockups/mobile_mockups/mobile_sign_up.png) |

### 🔍 Purpose
The Sign Up Page enables new users to create an account by providing required registration details.

### ✨ Features
- Customized Django user registration template.
- Includes fields for username, email, password, and password confirmation.
- Validates user inputs with clear error messages.
- Responsive layout styled with Bootstrap.
- Custom branding and styling consistent with the rest of the site.

### ⚙️ Backend Integration
- Connects to a Django registration view handling user creation.
- On successful registration, users may be redirected to login or automatically logged in.
- Uses Django forms for validation and user model creation.
- Includes CSRF protection and security best practices.


## 📝 About Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop about page](documentation/mockups/desktop_mockups/desktop_about_page.png) | ![Mobile about page](documentation/mockups/mobile_mockups/mobile_about_page.png)  |

### 🔍 Purpose
The About Page provides visitors with detailed information about DUAC’s brand story, mission, latest arrivals, best-selling products, materials used, and recent product launches. It is designed to build trust and engagement by showcasing the company’s values and product highlights.

### ✨ Features
- **Hero Section** with a large background image and overlay title.
- **Our Mission** section describing the brand’s vision and goals.
- **New Arrivals** grid showcasing the latest footwear products.
- **Our Materials** section explaining the sustainable or quality materials used.
- **Best Selling** highlight with text and image, including a shop button.
- **Launched Products** featuring products launched in the last 3 years.

### ⚙️ Backend Integration

- Data for each section is managed via Django models and can be updated through the Django Admin interface.
- The template uses conditional rendering: each section only appears if its corresponding model instance or queryset is available.
- Product images and details are fetched dynamically from related models.
- Example usage in the view:

## 📞 Contact Page

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop Contact page](documentation/mockups/desktop_mockups/contact_page.png) | ![Mobile Contact page](documentation/mockups/mobile_mockups/mobile_contact_us_page.png) |

### 🔍 Purpose
The Contact Page enables users to get in touch with DUAC by submitting inquiries via a contact form or by using the provided contact information. It facilitates customer support and communication.

### ✨ Features
- **Contact Form** where users can enter their name, email, subject, and message.
- **Form Validation** to ensure all required fields are filled and email format is correct.
- **Submission Feedback** with success or error messages after form submission.
- **Display of Contact Information** including phone number, email, and physical address for alternative contact methods.
- **Responsive Layout** optimized for desktop and mobile devices.


## 🧑‍💼 Product Management (Admin Only)

| Desktop Version | Mobile Version |
|-----------------|----------------|
| ![Desktop product management](documentation/mockups/desktop_mockups/desktop_product_management.png) | ![Mobile product management](documentation/mockups/mobile_mockups/mobile_product_management.png) |

---
### 🔍 Purpose (Add & Edit)
The Product Management system allows admins or authorized users to manage the product catalog for DUAC. It supports creating and editing products through a secure interface, keeping the product inventory up to date and accurate.

### ✨ Features  
- **Add Product** form with fields for name, description, category, price, image, and sizes.
- **Edit Product** view to update any product details.
- **Product Detail View** that shows individual product data for editing.
- **Form Validation** to ensure proper input (e.g., required fields, valid prices).
- **Admin-Only Access** to restrict product management to authenticated staff.
- **Responsive Design** compatible with desktop, tablet, and mobile admin interfaces.

### 🔍 Purpose (DELETE)

#### Delete Product
Admins or authorized users can delete products from both the product detail view and the main product list. A confirmation prompt provides a defensive warning to ensure the user truly intends to delete the item.
![Delete Product](documentation/mockups/desktop_mockups/deleting_warning.png) |
---

### 📄 Informational Pages: Returns, Privacy Policy, FAQs, Contact & About

These pages combine **static and dynamic functionality** to deliver important information and services to users. While their structure is similar for consistency, each page provides a unique value:

- **Returns & Privacy Policy**  
  Provide legal and customer service-related policies. They include downloadable versions for user convenience and transparency.
  ![Policies](documentation/mockups/pp_mock.png) |

- **FAQs**  
  Offers common questions and answers in a clear, searchable format to assist users quickly and reduce support queries.
  ![FAQs](documentation/mockups/faqs_mockup.png) |

-----
## 🧭 Header Navigation

The header navigation across DUAC uses the `base.html` template as its foundation. It dynamically adapts based on user authentication and device viewport, providing seamless navigation for both regular users and admin staff.

### Desktop – User Header  
- Displays the DUAC logo linked to the homepage.
- Main navigation includes links to Shop, About, Contact, and user profile dropdown.
- Shows shopping bag icon with dynamic cart total.
- User profile dropdown offers links to profile and logout for logged-in users; otherwise, links to login and signup.

![Desktop User Header](documentation/mockups/desktop_mockups/desktop_header_user.png)

### Desktop – Admin Header  
- Includes additional navigation links for admin features such as Product Management.
- Maintains user profile dropdown and shopping bag functionality.

![Desktop Admin Header](documentation/mockups/desktop_mockups/desktop_header_admin.png)

### Mobile – User Sidebar Nav  
- Sidebar navigation slides in on mobile devices for logged-in users.
- Contains main navigation links optimized for mobile screen.
- Provides quick access to profile and logout.

![Mobile User Sidebar Navigation](documentation/mockups/mobile_mockups/mobile_navigation_sidebar_user.png)

### Mobile – Admin Sidebar Nav  
- Sidebar navigation for admin users on mobile devices.
- Includes admin-specific links like Product Management along with regular navigation.

![Mobile Admin Sidebar Navigation](documentation/mockups/mobile_mockups/mobile_navigation_sidebar_admin.png)

---

## 🔻 Footer

The footer is consistent across pages and responsive, included in the `base.html` template:

- Contains site navigation links: About, Contact, Privacy Policy, Returns, and FAQs.
- Displays social media icons linking to official DUAC channels.
- Shows current year and company name copyright.

### Desktop View  
![Desktop Footer](documentation/mockups/desktop_mockups/desktop_footer.png)

### Mobile View  
![Mobile Footer](documentation/mockups/mobile_mockups/mobile_footer.png)

---

### Notes on `base.html` Integration

- The base template contains the HTML structure and loads CSS/JS libraries needed for responsive behavior.
- Navigation menus and footer are embedded within the base template using Django templating language.
- User-specific content such as profile links and admin features are conditionally rendered based on `user.is_authenticated` and `user.is_staff`.
- Mobile and desktop views adapt automatically via Bootstrap's responsive classes and custom JavaScript interactions included in the base template.

This ensures all header and footer components remain consistent and maintain functionality across all pages and device sizes.

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


### Surface Plane - Global Styles Overview

This section outlines the global variables, typography, layout, and UI elements that form the **surface plane** of the SneakUp web application, ensuring consistent visual design and user experience.

#### 🎨 Global Variables & Font Families
- Defined in CSS `:root` for colors and fonts:
  - Background: `#ffffff`
  - Text: `#000000`
  - Accent: `#ff4c60`
  - Auth Color: `#0070f3`
  - Fonts: `'Bebas Neue'` (headings), `'Barlow'` (UI), `'Open Sans'` (body)

#### 🏗️ Base Layout & Reset
- Universal margin, padding reset, and box-sizing set to `border-box`
- Body styled with flexible column layout for sticky footer
- Smooth font rendering enabled across browsers

#### ✍️ Typography
- Headings (`h1` to `h6`) use the heading font with responsive sizes via `clamp()`
- Paragraphs and lists styled with consistent spacing and font-family
- Links use primary color with smooth hover transitions to accent color

#### ⚙️ Forms & Inputs
- Inputs, textareas, selects have unified backgrounds, borders, and padding
- Placeholders styled with italic and subtle color for clarity

#### 🔘 Buttons
- Two button styles:
  - `.button-accent` using accent color
  - `.button-auth` using auth color (blue)
- Both have uppercase text, rounded corners, and pointer cursor

#### 🗺️ Layout Utilities
- `.container` class limits content width to 1200px, centers horizontally, and adds responsive padding

#### 🧭 Navigation & Header
- Header fixed width with box shadow and flex container for logo, nav links, and icons
- Navigation links styled with color transitions and active/focus states

#### 📱 Responsive Mobile Menu
- Slide-out mobile navigation panel with smooth transitions and visibility toggling

#### ⚓ Footer
- Footer with centered layout, social links, and interactive hover states on links
- Responsive gaps and padding adjusted via media queries

#### 🧩 Product Detail Styles
- Size selection boxes with hover and selected states for clear user feedback

#### 📐 Media Queries
- Responsive spacing and layout adjustments for footer and social links across viewport sizes


## User Stories

| Target | Expectation | Outcome |
|--------|-------------|---------|
| As a user | I would like the site to have a consistent header and footer | so that I can navigate easily and access key links on every page. |
| As a user | I would like the website to be responsive on all devices | so that I can shop and navigate comfortably from mobile or desktop. |
| As a user | I would like to view a landing page with trending shoes and banners | so that I can discover new and popular products. |
| As a user | I would like to browse all products with filters and categories | so that I can find the type of shoes I want efficiently. |
| As a user | I would like to view a product's detailed information and recommendations | so that I can make informed purchasing decisions. |
| As a user | I would like to register and log in securely | so that I can access my account and order history. |
| As a user | I would like to reset my password if I forget it | so that I can regain access to my account. |
| As a user | I would like to manage my personal profile information | so that I can update my shipping details and preferences. |
| As a user | I would like to view my previous orders and details | so that I can track purchases and reorder items. |
| As a user | I would like to add items to a shopping bag | so that I can purchase multiple products at once. |
| As a user | I would like to view and edit my shopping bag contents | so that I can adjust quantities or remove products before checkout. |
| As a user | I would like to securely checkout using Stripe | so that I can pay safely and complete my order. |
| As a user | I would like to receive a confirmation email after my payment | so that I have proof and details of my purchase. |
| As a user | I would like to learn about SneakUp's story and mission | so that I can connect with the brand values. |
| As a user | I would like to contact customer service using a contact form | so that I can get help or ask questions easily. |
| As a user | I would like to access legal policies and download them | so that I can understand the store’s privacy and return terms. |
| As an admin | I would like to securely log in to the admin dashboard | so that I can manage products and orders. |
| As an admin | I would like to add, edit, and delete products | so that I can keep the inventory up to date. |
| As a user | I would like to confirm before deleting a product | so that I don’t remove it by mistake. |


---

## Features Overview

Below is a breakdown of existing and planned features based on the [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method) prioritization from the user stories. Features have been grouped into **Implemented (MVP)** and **Future Enhancements**.

---

### Implemented Features (MVP)

> These features are completed, tested, and deployed as part of the MVP launch.

#### Consistent Layout  
- Global header and footer with navigation  
- Fully responsive and reused across all pages

#### Home (Landing Page)  
- Hero section, product previews, and brand messaging  
- Optimized layout for desktop and mobile  
- SEO and performance-focused

#### User Authentication & Security  
- Secure login/logout/register flows  
- Password encryption and CSRF protection  
- Integrated with Django AllAuth

#### Sign In / Sign Out / Reset Password  
- Password reset via email  
- Form validation and error feedback  
- Django AllAuth custom templates

#### Product Page  
- Filterable, paginated product list  
- Structured product cards with category filtering  
- Mobile and desktop layout

#### Product Detail Page  
- Full product details view  
- Add-to-cart with quantity and size selection  
- Related/up-selling product options

#### Shopping Bag  
- Add/update/remove products  
- Session-based cart persistence  
- Automatic price and total updates

#### Checkout + Stripe Payment  
- Stripe integration for secure payment  
- Shipping & billing form with autofill  
- Webhooks for post-payment order creation

#### Email Confirmation  
- Email sent after successful checkout  
- Contains receipt and order summary  
- HTML + fallback plain text support

#### User Profile  
- Edit user details  
- Manage shipping address  
- View past orders

#### Order History  
- Displays user's past purchases  
- Table with order numbers and timestamps

#### Contact Page  
- Submit form with validation  
- Displays static contact info (email, phone, address)  
- Connected to backend form handling

#### Responsive Design  
- Adaptive breakpoints for mobile and tablets  
- Hamburger navigation on small screens  
- Optimized images and layout testing

#### About Page  
- Story of SneakUp with sections: mission, history, new arrivals, launches, best sellers  
- Fully responsive and content-rich  
- Dynamic via admin

#### Static Page Management  
- Admin can CRUD: About, Privacy, Returns, etc.  
- Rich text rendering  
- Pages stored in models, editable via dashboard

---

### Future Enhancements (Post-MVP)

> These features were marked as **Won’t Have** for the MVP but are planned for future updates.

#### Product Reviews & Ratings  
- Allow users to rate and review products  
- Requires moderation and approval flow  
- Adds social proof and engagement

#### SMS Confirmation  
- Real-time order status via SMS  
- Would require third-party service like Twilio  
- Deferred due to complexity and cost

---

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) | Cloud-based IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/Figma-grey?logo=figma&logoColor=F24E1E)](https://www.figma.com) | Creating wireframes and edited stitch UI designs |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![Stitch](https://img.shields.io/badge/Stitch-blue?logo=google&logoColor=white)](https://stitch.withgoogle.com/) | Used to design UI for mobile and web. |

## Database Design

### Data Model

Auto-generating Entity Relationship Diagrams (ERD)

I have used Auto-generating Entity Relationship Diagrams (ERD) to document my database models, making it easier to visualize relationships between different models in my Django project. By utilizing the django-extensions and pygraphviz libraries, I was able to automatically generate an ERD representing the structure of my database. This approach streamlines the process of creating an up-to-date diagram, especially as the project evolves. Below are the steps I followed to generate the ERD, which can be included in your project’s documentation for better understanding and future reference.

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![E.R.D](documentation/%20advanced-erd.png)

## 🧑‍💻 Agile Development & Process

### GitHub Projects

[GitHub Projects](https://www.github.com/ZakariyeNor/sneakup/the_shoe) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![The shoe project](documentation/agile/gi_projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/ZakariyeNor/sneakup/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/ZakariyeNor/sneakup)](https://www.github.com/ZakariyeNor/sneakup/issues) | ![Issues](documentation/agile/gi_issues.png) |

- SMS confirmation and customer management features are currently in the backlog and were not delivered in this iteration. They are planned for future development.

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCow" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*~15% of stories*)
- **Won't Have**: not a priority for this iteration - future features (*the rest ~5% of stories*)

### GitHub Project Board

Tasks are tracked using:
- Epics
- Issues
- Milestones
- Labels (e.g., `must`, `should`, `won't`)

---

## ✅ Testing

 For all testing, you can find them [TESTING.md](documentation/test_documentation/) folder.

> Or for each 
 > [Manual Testing](documentation/test_documentation/MANUAL_TESTING.md),
 > [Front-end Tests](documentation/test_documentation/front_end_testing/FRONT_END_VALIDATION.md),
 > [Back-end Tests](documentation/test_documentation/back_end_testing/BACK_END_VALIDATION.md) and 
 > [PyTests](documentation/test_documentation/back_end_testing/PYTEST.md),

- | [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) |
- I used to output html templates, to validate in HTML validator without templatetags,
- I used to test, views, functions, models, urls, admin and forms to make the testing process faster.
- I used to document testing files to make the process of documenting faster
- I used to test the template logic and user accessibility.
- I used HTML validator for html testing, CSS validator for css testing and JSHINT for javascript testing.

---

## 🚀 Deployment

### Live Site

The live deployed application can be found deployed on [SneakUp on Heroku](https://sneakup-904b7ffd186f.herokuapp.com/)

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

| Key | Value |
| --- | --- |
| `CLOUDINARY_NAME` | https://cloudinary.com/ |
| `CLOUDINARY_API_KEY` | https://cloudinary.com/ |
| `CLOUDINARY_API_SECRET` | https://cloudinary.com/ |
| `DB_URL` | https://www.postgresql.org/ |
| `SECRET_KEY`          | Django secret key (keep this confidential)                                          |
| `EMAIL_HOST_PASSWORD` | Email service password (used for sending emails)                                    |
| `EMAIL_HOST_USER`     | Email address used to send transactional emails (e.g., `noreply@sneakup.com`)       |
| `DEFAULT_FROM_EMAIL`  | Default from-email address used in Django settings                                  |
| `STRIPE_PUBLIC_KEY`   | Public Stripe key for frontend use                                                  |
| `STRIPE_SECRET_KEY`   | Secret Stripe key for backend operations                                            |
| `STRIPE_WH_SECRET`    | Stripe webhook signing secret for validating Stripe events                          |


Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn sneakup.wsgi > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (*replace `app_name` with your app name*)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/ZakariyeNor/sneakup).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/ZakariyeNor/sneakup.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/ZakariyeNor/sneakup)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/ZakariyeNor/sneakup).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

Throughout the development of this project, I have used various resources, tools, and references that have helped shape and improve the application. This section acknowledges the individuals, tutorials, open-source libraries, and documentation that contributed to the project’s success.

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [Products of Boutiqua Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Checkout with stripe of Boutiqua Ado](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic, help to make faster the testing process and explanations |
| [FontAwesome](https://fontawesome.com) | Icon library for scalable vector icons |
| [jQuery](https://jquery.com) | JavaScript library for simplifying HTML DOM manipulation |
| [Bootstrap](https://getbootstrap.com) | Front-end framework for responsive web design |
| [Django Tutorial Playlist](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM) | Django tutorial series for beginners |
| [![Stitch](https://img.shields.io/badge/Stitch-blue?logo=google&logoColor=white)](https://stitch.withgoogle.com/) | Used to design UI for mobile and web. |

### Media

### Media Attribution

- **Logo**: The logo used in this project is a fontawesome icon.
- **Cover Image**: The cover image used in this project is from the official [Django Walkthrough](https://github.com/ZakariyeNor/django-semi).
- The scissors logo in the large screen size is [Font Awesome](https://fontawesome.com).
- **Email**: The email connected to the contact us form (sneakup.confirmation@gmail.com) is owned and managed by me.

### Images & Content Sources

- **Images**  
  - [Pexels](https://www.pexels.com) - Free stock images
  - [Unsplash](https://unsplash.com/s/photos/shoes) - Free stock images 
  - [Google images](https://www.google.com/) - Free stock images

  The images that are deployed and submitted as part of the live app are sourced from Pexels, Unsplash and googlge These images have been uploaded to Cloudinary for efficient media management and optimization, ensuring a seamless user experience.


- **Text & Content**  
  - Generated using ChatGPT
  - Generated UI using  and stitch
  - Design Ideation: The concept of balanced typography, fonts, colors, sizing, and spacing was developed with the help of ChatGPT ideation.

### Acknowledgements

I would like to acknowledge and thank those who have contributed to the success of this project. Their support, tools, and resources have been invaluable throughout my development process.

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank God, who gave me the ability to do all of these and remain consistent.
