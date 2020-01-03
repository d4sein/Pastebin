<template>
  <div id="main-header">
    <ul>
      <li v-if="user.username">{{ user.username }}</li>
      <li v-else>Anonymous</li>
      <li>|</li>
      <li>Paste</li>
      <li>Login</li>
      <li>Register</li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import '../assets/static/axios_config'

export default Vue.extend({
  name: 'main-header',
  data () {
    return {
      user: Object
    }
  },
  mounted () {
    this.axios
      .get('session')
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
    }
  }
}
</style>
