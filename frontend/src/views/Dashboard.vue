<template>
  <div id="dashboard">
    <main-header ref="mainHeader"/>
    <dashboard-interface ref="DashboardInterface"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import MainHeader from '@/components/MainHeader.vue'
import DashboardInterface from '@/components/DashboardInterface.vue'

export default Vue.extend({
  name: 'dashboard',
  components: {
    MainHeader,
    DashboardInterface
  }
})
</script>
