# Bottle Game Project

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [API Endpoints](#api-endpoints)

## Introduction

The Bottle Game is a unique web application where users can anonymously send and receive messages based on their geographical location. Users can create bottles, read bottles from others, and respond to them, all while maintaining their anonymity. The game encourages exploration and interaction among users in a fun and engaging way.

## Features

- **Anonymity**: Users can send and receive messages without revealing their identity.
- **Geolocation**: Messages (bottles) are delivered based on users' locations and specified distance ranges.
- **User Registration**: Users can register and log in to manage their activities.
- **Bottle Creation**: Users can create bottles with a message, which are sent randomly to other users within the specified distance.
- **Reading Bottles**: Users can read bottles sent by others, limited to a certain number per day.
- **Response Functionality**: Users can respond to bottles, creating a new bottle that reflects their response.
- **Shop System**: Users can purchase items to enhance their gameplay experience, such as unlimited bottle reads and the ability to respond to bottles.
- **Ranking System**: Users are ranked based on the number of bottles they have read, fostering competition.

## Technologies Used

- **Django**: Web framework for building the application.
- **Django REST Framework**: For creating APIs.
- **PostgreSQL**: Database management system.
- **HTML/CSS/JavaScript**: For the front-end interface.
- **Bootstrap**: For responsive design.



## API Endpoints

- **POST /api/register/** Register a new user.
- **POST /api/login/** User login.
- **GET /api/bottles/** List all bottles available to the user.
- **POST /api/bottles/create/** Create a new bottle.
- **POST /api/bottles/respond/{bottle_id}/** Respond to a specific bottle.
- **GET /api/shop/** View items available in the shop.
- **POST /api/shop/purchase/** Purchase an item from the shop.
- **GET /api/rankings/** View user rankings based on bottles read.

