<template>
  <div id="register-interface">
    <div id="register-flex-container">
      <form
        id="register-form"
        method="POST"
        @submit="sendForm"
      >
        <div class="input-error">{{ usernameError }}</div>
        <input
          id="register-form-username"
          v-model="username"
          name="username"
          type="text"
          placeholder="Username"
        >
        <div class="input-error">{{ passwordError }}</div>
        <input
          id="register-form-password"
          v-model="password"
          name="password"
          type="text"
          placeholder="Password"
        >
        <div class="input-error">{{ passwordConfirmError }}</div>
        <input
          id="register-form-password-confirm"
          v-model="passwordConfirm"
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
  name: 'register-interface',
  methods: {
    sendForm: function (event: any): any {
      // If any of the inputs is empty
      if (!this.username || !this.password || !this.passwordConfirm) {
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

        if (!this.passwordConfirm) {
          this.passwordConfirmError = 'Confirm password cannot be empty'
        } else {
          this.passwordConfirmError = ''
        }

        return event.preventDefault()
      } else {
        // Reset error messages
        this.usernameError = ''
        this.passwordError = ''
        this.passwordConfirmError = ''
      }

      // This will be treated in the API but
      // for practicality sake it'll also be verified here
      // so it can easily update the error message
      if (this.password !== this.passwordConfirm) {
        this.passwordConfirmError = 'Confirm password doesn\'t match password'

        return event.preventDefault()
      }

      let data = {
        'username': this.username,
        'password': this.password,
        'password-confirm': this.passwordConfirm
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
      passwordError: '',
      passwordConfirm: '',
      passwordConfirmError: ''
    }
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#register-flex-container {
  .window-container-style();

  width: 400px;
  margin: auto;
  margin-top: 100px;
}

#register-form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

#register-form-username {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#register-form-password {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#register-form-password-confirm {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#register-form-btn {
  .button-style();

  height: 25px;
  margin: 5px 0;
}

#register-form-footer {
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
