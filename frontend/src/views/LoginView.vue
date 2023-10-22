<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Enter username" />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LoginView',
    data() {
      return {
        username: '',
      };
    },
    methods: {
      login() {
        // this.$emit('login', this.username);
        // bypass the login to go to the dashboard for now
        this.$router.push({ name: 'dashboard' });
      },
    },
  };
  </script>
  