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

All pages passed through the Lighthouse test

- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/1.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/2.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/3.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/4.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/5.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/6.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/7.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/8.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/9.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/10.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/11.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/12.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/13.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/14.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/15.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/16.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/17.JPG)
- [Lighthouse test for all Apps in Mobile](read-me/testing-validators/lighthouse-mobile/18.JPG)

<hr>

- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/1.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/2.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/3.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/4.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/5.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/6.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/7.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/8.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/9.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/10.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/11.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/12.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/13.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/14.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/15.JPG)
- [Lighthouse test for all Apps in Desktop](read-me/testing-validators/lighthouse-desktop/16.JPG)

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
| Home         	| N/A                                                         	| N/A                                                         	| N/A                                                         	| N/A                                                      	| ![Home](read-me/testing-validators/ci-linter/1.jpg)         	| ![Home](read-me/testing-validators/ci-linter/2.jpg)         	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Blog         	| ![Blog](read-me/testing-validators/ci-linter/3.jpg)         	| ![Blog](read-me/testing-validators/ci-linter/4.jpg)         	| ![Blog](read-me/testing-validators/ci-linter/5.jpg)         	| N/A                                                      	| ![Blog](read-me/testing-validators/ci-linter/6.jpg)         	| ![Blog](read-me/testing-validators/ci-linter/7.jpg)         	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Shop         	| ![Shop](read-me/testing-validators/ci-linter/8.jpg)         	| ![Shop](read-me/testing-validators/ci-linter/9.jpg)         	| ![Shop](read-me/testing-validators/ci-linter/10.jpg)        	| N/A                                                      	| ![Shop](read-me/testing-validators/ci-linter/11.jpg)        	| ![Shop](read-me/testing-validators/ci-linter/12.jpg)        	| ![Shop](read-me/testing-validators/ci-linter/13.jpg) 	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Profiles     	| ![Profiles](read-me/testing-validators/ci-linter/14.jpg)    	| ![Profiles](read-me/testing-validators/ci-linter/15.jpg)    	| ![Profiles](read-me/testing-validators/ci-linter/16.jpg)    	| N/A                                                      	| ![Profiles](read-me/testing-validators/ci-linter/17.jpg)    	| ![Profiles](read-me/testing-validators/ci-linter/18.jpg)    	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Wishlist     	| ![Wishlist](read-me/testing-validators/ci-linter/19.jpg)    	| N/A                                                         	| ![Wishlist](read-me/testing-validators/ci-linter/20.jpg)    	| ![Wishlist](read-me/testing-validators/ci-linter/21.jpg) 	| ![Wishlist](read-me/testing-validators/ci-linter/22.jpg)    	| ![Wishlist](read-me/testing-validators/ci-linter/23.jpg)    	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Cart         	| N/A                                                         	| N/A                                                         	| N/A                                                         	| N/A                                                      	| ![Cart](read-me/testing-validators/ci-linter/24.jpg)        	| ![Cart](read-me/testing-validators/ci-linter/25.jpg)        	| N/A                                                  	| ![Cart](read-me/testing-validators/ci-linter/26.jpg) 	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Checkout     	| ![Checkout](read-me/testing-validators/ci-linter/27.jpg)    	| ![Checkout](read-me/testing-validators/ci-linter/28.jpg)    	| ![Checkout](read-me/testing-validators/ci-linter/29.jpg)    	| N/A                                                      	| ![Checkout](read-me/testing-validators/ci-linter/30.jpg)    	| ![Checkout](read-me/testing-validators/ci-linter/31.jpg)    	| N/A                                                  	| N/A                                                  	| ![Checkout](read-me/testing-validators/ci-linter/32.jpg) 	| ![Checkout](read-me/testing-validators/ci-linter/33.jpg) 	| ![Checkout](read-me/testing-validators/ci-linter/34.jpg) 	|
| Contact      	| ![Contact](read-me/testing-validators/ci-linter/35.jpg)     	| ![Contact](read-me/testing-validators/ci-linter/36.jpg)     	| ![Contact](read-me/testing-validators/ci-linter/37.jpg)     	| ![Contact](read-me/testing-validators/ci-linter/38.jpg)  	| ![Contact](read-me/testing-validators/ci-linter/39.jpg)     	| ![Contact](read-me/testing-validators/ci-linter/40.jpg)     	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
| Testimonials 	| ![Testimonial](read-me/testing-validators/ci-linter/41.jpg) 	| ![Testimonial](read-me/testing-validators/ci-linter/42.jpg) 	| ![Testimonial](read-me/testing-validators/ci-linter/43.jpg) 	| N/A                                                      	| ![Testimonial](read-me/testing-validators/ci-linter/44.jpg) 	| ![Testimonial](read-me/testing-validators/ci-linter/45.jpg) 	| N/A                                                  	| N/A                                                  	| N/A                                                      	| N/A                                                      	| N/A                                                      	|
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

There are no other known bugs to be fixed.

</details>