<template>
  <div id="main-header">
    <ul>
      <li v-if="user.username"><router-link to="dashboard">{{ user.username }}</router-link></li>
      <li v-else>Anonymous</li>
      <li>|</li>
      <li><router-link to="paste">Paste</router-link></li>
      <li><router-link to="login">Login</router-link></li>
      <li><router-link to="register">Register</router-link></li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import '../assets/static/axios_config'
import store from '../assets/static/vuex_config'

export default Vue.extend({
  name: 'main-header',
  data () {
    return {
      user: {}
    }
  },
  mounted () {
    let token: any = {
      'x-access-token': store.getters.token
    }

    this.axios
      .get('session', { headers: token })
      .then(response => (this.user = response.data))
      .catch(e => console.error(e))
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#main-header {
  width: 100%;

  ul {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    padding: 5px;

    li {
      padding: 0 8px;
      color: @dark-gray;

      a {
        color: @dark-gray;

        &:hover {
          color: @white;
        }
      }
    }
  }
}
</style>
