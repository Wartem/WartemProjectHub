![Python](https://img.shields.io/badge/language-Python-blue.svg)
![HTML](https://img.shields.io/badge/language-HTML-orange.svg)
![CSS](https://img.shields.io/badge/language-CSS-green.svg)
![Flask](https://img.shields.io/badge/framework-Flask-lightgrey.svg)
![Jinja](https://img.shields.io/badge/template%20engine-Jinja-yellow.svg)

# WartemProjectHub

## Overview
WartemProjectHub is a centralized platform for managing and showcasing various projects developed under the name Wartem. This hub provides a unified interface for accessing multiple projects, each with its own unique functionality and purpose.

## Table of Contents
- [Deployment](#deployment)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Project Hub](#running-the-project-hub)
  - [Creating a New Project](#creating-a-new-project)
- [Project List](#project-list)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features
- Centralized management of multiple projects
- Dynamic project discovery and integration
- Easy-to-use interface for navigating between projects
- Customizable project display names
- Automated project creation tool

## Deployment
This application is deployed and accessible at the following URLs:
- [https://9jh73c-5000.csb.app/](https://9jh73c-5000.csb.app/)

You can visit these links to interact with the live versions of the application.

## Project Structure
```
WartemProjectHub/
├── main_app.py # Main application file
├── wsgi.py # WSGI entry point
├── requirements.txt # Main project dependencies
├── create_project.py # Script for creating new projects
├── templates/ # HTML templates for the main app
│ ├── base.html
│ └── home.html
├── static/ # Static files (CSS, JS, images)
├── projects/ # Directory containing all projects
│ ├── existing_project/
│ │ ├── init.py
│ │ ├── project_config.json
│ │ ├── project_main.py
│ │ ├── routes.py
│ │ └── templates/
│ │ ├── index.html
│ │ └── project.html
│ └── new_project/
│ ├── ...
└── project_template/ # Template for new projects
├── init.py
├── project_config.json
├── project_main.py
├── routes.py
└── templates/
├── index.html
└── project.html
```

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation
1. Clone the repository:
git clone https://github.com/Wartem/WartemProjectHub

2. Navigate to the project directory:
   cd WartemProjectHub
   
4. Install the required dependencies:
   pip install -r requirements.txt

## Usage

### Running the Project Hub
1. Start the application: python app.py
2. Open a web browser and navigate to `http://localhost:5500`

### Creating a New Project
1. Run the project creation script: python create_project.py

2. Follow the prompts to name your project and set up initial configurations.

## Project List
- A version of [CO2-Transport-Calculator-Example](https://github.com/Wartem/CO2-Transport-Calculator-Example)

## Acknowledgements
This project was developed with the significant assistance of Perplexity AI (https://www.perplexity.ai), an innovative AI tool that greatly facilitated the research and development process. Perplexity AI provided invaluable guidance on project structure, coding practices, and documentation. It helped streamline the gathering of information and offered crucial insights into the structure and functionality of the application.

## License
This project is licensed under the MIT License.
