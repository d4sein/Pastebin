<template>
  <div id="register-interface">
    <div id="register-flex-container">
      <form
        id="register-form"
        method="POST"
        @submit.prevent="sendForm"
      >
        <div class="input-error">{{ registerError }}</div>
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
          <p>Already has an account? <router-link to="login">Login</router-link>.</p>
        </footer>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import store from '../assets/static/vuex_config'

export default Vue.extend({
  name: 'register-interface',
  methods: {
    sendForm: function (event: any): void {
      this.usernameError = this.username.length ? '' : 'Username cannot be empty'
      this.passwordError = this.password.length ? '' : 'Password cannot be empty'
      this.passwordConfirmError = this.passwordConfirm.length ? '' : 'Confirm password cannot be empty'

      // This will be treated in the API but
      // for practicality sake it'll also be verified here
      // so it can easily update the error message
      if (this.password !== this.passwordConfirm) {
        this.passwordConfirmError = 'Confirm password doesn\'t match password'
      }

      let data: any = {
        'username': this.username,
        'password': this.password,
        'password-confirm': this.passwordConfirm
      }

      this.axios
        .post('register', data)
        .then(response => {
          if (response.status === 201) {
            store.commit('addToken', response.data.token)
            this.$router.push('paste')
          }
        })
        .catch(e => {
          if (e.status === 409) {
            this.registerError = 'This username is already registered'
          }
        })
    }
  },
  data () {
    return {
      registerError: '',
      username: '',
      usernameError: '',
      password: '',
      passwordError: '',
      passwordConfirm: '',
      passwordConfirmError: ''
    }
  },
  beforeCreate () {
    if (store.getters.token !== null) {
      this.$router.push('paste')
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
  .input-error-style();
}
</style>
