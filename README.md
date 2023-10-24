# CineMatch: the long-distance movie date

## Description

CineMatch aims to revolutionize the way long-distance couples experience movies together. It's not just another movie recommendation app; it's a bonding experience. Our platform offers a simple yet interactive interface where couples can swipe right or left on a curated list of films, complete with IMDb and Rotten Tomatoes ratings. When both partners swipe right, it's a match! Now all that's left is to decide who's making the popcorn.

Potential extension:
A goodreads but for movies. Letterboxd exists but it's not free and doesn't have the smart recommendation features.

## Features

- Real-time Swiping: Sync your movie preferences in real-time.
- Curated Matches: A smart recommendation algorithm to match you with movies both will love.
- High-quality Movie Database: Comprehensive movie details with reviews and ratings.
- Instant Notifications: Get notified immediately when both of you swipe right on a movie.

## Want to contribute?

Check out this [article](https://opensource.guide/how-to-contribute/) if you're new.

- Community Impact: Help long-distance couples feel closer than ever.
- Technical Challenge: Work on real-time systems, data scraping, and complex matching algorithms.
- Practice new skills: Our stack includes Vue.js, FastAPI, PostgreSQL, and various cloud services, providing a learning opportunity across different technologies.

Check out the working draft of our [developer guide](docs/develop.md).

## Support

Your financial support will enable us to maintain server costs, API subscriptions, and further development to make CineMatch even better. Every contribution counts, use the sponsor button or contact me at <tanmayagrawa@umass.edu>!

## TODO

- Set Up cloud services
- Set up EC2 for hosting, RDS for the PostgreSQL database, S3 for static files, and Route53 for DNS management.
- API Integrations: Integrate TMDB, IMDb, and Rotten Tomatoes APIs. If IMDb and Rotten Tomatoes APIs are not available, you'll need to implement web scraping.

### Proposed LLM features
  
- Personalized Movie Descriptions: Use LLMs to write engaging, personalized movie descriptions based on users' past likes and preferences.

- Recommendation Explanations: When a match is made, use LLMs to provide a detailed explanation of why this movie could be a good choice for both users.

- Questions/Trivia/Hype: Implement a chat feature where the LLM can answer questions about the movie, discuss similar movies, or hype you up about the movie. For e.g. I personally love to know trivia or real-world connections.

- Tiebreaker: Use LLMs to summarize long reviews or aggregate multiple reviews into a concise summary for breaking ties.

## Backend Development

We're using FastAPI for the web framework, SQLAlchemy for ORM, and Pydantic for data validation because that's what i like. Fastapi's good because it's sufficiently performant among JS and Python [frameworks](https://www.techempower.com/benchmarks/#section=data-r21&test=query) but I am open to moving high-throughput endpoints to rust/go servers.

Implement the following endpoints:

- POST /login
- POST /signup
- POST /streaming_services
- GET /movies (also personalized descriptions)
- POST /swipe
- GET /match (also recommendation explanations)
- POST /hype
- GET /tiebreak

Also, implement real-time matching notifications using WebSocket.

## Frontend Development

Use Vue.js 3 for UI components, Axios for API requests, and Socket.io for real-time features. Develop the following components:

- Login/Signup Page
- Dashboard to display movie cards
- Notification/Messaging System

## Testing

Write unit tests for both frontend and backend.

## Deployment

Use Docker for containerization of both frontend and backend. For the initial stages, manual scaling should suffice. Later we can consider Kubernetes for orchestration.
