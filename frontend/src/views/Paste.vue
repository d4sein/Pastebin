<template>
  <div id="paste">
    <main-header ref="mainHeader"/>
    <paste-interface ref="pasteInterface"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import MainHeader from '@/components/MainHeader.vue'
import PasteInterface from '@/components/PasteInterface.vue'

export default Vue.extend({
  name: 'paste',
  components: {
    MainHeader,
    PasteInterface
  }
})
</script>
