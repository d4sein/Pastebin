<template>
  <div id="main-header">
    <ul>
      <li>Anonymous</li>
      <li>|</li>
      <li>Paste</li>
      <li>Login</li>
      <li>Register</li>
    </ul>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'main-header'
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
