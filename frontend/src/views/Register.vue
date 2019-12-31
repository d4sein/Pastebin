<template>
  <div id="register">
    <main-header ref="mainHeader"/>
    <register-interface ref="registerInterface"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import MainHeader from '@/components/MainHeader.vue'
import RegisterInterface from '@/components/RegisterInterface.vue'

export default Vue.extend({
  name: 'register',
  components: {
    MainHeader,
    RegisterInterface
  }
})
</script>
