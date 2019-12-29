<template>
  <div id="login">
    <main-header ref="mainHeader"/>
    <login-interface ref="loginInterface"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import MainHeader from '@/components/MainHeader.vue'
import LoginInterface from '@/components/LoginInterface.vue'

export default Vue.extend({
  name: 'login',
  components: {
    MainHeader,
    LoginInterface
  }
})
</script>
