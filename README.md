# Real-Time News Aggregator

## Project Overview
The Real-Time News Aggregator is a web application designed to streamline the consumption of news by aggregating content from multiple RSS feeds into a single interface. This project uses modern web technologies to enhance user experience by offering personalized content, efficient language translation, and accessible features. The aggregator is especially useful for users looking to save time and effort while staying updated with the latest news in their preferred language.

## Features
- **News Aggregation**: Automatically gathers news from five different sources’ RSS feeds, allowing users to access a curated stream of news articles in one place.
- **Article Recommendation System**: Utilizes user interaction data to provide personalized article recommendations, boosting engagement and making content discovery seamless.
- **Multilingual Article Summarization**: Features an extractive summarization tool for articles in Hindi, Gujarati, and English, which helps in reducing the reading time for users.
- **Voice Assistant Integration**: Incorporates a voice assistant to navigate through the application, enhancing usability and accessibility for all users.
- **Language Translation**: Implements AWS Translate to dynamically translate articles into Hindi, Gujarati, and English, significantly decreasing webpage latency by 60% and enhancing the user experience for non-native speakers.

## Technologies Used
- **Frontend**: HTML, CSS, ReactJS
- **Backend**: Django
- **Database**: SQLite
- **Natural Language Processing**: For summarization and translation features
- **AWS**: AWS Translate for real-time language translation

## Setup and Installation
1. **Clone the Repository**
   git clone (https://github.com/ShahVandit/AI-Based-News-Aggregator.git)
   cd AI-Based-News-Aggregator

2. **Install Dependencies**
   npm install
   pip install -r requirements.txt

3. **Run the Application**
   // Start the frontend
   npm start

   // Run the Django server
   python manage.py runserver

## Usage
After starting the application, navigate to `localhost:3000` in your web browser to view the news aggregator. Interact with the voice assistant by clicking the microphone icon and speaking commands to navigate through the application.

