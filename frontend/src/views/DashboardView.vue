<template>
    <div>
      <h1>Dashboard</h1>
      <MovieCard
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
        @swiped="swipeMovie"
      />
    </div>
  </template>
  
  <script>
  import MovieCard from '@/components/MovieCard.vue';
  
  export default {
    name: 'DashboardView',
    components: {
      MovieCard,
    },
    data() {
      return {
        movies: [
          {
            id: 1,
            name: 'Inception',
            imdb: 8.8,
            rottenTomatoes: 87,
          },
          {
            id: 2,
            name: 'The Matrix',
            imdb: 8.7,
            rottenTomatoes: 88,
          },
          // use an API to get movies
        ],
      };
    },
    methods: {
      swipeMovie({ movie, action }) {
        // Handle the swipe action.
        // Typically, we would send this to our backend.
        console.log(`Swiped ${action} on ${movie.name}`);
  
        // Remove the movie from the list.
        this.movies = this.movies.filter(m => m.id !== movie.id);
      },
    },
  };
  </script>
  