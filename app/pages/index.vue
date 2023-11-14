<template>
  <h1>Login to enter the petting zoo:</h1>
  <label>
    Username:
    <input type="text" v-model="state.username" />
  </label>
  <br />
  <br />
  <label>
    Password:
    <input type="password" v-model="state.password" />
  </label>
  <br />
  <br />
  <button @click="login" :disabled="loginNotAllowed()">Login</button>
  <p v-if="warning">{{ warning }}</p>
</template>

<script setup>
const state = reactive({
  username: '',
  password: '',
});
const warning = ref('');
function loginNotAllowed() {
  return state.username.length == 0 || state.password.length == 0;
}
async function login() {
  const response = await $fetch('/api/login', {
    method: 'POST',
    body: state,
  });
  if (response) {
    navigateTo('/zoo');
  } else {
    warning.value = 'Login failed :(';
  }
}
</script>

<style>
* {
  font-family: sans-serif;
}
</style>
