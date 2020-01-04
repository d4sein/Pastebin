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
import store from '../assets/static/vuex_config'

export default Vue.extend({
  name: 'login-interface',
  methods: {
    sendForm: function (event: any): any {
      this.usernameError = this.username.length ? '' : 'Username cannot be empty'
      this.passwordError = this.password.length ? '' : 'Password cannot be empty'

      let data: any = {
        username: this.username,
        password: this.password
      }

      this.axios
        .post('session', data, { auth: data })
        .then(response => (store.commit('addToken', response.data.token)))
        .catch(e => console.error(e))

      // this.$router.push('/paste')
      return event.preventDefault()
    }
  },
  data () {
    return {
      username: '',
      usernameError: '',
      password: '',
      passwordError: ''
    }
  }
  // computed: {
  //   usernameError (): string {
  //     return this.username.length ? '' : 'Username cannot be empty'
  //   }
  // }
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
