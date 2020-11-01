# The British Wine Cellar
This is website for an online wine retailer called The British Wine Cellar. The British Wine Cellar 
focus on supporting small and medium sized vineyards and wineries promoting local produce and celebrating 
the little know high quality wines that can be found across Great Britain.

This current iteration of the website sets out the foundation for a wider project that will introdcue more
products and celebrate more vineyards.

This web application can ve found at:
[The British Wine Cellar](https://the-british-wine-cellar.herokuapp.com/)

## UX
### User Stories
See attached link to Google Sheets doc

# Viewing and navigation
* As a shopper I want to be able to:
- view a list of wines that are available so that I can select some to purchase.
- view the details of each individual bottle of wine so that I can identify the price, learn about the wine from a description, read views, see a product image.
- quickly identify deals, delivery offers and combination deals so that I can take advantage of savings and get good value for money.
- easily view the total of my purchases at any time so that I can avoid spending too much.

# Registration and user accounts
* As a site user I want to be able to:
- easily register for an account so that I can have a personal account and be able to view my profile.
- easily login or logout so that I can access my personal information.
- easily recover my password in case I forget it so that I can recover access to my account.
- receive an email confirmation after registering so that I can verify my account registration was successful.
- have a personalised user profile so that I can view my personal order history and order confirmations, and save my payment information.

# Sorting and searching
* As a shopper I want to be able to:
- sort the available products so that I can easily identify the best rated, best priced and catergorically sorted products.
- sort a specific category of products so that I can find the best priced, best rated in a specific category or sort the products in that category by name.
- sort multiple categories of products simultaneously so that I can find the best priced or best rated prodicts across broad categories, such as by region, or type of wine.
- search by product name or description so that I can find a specific product I'd like to purchase.
- easily see what I have searched for in the results so that I can quickly decide whether the product I want is available.

# Purchasing and checkout
* As a shopper I want to be able to:
- easily select the quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product or quantity.
- view the items in my bag to be purchased so that I can identify the total cost of my purchase and all the items I will receive.
- adjust the quantity of individual items in my bag so that I can easily make changes to my purchase before checkout.
- easily enter payment information so that I can checkout quickly and with no hassles.
- feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
- view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
- receive an email confirmation after checking out so that I can keep the confirmation of what I have purchased for my records.

# Admin and store management
* As a store owner I want to be able to:
- Add a product so that I can add new items to my store.
- edit / update a product so that I can change the product proces, descriptions, images and other product criteria.
- delete a product so that I can remove items that are no longer for sale.


### Wireframes - links from Adobe XD
The wireframes for this web app were created using AdobeXD.

[Wireframe](https://xd.adobe.com/view/075a783b-58bd-46c7-b232-beef62f8d1e6-5209/)

PDF files also available in the project folders.

## Features
### Feature 1 - Search, filter and Sort by wine type, vineyard, different grapes and regions
* Shoppers can use the navigation dropdowns on the main header to filter under different categories, including wine type (i.e red, white, sparkling and rose.
* Shoppers can also use the search bar to search for a given term.
* Shoppers can use the filter dropdown tool in the product views to filter by different categories.

### Feature 2 - Browse, view and purchase a bottle of wine
* Shoppers can browse the selection of wines and the follow the links to see the product details. 
* If they like what they can see they can add the wine to their basket and purchase using the secure payment system, Stripe.

### Feature 3 - Create an account and view order history
* Users can create an account when  purchasing a product then view the history of their orders by logging in securely into their own profile.

### Feature 4 - Store Owners can add, edit, update and delete products from their store
* Store owners have superuser access and can log into the management side of the store. Once authenticated they can add, eit, update and delete products.


## Technologies Used
* CSS
* html
* Python
* Flask
* Jinja
* Bootstrap 
* JavaScript
* JQuery 
* Allauth
* Stripe payment system
* Amazon Web Service for hosting of static and media files
* Heroku - for Deployment
* GitPod - the IDE use to develop this web app
* SQLite
* Django


## Testing
### Test 1: Testing not completed at time of writing.

### Test 2: 

### Test 3: 

### Test 4: 

### Test 4: 

### Device Testing
(AWS caused an issue meaning I have been unable to upload media and static files for Heroku to deploy.)

Basic automated testing has been set up in the test_events.py as a starting point. This follows the Python unittest framework, which can be found here:

[Python Unittest](https://docs.python.org/3/library/unittest.html)

## Bugs and Problems
### 
* Selecting the 'save information to my account' was causing an error
* Email verification not fully setup with Google smtp.
* AWS caused issue with uploading media files due to issue with 'storage class'
* Minor CSS / Boostrap issue causing tow mobile navs to load.
* Order history in the My Profile template is not showing correctly.

### Deployment
#### Heroku
The site was deployed using Heroku. 

1. Create an Heroku app with a unique app name.
2. Link Heroku to your local GutHub respository
3. Create the following files, using the CLI as stated below:
    - pip3 freeze --local > requirements.txt
    - echo web: python app.py > Procfile

#### Local Deployment
You can also deploy the project locally by following the `clone / download` link from the main repository page and copy the link.  Then, open up a new terminal in your IDE and type 'git clone' followed directly by the copied link.

## New Features to follow in the next version
* Improved sorting functionality to icnlude checkbox searching to refine categories further and more precisely.
* Improved navigation to include 'mega-menu styling navbar for easier more intuitive navigation.
* Inventory tracking for products.
* Improved security in payment and addtion of Google and Apple pay.
* Complete email setup with GMail SMTP
* Make further customisations to all templates, including Allauth templates.
* Add messaging using Bootstrap Toasts
* Remove the comma in the list of 'grapes' in the product description.
* Complete email verification setup.

## Credits
* The use of the Code Institute tutuorial videos (of Boutique Ado) were essential in completing this project, particularly in completing the secure checkout functionality (webhook, webhook handlers and use of Stripe). There are elements of the code from the the Boutique Ado project running this project but they have been adapted to meet the needs of a different store - for the purpose of The British Wine Cellar.
* Some templates remain overly-similar to the Boutique Ado where the videos were followed and was there not enough time was allowed for the customisation of all templates. This remains a point for future development of this project beyond submission.

