<template>
  <div id="register-interface">
    <div id="register-grid-container">
      <form id="register-form">
        <input
          id="register-form-username"
          name="username"
          type="text"
          placeholder="Username"
        >
        <input
          id="register-form-password"
          name="password"
          type="text"
          placeholder="Password"
        >
        <input
          id="register-form-password-confirm"
          name="password-confirm"
          type="text"
          placeholder="Confirm password"
        >
        <button id="register-form-btn" type="submit">Register</button>
        <footer id="register-form-footer">
          <p>Already has an account? <a href="#">Login</a>.</p>
        </footer>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'register-interface'
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#register-grid-container {
  .window-container-style();

  width: 400px;
  height: 240px;
  margin: auto;
  margin-top: 100px;
}

#register-form {
  width: 100%;
  height: 100%;
  display: grid;
  grid-gap: 15px;
  grid-template-rows: repeat(4, 25px) 1fr;
}

#register-form-username {
  .text-input-style();
}

#register-form-password {
  .text-input-style();
}

#register-form-password-confirm {
  .text-input-style();
}

#register-form-btn {
  .button-style();
}

#register-form-footer {
  position: relative;

  p {
    bottom: 0;
    position: absolute;
    font-size: 15px;
    color: @dark-gray;
  }
}
</style>
