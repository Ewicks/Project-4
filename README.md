# Universal Blogs

## Introduction
Universal Blogs is a website that shares articles on any topic the user wants to post about, the main topics like: technology, sports and business are categorised already. If the user wants to seatch for a less popular topic they can browse the other article category or search for the article in the search bar.

This website allows all users to be able to post, add, edit and delete their posts. All they need is an account which they will have to sign up for.

## Preview
- all responsive image goes hereeeeeee

### Live Website
To visit the deployed website click [here](https://universal-blogs-project-4.herokuapp.com/)


# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [UX](#ux-user-experience)
- [Agile Development Process](#agile-development-process)
- [Design](#design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)


## UX User Experience
### User Stories

### Site Admin/Creator:
* Restrict users access to users that have not been registered
* Superuser will have full access

### Site User
* Able to sign up and create an account to access certain functionality
* Be able to create, edit, delete, comment, like and unlike posts
* To be able to search up any article using the search bar


## Design
### Wireframes
<details>
  <summary>Click here to view all wireframes both Desktop & mobile:</summary>

  ![](doc/wireframes/wireframe-home.png)
  ![](doc/wireframes/wireframe-about.png)
  ![](doc/wireframes/wireframe-blog.png)
  ![](doc/wireframes/wireframe-contact.png)
  

  </details>


### Database Schema

The Post table is used when the user wants to create a article and post it on the website.

The Comment table is used when users add a comment to a post.

The Contact table is used when users submit the form in the contact us page.

![](doc/images/database-scheme.png)
  


## features 

### navbar

- I have created a navbar with a signin and logout button which is displayed when the user is not logged in. When the user logs in, those two buttons disappear and will be replaced with a Signout button. 

![Navbar](doc/images/navbar.png)

### Home Page

- If the user is not logged in, a sign up button will appear on the home page. This button will be replaced with a sign out button if user is logged in.

![Home Page](doc/images/home-page.png)


### About Page

- The About page displays illustrations and instructions on how to create a blog post.

![About Page](doc/images/about-page.png)


### Blog Page

- This page displays all blog posts that have been posted. At the end of the page there is category and latest post widget.

- If there if more than 6 posts on this page, then page navigation will appear below the posts section, allowing the user to press next, previous or final pape depending on how many articles there are.

![Blog Page](templates/blog.html)


### Contact Page

- If the user enters all the details, the form will then allow them to submit the infomation which will be stored in the django database which can be accesed via an admin account.

![Contact Page](doc/images/contact-page.png)


### Article Page

- The Article page displays the fulll article, along with the a comments section and the ability to like a post.

![Article Page](doc/images/article-page.png)

### Topic Page

- When the user searches for an article or keyword, all the posts related to this search will appear making it easy for the user to find a specific article if there are many artciles on the blog page.

![]()

### Add Post

- The user will have to fill in all the details apart from the image before the form will allow the user to submit their post. After they pressed submit, the post will be added the first post on the first page and will be previewed in the latest post widget.

![Add Page](doc/images/addpost-page.png)

### Edit Post

- The user can edit their posts to there liking as many times as they want.

![Edit Page](doc/images/updatepost-page.png)


### Signup Page

- If the user has already got an account, they can press the login link to be directed to the login page.

![Signup Page](doc/images/signup-page.png)

### Login Page

- If the user has not created an account, the details they use to log in will not work.

![Login Page](doc/images/login-page.png)

### Admin Page with Superuser Access

![Admin Page](doc/images/admin-page.png)


### Contact Page Django Admin

- All Contact forms details will be stored in the contact section on the admin page in django, this includes the name, email and body of the message.

![Contact Django Page](doc/images/contact-django-admin.png)

### 404 Error Page

- This page provides a link to direct them back to the website if user gets a  navigational page error.

![404 Error Page](doc/images/404-page.png)


### Default Images 

- If the user does not submit an image, a default image will be displayed depending on what topic the user chooses. If the user chooses technology as the topic, the technology image will be displayed within that post. This prevents posts having no image to be displayed.

![Technology Image](static/images/technology.png)
![Business Image](static/images/business.png)
![Sports Image](static/images/sports.png)
![Other Image](static/images/other.png)

### Future Features

- Allowing the user to filter posts by how many likes and comments each post has.

- Allow each user to only edit or delete the posts they created.

- Create a section where a user can donate money too support the ongoing publications.

### Bugs/Errors encountered during development

- 

## Testing

### The W3C Markup Validator

