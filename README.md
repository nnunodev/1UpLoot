# 1UpLoot

<p align="center"> <img width="800" height="500" src="data/page_image/site_screenshot.png"></p>

> **Note:** the original Heroku deployment is retired (Heroku's free tier ended in 2022).
> Run it locally using the setup steps below.

## Index

* [Project description](#project-description)
* [UX](#ux)
* [Features](#features)
* [Wireframes](#wireframes)
* [Technologies](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Disclaimer](#disclaimer)

## Project Description

1UP Loot is a web application, designed for physical game collectors to plan, track and organize their collections. All information the user creates is saved into a database, so they can easily access their collections on every device. All major genres and platforms are supported including retro gaming systems.
Users can add, search, edit, delete their games into the web app. Each game entry has several fields: Game Name, Game Platform, Game Genre, Pickup Date, Game Store, Game Price, Current Value, Game condition and Game Image.
With Game Image users can add a url 200x200 hosted cover image of their choice.

## UX

### Who is it for

* Avid Game collectors that have big collections for several game systems.
* New collectors that are starting to collect games.
* General users that want a place to organize and manage their games library.

### User Stories

* As a user/collector, I want to easy navigate and find the information I need quickly.
* As a collector, I want to add all possible information I have about my games.
* As a user/collector, I want to be able to use my collection on all my devices.
* As a collector, I want to be able to edit information on all my games, so I can update their current value, prices or vendors.
* As a user/collector, I want to be able to remove any games from my library, in case I sell or trade any of them.
* As a user/collector, I want to be able to filter my games per game system or genre, so I can have an overview on what games I already own.
* As a collector, I want to have the option to add retro gaming systems, in case I decide to collect any games for those systems.
* As a user/collector, I want to have all major platforms available to me so I can add all games from my collection.

## Features

### Existing Features

* Navbar
  * Allows user to navigate easily through the different sections of the page.

* About
  * A simple introduction to the app, so the user can have a brief idea on what it does without overloading with lots of information. They have a sign-up button below if they decide to discover more about it.

* Features section
  * Gives a brief description on the app's features. The user can have an overview on what they can do with the app, in a simple way with easy to read icons for each feature and a relevant description below.

* Footer
  * Provides links to the relevant social websites.

* Login
  * Simple form where the user can use their created credentials from the "Register Account" page to login and start to use the app's features to create their library.

* Register Account
  * If the user decides to use the app, they're able to create an account and access all of the app's features. All passwords are encrypted in the database, to enhance security.

* User Session
  * When the user is logged in, they're able to create their collection, Add/Edit/Delete/Modify their games, in a more private and personalized way.

* Filter
  * User can filter their games by Platforms and Game genres, helping giving a better overview of what games they have for each platform or genre.

* Add/Edit/Delete tasks
  * User can add any games they want and remove them. They're able to edit any games that were added as well.
  
### Features left to implement

As I develop my skills, I would like to implement more features in this app like:

* Detailed search system
  * Would be useful for users with bigger collections to be able to have access to a more detailed search.
* Upload game images
  * Ability to upload images, instead of using URLs.
* Wishlist
  * A feature for collectors to help them find the games they don't have in their collection.
* Share feature
  * Ability to share their private collections to fellow collectors through the app with a public generated link with read only permissions.
* Community/Forum
  * A blog/forum for all users and collectors curious about the subject, can join and discuss their favourite hobby.

## Wireframes

Wireframes done with Balsamiq, available here:

* [Desktop](https://github.com/Brainvibe/1UpLoot/blob/master/data/wireframes/Desktop.png)
* [Mobile](https://github.com/Brainvibe/1UpLoot/blob/master/data/wireframes/Mobile.png)
* [Tablet](https://github.com/Brainvibe/1UpLoot/blob/master/data/wireframes/Tablet.png)

## Technologies Used

* **HTML**
  * The project uses HTML to structure the DOM.

* **CSS**
  * Used to style webpages.

* **[Flask](http://flask.palletsprojects.com/en/1.1.x/)**
  * Used to generate pages, generate dynamic links, and content within the application.

* **[Python 3](https://www.python.org/)**
  * Used to integrate Flask in this project and all CRUD tasks.

* **[Mongodb](https://cloud.mongodb.com)**
  * Database used for this project, for CRUD (create, read, update & delete) tasks.

* **[PyMongo](https://api.mongodb.com/python/current)**
  * Used to connect and transfer data to and from MongoDB.

* **[Materialize](https://materializecss.com/)**
  * Web Framework used in the project based on Material Design by Google.

* **[Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)**
  * Used to encrypt all users passwords in the database.

* **[JQuery](https://jquery.com)**
  * The project uses JQuery to initialize Materialize CSS components

* **[Font Awesome](https://fontawesome.com/)**
  * Used for footer icons.

* **[Materialize Icons](https://materializecss.com/icons.html)**
  * All icons in the webpage except the footer which are from Font Awesome.

* **[Heroku](https://www.heroku.com/)**
  * Used to deploy the live website.

* **[Google Fonts](https://fonts.google.com/)**
  * "Covered By Your Grace" for logo and "Open Sans Condensed" with two font weight variants for the rest of the page.

## Testing

### W3C Validation Services

* ```Attribute with not allowed on element img at this point```
  * Had a typo in img: ```with``` instead of ```width```, changed and fixed.
* ```An img element must have an alt attribute, except under certain conditions.```
  * Fixed missing ```alt``` attribute to img.
* ```No space between attributes.```
  * Fixed the space between attributes

### W3C Link Checker

* No errors, all links working properly. Only two links were not able to be tested by the tool. Here's the console log:

  ```info Line: 333 https://www.facebook.com/
       Status: (N/A) Forbidden by robots.txt
       The link was not checked due to robots exclusion rules. Check the link manually.
       info Line: 338 https://www.twitter.com/
       Status: (N/A) Forbidden by robots.txt
       The link was not checked due to robots exclusion rules. Check the link manually.
  ```

  * Both links were tested manually and working.
  
### CSS Validation service

* All errors were from third party errors and css issues in Materilize like so:

  ```Sorry! We found the following errors (1)
    URI : https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css
    13 .table-of-contents a Value Error : letter-spacing only 0 can be a unit. You must put a unit after your number : 0.4
  ```

## Google dev tools

### Accessibility

* ```Background and foreground colors do not have a sufficient contrast ratio```
  * This was related to the description text color and sign up button color, changed and fixed.
* ```Links do not have a discernible name```
  * Footer links didn't have a proper name, added ```aria-label``` to all links changed and fixed.
* It's now scored 100.

### SEO

* ```Document does not have a meta description```
  * Fixed by adding Metadata
* ```Links do not have a discernible name```
  * Footer links didn't have a proper name, added ```aria-label``` to all links changed and fixed.

### Best Practices

* ```Includes front-end JavaScript libraries with known security vulnerabilities 3 vulnerabilities detected```
  * This was due to be using a vulnerable and outdated version of jQuery 3.2.1, updated and changed to the latest version 3.5.1

### Performance

* Performance locally is at 94, but due to heroku deployment, the performance took a big hit going to 74. This is all due to the third-party requests.

## Non-automated testing

### Links

* All links, were checked manually to ensure that all pages were being opened/redirected correctly.
* All footer social icons were checked as well, to make sure they were opening on a new tab.

### Login

* Typed incorrect credentials in order to see if the correct error message was given to the user.
* Tried to login without any text in the input fields to test the validation and feedback message to the user, on both username and password.
* Tested sign up link, to see if it was redirected correctly to register page.
* Tested after login if the user was correctly displayed in the navbar.
* Tested if the correct navbar options were being displayed after login.
* Tested all links after the user is logged in.

### Register

* Typed username that existed already in the database to see if the feedback message was given to the user.
* Typed without any text to see if the form validation was working and the appropriate messaging was delivered to the user.
* Typed only username to test the validation to avoid creating accounts without user name.
* Typed only password to avoid creating accounts without any passwords and the correct message was given to the user.  
* Tested if the register routine was working correctly and not allowing creation of duplicate users. For each entry I've check in mongodb if there was any duplicate entries.

### Logout

* Tested if the user was logged out completely from the page, by checking the session in dev tools.
* Checked if the correct navbar options were displayed correctly after logout by checking if the user was authenticated or not.
* Tested all links after being logged out to see if everything was redirected correctly.

### Filter

* Added a game for each platform and genres, to test if all searches were being done correctly.
* Ran a filter search for all platforms, retro platforms and genres, to test if the games that were showing up in the results were not from other users, and only from the session user authenticated.

### Loot/Game list

* Tested if loop.index was corrected implemented by adding several games, and make sure a unique modal was opened for each game.
* Tested opening modal for each game and made sure that the Edit and OK buttons were being redirected to the game that was selected.
* Added several games to test if all values were introduced correctly in the database and showing correctly in modal.
* Tested if all games were showing correctly for the relevant user and not for all users. This was done by creating several different accounts and by adding several games to different users' libraries.

### Add Games

* Tried to submit different values on all fields to check if they were being saved correctly in the database.
* Tested validation forms, by not entering any text on the required fields, confirming that the user got the correct feedback message.
* Tried to open "add" games page URL without a user being authenticated, to see if it was redirected and got the appropriate message.
* Added game for each platform, genre and game condition, to test if all values were sent correctly to the database.

### Edit Games

* Edited every entry, to see if all the information was saving correctly to the database.
* Opened manually the "edit" games page link without a user being authenticated to avoid a non-user to edit the information on an user's account.

### Delete

* Delete task was tested several times with different users logged in, to see if the correct games were being deleted for a single user, and not for all users.
* Tested the delete task on results and results_genre to check if everything was being redirected correctly.
* Several combinations of modal delete confirmation, were tested to make sure the game wasn't being deleted by choosing the incorrect option.

### Tested Devices

* Apart from using the dev tools to see if the site was responsive across different resolutions, I've tested all features on the following devices:
  * One Plus 7 pro
  * Fire HD 10
  * Ipad mini 4
  * Iphone 11
  * Macbook Pro 13"
  * Windows 10 desktop

### Tested Browsers

* To ensure browser compatibility I've tested all features above on the following browsers:
  * Chrome
  * Firefox
  * Safari

## Deployment

### Running this project locally

These instructions will be for [Visual Studio Code](https://code.visualstudio.com/), as the project was developed using this code editor.

#### Requirements

* [Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/downloads)
* [Python 3](https://www.python.org/)
* [MongoDB Atlas](https://www.mongodb.com/) account
* [pip](https://pypi.org/project/pip/)

After you have everything installed, start by cloning the project from GitHub:

* Go to [GitHub repository](https://github.com/Brainvibe/1UpLoot).
* Under the repository name, click the green "Clone or download" button.
* In the Clone with HTTPs section, copy the clone URL for the repository.
* Open the terminal in your IDE.
* Change the current working directory to the location where you want the cloned directory to be created.
* Copy paste the following command:

```git clone https://github.com/Legaeldan/milestone-3```

The repository is now cloned.

* Install the requirements needed to run the project from the terminal using the following command:

```pip3 install -r requirements.txt```

* After pip installs all packages, just type ```python app.py``` in the terminal and it will now run locally.

### Deployment to Heroku

To deploy this project to Heroku, follow these steps:

* Log into [Heroku](https://dashboard.heroku.com/).
* From the main dashboard, select the **New** dropdown, then select **Create new app**.
* Give your app a unique name, and select the region you wish to deploy to.
* After the app is created, select **Deploy** from the top of the page, and scroll down to **Deployment Method**.
* Select **GitHub** as the method of deployment.
* Log in using your **Github credentials**.
* Select your username, and search for the reposity in the **repo-name** box.
* Select **Connect** on the repository you wish to connect to.
* Under **Manual deploy**, select the branch you wish to deploy, and hit **Deploy Branch**.
* After the application is built, select **Settings** from the top of the page.
* Select **Reveal Config Vars**.
* Add the config keys for **IP**, **PORT**, **MONGO_URI**, **MONGO_DBNAME**, and **SECRET_KEY**.
* Select **More** from the top right of the page, and select **Restart all dynos**.

## Credits

### Media

* Main photos were downloaded from [Broforce Game](https://broforcegame.com/)

### Acknowledgements

* Smooth Scrolling from [W3schools](https://www.w3schools.com/howto/howto_css_smooth_scroll.asp).
* Login system based on [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE).
* Most CRUD tasks were based on Code Institute Lessons for this module.
* A big thanks to all students and leads from slack channel #data-centric-dev for their help and feedback.

As always, I want to thank my mentor [Victor Miclovich](https://github.com/miclovich) for his great knowledge and experience with valuable feedback in our mentoring sessions.

## Disclaimer

### All content for educational use only
