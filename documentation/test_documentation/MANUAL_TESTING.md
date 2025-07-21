## ✅ Manual Testing

All core features of the SneakUp platform were manually tested on multiple devices and browsers to ensure usability, responsiveness, accessibility, and data integrity. The following outlines the manual testing process and outcomes:

### 📱 Responsive Layout
| Device | Action | Outcome |
|--------|--------|---------|
| Mobile | Navigated through header links and menus | All links functional; burger menu works as expected |
| Tablet | Browsed product grid | Products resized and aligned correctly |
| Desktop | Resized window and switched pages | Layout adapted properly at all breakpoints |

### 👟 Product Features
| Feature | Action | Result |
|--------|--------|--------|
| Product Listing | Visited product page with filters and pagination | Products display and update as expected |
| Product Detail | Clicked on product to view details | Details (price, size, description) loaded correctly |
| Add to Cart | Added item with size (or free size) | Item correctly added with feedback toast |
| Cart Management | Updated, removed items | All cart actions worked, totals updated live |

### 💳 Checkout Flow
| Step | Action | Outcome |
|------|--------|---------|
| Guest Checkout | Filled in form and completed payment | Order processed, redirected to success page |
| Logged-in Checkout | Used saved profile data | Form autofilled; user order stored in profile |
| Invalid Card | Entered test invalid details | Stripe blocked submission with error message |
| Order Confirmation | Checked email inbox | Confirmation email received with order summary |

### 🔒 Authentication & User Profile
| Action | Test | Result |
|--------|------|--------|
| Register | Created new account | Account created, redirected to profile |
| Login / Logout | Logged in/out repeatedly | Sessions maintained correctly |
| Reset Password | Used reset link from email | Password updated successfully |
| Profile Update | Changed name/address | Saved and reflected in checkout and dashboard |
| View Orders | Accessed past orders page | Previous orders listed with full detail view |

### 📄 Static / Informational Pages
| Page | Test | Result |
|------|------|--------|
| Returns & Privacy | Viewed and downloaded policies | Pages rendered; download buttons worked |
| About Page | Read history and sections (mission, best sellers, etc.) | Content structured and visible correctly |
| Contact Page | Submitted message via contact form | Success message shown; info not editable |
| FAQs | Read expandable questions | Layout rendered cleanly, mobile-friendly |

### ⚙️ Admin & Management
| Action | Test | Result |
|--------|------|--------|
| Add Product | Added via admin dashboard | Product appeared instantly on front store |
| Delete Product | Tried from product detail & list | Warning prompt shown; product removed |
| Edit Static Page | Modified About/Privacy from admin | Changes reflected dynamically on site |

---

### ✅ Summary
All manual testing passed with expected behavior across all critical flows. Bugs or inconsistencies (if any) were documented and resolved during development. Accessibility and responsiveness were prioritized on all pages.
