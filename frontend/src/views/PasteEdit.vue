<template>
  <div id="paste-edit">
    <main-header ref="mainHeader"/>
    <paste-edit-interface ref="pasteEditInterface"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import MainHeader from '@/components/MainHeader.vue'
import PasteEditInterface from '@/components/PasteEditInterface.vue'

export default Vue.extend({
  name: 'paste-edit',
  components: {
    MainHeader,
    PasteEditInterface
  }
})
</script>
