# Testing

This is the TESTING file for the [Mindspark](https://mind-spark-139c9f977593.herokuapp.com/) website.

Return back to the [README.md](README.md) file.


## Testing Contents  
  
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Validator Testing](#validator-testing)
    - [Lighthouse](#lighthouse)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Automated Testing](#automated-testing)
    - [Python](#python)
    - [Browser Compatibility](#browser-compatibility)
    - [Testing User Stories](#testing-user-stories)
  - [Bugs](#bugs)
    - [Unfixed Bugs](#unfixed-bugs)


### Manual Testing

<details>
<summary>Testing</summary>
<br>
 

| **Page Name**       | **Action**                                           | **Expected Behavior**                                               | **Pass/Fail** | **Tested** |
|---------------------|------------------------------------------------------|----------------------------------------------------------------------|--------------|------------|
| **Base**           | Click on the contact icon                            | Redirects to the contact page                                       | ✅ Pass      | Yes        |
| **Base**           | Use the search bar                                   | Allows users to search for content successfully                      | ✅ Pass      | Yes        |
| **Base**           | Click on navigation links                            | Navigates to the respective pages                                    | ✅ Pass      | Yes        |
| **Base**           | Click on the website logo                           | Redirects to the home page                                           | ✅ Pass      | Yes        |
| **Base**           | Open on smaller screens                              | Displays a responsive hamburger menu                                | ✅ Pass      | Yes        |
| **Base**           | Check for favicon                                    | Favicon is properly displayed                                       | ✅ Pass      | Yes        |
| **Home**           | View the homepage carousel                          | Three sliding images transition smoothly                            | ✅ Pass      | Yes        |
| **Home**           | View the About section                              | Displays images and a "Shop" button linking to the shop page        | ✅ Pass      | Yes        |
| **Home**           | View Latest Blogs section                           | Blog content is displayed with a "Read Blog" button                 | ✅ Pass      | Yes        |
| **Home**           | Click "Read Blog" button                            | Navigates to the respective blog page                               | ✅ Pass      | Yes        |
| **Home**           | Submit a testimonial                               | Redirects to login page if user is unauthenticated                  | ✅ Pass      | Yes        |
| **Home**           | Submit a testimonial (authenticated user)           | User can leave a review through a form                              | ✅ Pass      | Yes        |
| **Home**           | Edit or delete own testimonial                      | Users can modify or remove their own reviews                        | ✅ Pass      | Yes        |
| **Home**           | View testimonials                                   | All users (authenticated & unauthenticated) can see reviews         | ✅ Pass      | Yes        |
| **Footer (Base)**  | Click on social media links                         | Redirects to respective social media platforms                      | ✅ Pass      | Yes        |
| **Footer (Base)**  | Click on Privacy Policy link                        | Navigates to the Privacy Policy page                                | ✅ Pass      | Yes        |
| **Footer (Base)**  | Check for free delivery message                     | "Free Delivery on Orders Above €50" message is visible             | ✅ Pass      | Yes        |
| **Blog Page**      | Admin adds new blog post                            | UI allows adding a blog post with title, content, and image         | ✅ Pass      | Yes        |
| **Blog Page**      | Admin saves blog post as draft                      | Blog remains hidden from public view                                | ✅ Pass      | Yes        |
| **Blog Page**      | Admin publishes blog post                           | Blog becomes visible to all users                                   | ✅ Pass      | Yes        |
| **Blog Page**      | Admin edits a blog post                             | UI allows editing the title, content, and image                     | ✅ Pass      | Yes        |
| **Blog Page**      | Admin deletes a blog post                           | Blog is removed from the system                                    | ✅ Pass      | Yes        |
| **Blog Page**      | Click "Cancel" while editing                        | Redirects to blog list without saving changes                      | ✅ Pass      | Yes        |
| **Blog Page**      | View blog posts                                     | Only published blog posts are visible to all users                  | ✅ Pass      | Yes        |
| **Shop Page**      | View all products                                   | Displays all available products with images, name, and price       | ✅ Pass      | Yes        |
| **Shop Page**      | Click on a product                                 | Redirects to the product detail page                               | ✅ Pass      | Yes        |
| **Product Detail** | View product details                               | Displays product image, description, price, and "Add to Cart" button | ✅ Pass  | Yes        |
| **Product Detail** | Click "Add to Cart"                                | Product is added to the cart                                       | ✅ Pass      | Yes        |
| **Product Detail** | View related products                              | Displays other recommended products                                | ✅ Pass      | Yes        |
| **Login Page**     | Enter valid credentials and submit                 | User is logged in successfully                                    | ✅ Pass      | Yes        |
| **Login Page**     | Enter invalid credentials                          | Error message is displayed                                       | ✅ Pass      | Yes        |
| **Logout**        | Click logout button                                 | User is logged out and redirected to the home page               | ✅ Pass      | Yes        |
| **Signup Page**   | Enter valid details and submit                      | User is registered successfully and logged in                     | ✅ Pass      | Yes        |
| **Signup Page**   | Enter invalid/missing details                       | Error messages are displayed                                     | ✅ Pass      | Yes        |
| **FAQs Page**     | View FAQs section                                   | All questions and answers are displayed                          | ✅ Pass      | Yes        |
| **Profile Page**  | View profile details                               | Displays user details with an option to edit                     | ✅ Pass      | Yes        |
| **Profile Page**  | Update profile information                          | Changes are saved successfully                                   | ✅ Pass      | Yes        |
| **Update Password** | Change password successfully                     | User can log in with a new password                             | ✅ Pass      | Yes        |
| **Delete Account** | Click "Delete Account" and confirm                 | Account is permanently removed                                 | ✅ Pass      | Yes        |
| **Wishlist Page** | Click "Add to Wishlist" (Unauthenticated user)      | Redirects to login page                                        | ✅ Pass      | Yes        |
| **Wishlist Page** | Click "Add to Wishlist" (Authenticated user)        | Product is saved to the wishlist                               | ✅ Pass      | Yes        |
| **Wishlist Page** | View wishlist                                      | Displays saved products                                       | ✅ Pass      | Yes        |
| **Wishlist Page** | Remove product from wishlist                       | Product is removed successfully                               | ✅ Pass      | Yes        |
| **Cart Page**     | View cart                                          | Displays all added products with quantity and total price     | ✅ Pass      | Yes        |
| **Cart Page**     | Update product quantity                            | Price updates accordingly                                    | ✅ Pass      | Yes        |
| **Cart Page**     | Remove product from cart                           | Product is removed successfully                             | ✅ Pass      | Yes        |
| **Checkout Page** | Click "Proceed to Checkout"                       | Redirects to checkout page                                  | ✅ Pass      | Yes        |
| **Checkout Page** | Enter shipping details and complete order          | Order is placed successfully                                | ✅ Pass      | Yes        |
| **Checkout Page** | Enter incorrect details                            | Error messages are displayed                               | ✅ Pass      | Yes        |
| **Thank You Page** | View order confirmation message                   | Displays order details and "Continue Shopping" button      | ✅ Pass      | Yes        |

<hr>

- Mindspark website is tested and verified with no issues in different browsers:
  
  - [Google Chrome](https://www.google.com/intl/en_in/chrome/)
  - [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/)
  - [Microsoft Edge](https://www.microsoft.com/en-us/edge/welcome?form=MA13FJ)

- Mindspark webpage is tested and verified that my website is responsive in various screen devices by using Google chrome web developer tools
  
  - Laptop
  - Tablet
  - Large screen mobile
  - Desktop

<hr>

### Validator Testing

### Lighthouse

All pages passed through the Lighthouse test. The performance score is lower due to image aspect ratios, the absence of WebP images, and the use of Stripe and jQuery CDN. I will analyze these factors in future versions to identify improvements and enhance performance.

![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/1.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/2.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/3.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/4.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/5.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/6.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/7.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/8.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/9.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/10.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/11.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/12.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/13.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/14.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/15.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/16.JPG)
![Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/17.JPG)

<hr>

![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/1.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/2.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/3.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/4.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/5.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/6.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/7.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/8.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/9.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/10.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/11.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/12.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/13.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/14.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/15.JPG)
![Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/16.JPG)

<hr>

### HTML

All pages have passed through the [W3 Markup HTML Validator](https://validator.w3.org/). I navigated to each page of the deployed site and used the "View Page Source" option to access the HTML code, and validated it in the W3C Markup HTML Validator.

![All pages passed through the HTML validator](read-me/testing-validators/html-validator/1.JPG)

<hr>

### CSS

CSS stylesheet have passed through the [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)

![CSS stylesheet passed through the CSS validator](read-me/testing-validators/css-validator/1.JPG)

<hr>

### JS Hint

JSHint was used to look for errors in js files. No warnings found.

![JS code passed through the JS Hint](read-me/testing-validators/js-hint-validator/1.JPG)
  
<hr>

### Automated Testing

tests.py resulted no issues for my wishlist app and contact app.

![Automated Testing](read-me/testing-validators/automated-test.JPG)


### Python

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files. Couldn't able to adjust the long characters. I have included some screenshots with the results below.

| Features     	| Models.py                                                   	| Forms.py                                                    	| Admin.py                                                    	| Tests.py                                                 	| Views.py                                                    	| Urls.py                                                     	| Widgets.py                                           	| Contexts.py                                          	| Signals.py                                               	| webhook_handler.py                                       	| webhooks.py                                              	|
|--------------	|-------------------------------------------------------------	|-------------------------------------------------------------	|-------------------------------------------------------------	|----------------------------------------------------------	|-------------------------------------------------------------	|-------------------------------------------------------------	|------------------------------------------------------	|------------------------------------------------------	|----------------------------------------------------------	|----------------------------------------------------------	|----------------------------------------------------------	|
| Home         	| N/A                                                         	| N/A                                                         	| N/A                                                         	| N/A                                                      	| ![Home](read-me/testing-validators/ci-linter/1.JPG)         	| ![Home](read-me/testing-validators/ci-linter/2.JPG)         	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Blog         	| ![Blog](read-me/testing-validators/ci-linter/3.JPG)         	| ![Blog](read-me/testing-validators/ci-linter/4.JPG)         	| ![Blog](read-me/testing-validators/ci-linter/5.JPG)         	| N/A                                                      	| ![Blog](read-me/testing-validators/ci-linter/6.JPG)         	| ![Blog](read-me/testing-validators/ci-linter/7.JPG)         	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Shop         	| ![Shop](read-me/testing-validators/ci-linter/8.JPG)         	| ![Shop](read-me/testing-validators/ci-linter/9.JPG)         	| ![Shop](read-me/testing-validators/ci-linter/10.JPG)        	| N/A                                                      	| ![Shop](read-me/testing-validators/ci-linter/11.JPG)        	| ![Shop](read-me/testing-validators/ci-linter/12.JPG)        	| ![Shop](read-me/testing-validators/ci-linter/13.JPG) 	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Profiles     	| ![Profiles](read-me/testing-validators/ci-linter/14.JPG)    	| ![Profiles](read-me/testing-validators/ci-linter/15.JPG)    	| ![Profiles](read-me/testing-validators/ci-linter/16.JPG)    	| N/A                                                      	| ![Profiles](read-me/testing-validators/ci-linter/17.JPG)    	| ![Profiles](read-me/testing-validators/ci-linter/18.JPG)    	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Wishlist     	| ![Wishlist](read-me/testing-validators/ci-linter/19.JPG)    	| N/A                                                         	| ![Wishlist](read-me/testing-validators/ci-linter/20.JPG)    	| ![Wishlist](read-me/testing-validators/ci-linter/21.JPG) 	| ![Wishlist](read-me/testing-validators/ci-linter/22.JPG)    	| ![Wishlist](read-me/testing-validators/ci-linter/23.JPG)    	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Cart         	| N/A                                                         	| N/A                                                         	| N/A                                                         	| N/A                                                      	| ![Cart](read-me/testing-validators/ci-linter/24.JPG)        	| ![Cart](read-me/testing-validators/ci-linter/25.JPG)        	| N/A                                                  	| ![Cart](read-me/testing-validators/ci-linter/26.JPG) 	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Checkout     	| ![Checkout](read-me/testing-validators/ci-linter/27.JPG)    	| ![Checkout](read-me/testing-validators/ci-linter/28.JPG)    	| ![Checkout](read-me/testing-validators/ci-linter/29.JPG)    	| N/A                                                      	| ![Checkout](read-me/testing-validators/ci-linter/30.JPG)    	| ![Checkout](read-me/testing-validators/ci-linter/31.JPG)    	| N/A                                                  	| N/A                                                  	| ![Checkout](read-me/testing-validators/ci-linter/32.JPG) 	| ![Checkout](read-me/testing-validators/ci-linter/33.JPG) 	| ![Checkout](read-me/testing-validators/ci-linter/34.JPG) 	|
| Contact      	| ![Contact](read-me/testing-validators/ci-linter/35.JPG)     	| ![Contact](read-me/testing-validators/ci-linter/36.JPG)     	| ![Contact](read-me/testing-validators/ci-linter/37.JPG)     	| ![Contact](read-me/testing-validators/ci-linter/38.JPG)  	| ![Contact](read-me/testing-validators/ci-linter/39.JPG)     	| ![Contact](read-me/testing-validators/ci-linter/40.JPG)     	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Testimonials 	| ![Testimonial](read-me/testing-validators/ci-linter/41.JPG) 	| ![Testimonial](read-me/testing-validators/ci-linter/42.JPG) 	| ![Testimonial](read-me/testing-validators/ci-linter/43.JPG) 	| N/A                                                      	| ![Testimonial](read-me/testing-validators/ci-linter/44.JPG) 	| ![Testimonial](read-me/testing-validators/ci-linter/45.JPG) 	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
<hr>

### Testing User Stories

User Stories are documented in the Mindspark [GitHub Projects Board](https://github.com/users/klsoundarya/projects/5). User Stories are numbered, with Acceptance Criteria and Tasks detailed within. All features were tested to ensure that they provided the user with the expected output and action.


| User Story                    	| Acceptance Criteria Met? 	| Pass/Fail 	|
|-------------------------------	|--------------------------	|-----------	|
| Home                          	| Yes                      	| Pass      	|
| Navigation                    	| Yes                      	| Pass      	|
| Footer                        	| yes                      	| Pass      	|
| Register Page                 	| Yes                      	| Pass      	|
| Login Page                    	| Yes                      	| Pass      	|
| Logout Page                   	| Yes                      	| Pass      	|
|Shop Page               	| Yes                      	| Pass      	|
| Product-detail Posts               	| Yes                      	| Pass      	|
| Update Password               	| Yes                      	| Pass      	|
| Contact Page                  	| Yes                      	| Pass      	|
| Blog Page                    	| Yes                      	| Pass      	|
| Newsletter subscription                   	| Yes                      	| Pass      	|
| My profile              	| Yes                      	| Pass      	|
| Add a product          	| Yes                      	| Pass      	|
| Wishlist     	| Yes                      	| Pass      	|
| Cart   	| Yes                      	| Pass      	|
| Checkout          	| Yes                      	| Pass      	|
| Thank you checkout 	| Yes                      	| Pass      	|
| Delete Account                      	| Yes                      	| Pass      	|
| Add clear button            	| Yes                      	| Pass       	|
| Add edit/update button for blog           	| Yes                      	| Pass       	|
| Add edit/update button for product          	| Yes                      	| Pass       	|
| Add edit/delete button for testimonial review          	| Yes                      	| Pass       	|

<hr>

</details>

### Bugs

<details>
<summary>Bugs Fixed</summary>
<br>

- When a user submits a form on the contact details page, if they use the erase functionality (e.g., clearing or editing the form) and attempt to fill in the details and resubmit, a 403 Forbidden CSRF token error occurs. However, if the page is refreshed before submitting the form, the submission works as expected.

- Emails not sent for user signup, order checkout, or forgot password when using an incognito tab.

- If any issues occur during checkout, a 500 Internal Server Error is displayed.
![500 server error](read-me/bugs/500-internal-error.JPG) 

| No. 	| Bugs                                            	| Notes 	|
|-----	|-------------------------------------------------	|-------	|
| 1.  	| ![Bug 1](read-me/bugs/html-validator/1.JPG)     	| Fixed 	|
| 2.  	| ![Bug 2](read-me/bugs/html-validator/2.JPG)     	| Fixed 	|
| 3.  	| ![Bug 3](read-me/bugs/html-validator/3.JPG)     	| Fixed 	|
| 4.  	| ![Bug 4](read-me/bugs/html-validator/4.JPG)     	| Fixed 	|
| 5.  	| ![Bug 5](read-me/bugs/html-validator/5.JPG)     	| Fixed 	|
| 6.  	| ![Bug 6](read-me/bugs/html-validator/6.JPG)     	| Fixed 	|
| 7. 	  | ![Bug 7](read-me/bugs/js-hint-validator/1.JPG) 	  | Fixed 	|
| 8. 	  | ![Bug 8](read-me/bugs/ci-linter/1.JPG) 	          | Fixed 	|
| 9. 	  | ![Bug 9](read-me/bugs/ci-linter/2.JPG) 	          | Fixed 	|
| 10. 	  | ![Bug 10](read-me/bugs/ci-linter/3.JPG) 	          | Fixed 	|
| 11. 	  | ![Bug 11](read-me/bugs/ci-linter/4.JPG) 	          | Fixed 	|
| 12. 	  | ![Bug 12](read-me/bugs/ci-linter/5.JPG) 	          | Fixed 	|
| 13. 	  | ![Bug 13](read-me/bugs/ci-linter/6.JPG) 	          | Fixed 	|


### Unfixed Bugs

- On the checkout success page, the dropdowns for "Shop" and "Account" do not transition smoothly.

- When removing products from the wishlist, the alert message bar also displays the cart update notification. I'll address this issue later.

![wishlist bug](read-me/bugs/wishlist_remove.JPG) 

</details>