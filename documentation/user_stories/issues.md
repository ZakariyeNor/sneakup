# Shoe Store User Stories - MoSCoW Prioritized Issues

---

## Must Have (60%)

### 1. Consistent Layout  
<!-- Labels: Must Have, Milestone 1: Project Setup & Basic Layout -->
**As a** visitor  
**I want** to see a consistent header and footer  
**So that** I can easily navigate the site.

#### Acceptance Criteria:
- Header and footer appear on all pages.  
- Navigation links work correctly.  
- Layout is consistent across devices.  
- Tests cover header/footer presence and navigation.  
- Documentation describes header/footer components and navigation usage.

---

### 2. Home (Landing Page)  
<!-- Labels: Must Have, Milestone 1: Project Setup & Basic Layout -->
**As a** visitor  
**I want** to view a clean and attractive homepage  
**So that** I get a good first impression of the brand.

#### Acceptance Criteria:
- All homepage sections render correctly.  
- Responsive on desktop and mobile.  
- Loading performance and images validated.  
- Tests verify homepage rendering and responsiveness.  
- Documentation includes homepage layout and content guidelines.

---

### 3. Product Page  
<!-- Labels: Must Have, Milestone 2: Product Listing & Detail -->
**As a** user  
**I want** to browse a list of available shoes  
**So that** I can choose what I like.

#### Acceptance Criteria:
- Products load and display correctly.  
- Filters and pagination behave properly.  
- Responsive and accessible design.  
- Tests verify product loading, filtering, and pagination.  
- Documentation explains product listing API and logic.

---

### 4. Product Detail Page  
<!-- Labels: Must Have, Milestone 2: Product Listing & Detail -->
**As a** user  
**I want** to view detailed information about a shoe  
**So that** I can understand what I’m buying.

#### Acceptance Criteria:
- All product details show correctly.  
- Up-selling and cross-selling sections appear.  
- Add-to-cart functionality works.  
- Tests cover product details, up-selling, cross-selling, and add-to-cart.  
- Documentation covers product detail structure and related products logic.

---

### 5. User Authentication & Security  
<!-- Labels: Must Have, Milestone 1: Project Setup & Basic Layout -->
**As a** user  
**I want** to register and log in securely  
**So that** my account and data are protected.

#### Acceptance Criteria:
- Registration and login workflows function.  
- Password encryption and secure session management.  
- Tests verify authentication flows and security.  
- Documentation explains authentication flow and security best practices.

---

### 6. User Sign In / Sign Out / Reset Password  
<!-- Labels: Must Have, Milestone 1: Project Setup & Basic Layout -->
**As a** user  
**I want** to sign in, sign out, and reset my password  
**So that** I can access my account safely and recover access if needed.

#### Acceptance Criteria:
- Sign in and sign out flows work.  
- Password reset email sent and reset process works.  
- Validation and error handling implemented.  
- Tests cover sign-in/out and password reset workflows.  
- Documentation describes endpoints and reset mechanism.

---

### 7. Profile Page  
<!-- Labels: Must Have, Milestone 4: Profile Page & Confirmations -->
**As a** user  
**I want** to view and edit my profile details  
**So that** my information stays current.

#### Acceptance Criteria:
- Profile data loads and saves correctly.  
- Input validation and error messages present.  
- Updates persist.  
- Tests verify profile CRUD operations and validation.  
- Documentation includes profile management UI and API details.

---

### 8. Shopping Bag  
<!-- Labels: Must Have, Milestone 3: Shopping Bag & Checkout -->
**As a** user  
**I want** to add shoes to my shopping bag  
**So that** I can buy them later.

#### Acceptance Criteria:
- Add/remove items functionality works.  
- Quantity updates and price calculations correct.  
- Persistence across sessions verified.  
- Tests cover shopping bag operations and persistence.  
- Documentation explains shopping bag logic and integration.

---

### 9. Checkout Page with Stripe Payment  
<!-- Labels: Must Have, Milestone 3: Shopping Bag & Checkout -->
**As a** user  
**I want** to enter or confirm my shipping and billing info  
**So that** I can place an order using Stripe payment.

#### Acceptance Criteria:
- Checkout form validations work.  
- Stripe payment succeeds and fails gracefully.  
- Orders created after payment.  
- Tests simulate payments and form validation.  
- Documentation includes checkout workflow and Stripe integration.

---

## Should Have (20%)

### 10. Order History  
<!-- Labels: Should Have, Milestone 4: Profile Page & Confirmations -->
**As a** user  
**I want** to see a list of my past orders  
**So that** I can track or reorder them.

#### Acceptance Criteria:
- Order history loads correctly.  
- Details and reorder functionality available.  
- Pagination works if needed.  
- Tests verify order history and reorder process.  
- Documentation explains order history API and UI.

---

### 11. Email Confirmation After Payment  
<!-- Labels: Should Have, Milestone 4: Profile Page & Confirmations -->
**As an** owner  
**I want** users to receive email confirmation after payment  
**So that** they have proof of purchase and order details.

#### Acceptance Criteria:
- Confirmation emails sent on successful payments.  
- Email content formatted correctly.  
- Errors in email delivery handled.  
- Tests verify email sending and content.  
- Documentation includes email templates and sending process.

---

### 12. Contact Page  
<!-- Labels: Should Have, Milestone 4: Profile Page & Confirmations -->
**As a** user  
**I want** to fill in a contact form  
**So that** I can ask questions or give feedback.

#### Acceptance Criteria:
- Form validation and submission work.  
- Messages received on backend or via email.  
- Confirmation message shown after submission.  
- Tests cover form validation and message handling.  
- Documentation explains form fields and backend process.

---

## Could Have (15%)

### 13. About Page  
<!-- Labels: Could Have, Milestone 5: Final Testing & Documentation -->
**As a** visitor  
**I want** to learn about the brand’s story and values  
**So that** I can trust the products.

#### Acceptance Criteria:
- Page content and images display correctly.  
- Responsive design and navigation.  
- Tests verify content rendering and responsiveness.  
- Documentation includes content guidelines and structure.

---

### 14. Responsive Design & Mobile Layout  
<!-- Labels: Could Have, Milestone 5: Final Testing & Documentation -->
**As a** user  
**I want** the website to adapt well on my mobile device  
**So that** I can browse and shop easily from any screen size.

#### Acceptance Criteria:
- Layout adapts correctly on various screen sizes.  
- Navigation and buttons work on touch devices.  
- Performance is acceptable on mobile networks.  
- Tests include multi-device layout and usability checks.  
- Documentation details responsive breakpoints and UX considerations.

---

## Won't Have (5%) — New Feature

### 15. Product Reviews & Ratings  
<!-- Labels: Won't Have, Milestone 5: Final Testing & Documentation -->
**As a** user  
**I want** to read and leave reviews for products  
**So that** I can make better purchase decisions.

#### Acceptance Criteria:  
- Users can submit star ratings and text reviews.  
- Reviews display on product detail pages.  
- Admin can moderate or remove inappropriate reviews.  
- Tests cover review submission, display, and moderation.  
- Documentation describes review implementation and moderation guidelines.

---
