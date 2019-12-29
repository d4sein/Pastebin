<template>
  <div id="login-interface">
    <div id="login-grid-container">
      <form id="login-form" action="login" method="POST">
        <input id="login-form-username" name="username" type="text" placeholder="Username">
        <input id="login-form-password" name="password" type="text" placeholder="Password">
        <button id="login-form-btn" type="submit">Login</button>
        <footer id="login-form-footer">
          <p>Doesn't have an account? <a href="#">Register</a>.</p>
        </footer>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'login-interface'
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#login-grid-container {
  .window-container-style();

  width: 400px;
  height: 200px;
  margin: auto;
  margin-top: 100px;
}

#login-form {
  width: 100%;
  height: 100%;
  display: grid;
  grid-gap: 15px;
  grid-template-rows: repeat(3, 25px) 1fr;
}

#login-form-username {
  .text-input-style();
}

#login-form-password {
  .text-input-style();
}

#login-form-btn {
  .button-style();
}

#login-form-footer {
  position: relative;

  p {
    bottom: 0;
    position: absolute;
    font-size: 15px;
    color: @dark-gray;
  }
}
</style>
