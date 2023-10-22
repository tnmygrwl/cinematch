<template>
    <div v-if="show">
      <p>You matched on {{ movie.name }}!</p>
    </div>
  </template>
  
  <script>
  export default {
    props: ['show', 'movie'],
  };
  </script>
  