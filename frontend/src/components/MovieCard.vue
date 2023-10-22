<template>
  <div>
    <h3>{{ movie.name }}</h3>
    <p>IMDB: {{ movie.imdb }}</p>
    <p>Rotten Tomatoes: {{ movie.rottenTomatoes }}</p>
    <button @click="swipe('like')">Like</button>
    <button @click="swipe('dislike')">Dislike</button>
  </div>
</template>

<script>
export default {
  props: ['movie'],
  methods: {
    swipe(action) {
      this.$emit('swiped', { movie: this.movie, action });
    },
  },
};
</script>
