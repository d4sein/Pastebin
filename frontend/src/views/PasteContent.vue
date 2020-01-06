<template>
  <div id="paste-content">
    <main-header ref="mainHeader"/>
    <paste-content-interface ref="pasteContentInterface"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import MainHeader from '@/components/MainHeader.vue'
import PasteContentInterface from '@/components/PasteContentInterface.vue'

export default Vue.extend({
  name: 'paste-content',
  components: {
    MainHeader,
    PasteContentInterface
  }
})
</script>
