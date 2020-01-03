<template>
  <div id="login-interface">
    <div id="login-flex-container">
      <form
        id="login-form"
        method="POST"
        @submit="sendForm"
      >
        <div class="input-error">{{ usernameError }}</div>
        <input
          id="login-form-username"
          v-model="username"
          name="username"
          type="text"
          placeholder="Username"
        >
        <div class="input-error">{{ passwordError }}</div>
        <input
          id="login-form-password"
          v-model="password"
          name="password"
          type="text"
          placeholder="Password"
        >
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
import '../assets/static/axios_config'
import { Method } from 'axios'

export default Vue.extend({
  name: 'login-interface',
  methods: {
    sendForm: function (event: any): any {
      // If any of the inputs is empty
      if (!this.username || !this.password) {
        if (!this.username) {
          this.usernameError = 'Username cannot be empty'
        } else {
          this.usernameError = ''
        }

        if (!this.password) {
          this.passwordError = 'Password cannot be empty'
        } else {
          this.passwordError = ''
        }

        return event.preventDefault()
      } else {
        // Reset error messages
        this.usernameError = ''
        this.passwordError = ''
      }

      let data = {
        'username': this.username,
        'password': this.password
      }

      this.axios
        .post('session', data)
        .then(response => (this.formResponse = response.data))
        .catch(e => console.log(e))

      return event.preventDefault()
    }
  },
  data () {
    return {
      formResponse: Object,
      username: '',
      usernameError: '',
      password: '',
      passwordError: ''
    }
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#login-flex-container {
  .window-container-style();

  width: 400px;
  margin: auto;
  margin-top: 100px;
}

#login-form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

#login-form-username {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#login-form-password {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#login-form-btn {
  .button-style();

  height: 25px;
  margin: 5px 0;
}

#login-form-footer {
  p {
    margin-top: 35px;
    font-size: 15px;
    color: @dark-gray;
  }
}

.input-error {
  font-style: italic;
  font-size: 13px;
  color: rgb(238, 26, 26);
}
</style>
