<template>
  <div id="paste-interface">
    <div id="paste-grid-container">
      <form id="paste-form" action="paste" method="POST">
        <input id="paste-form-title" name="title" type="text" placeholder="Title">
        <textarea id="paste-form-text" name="paste"
        spellcheck="false" cols="30" rows="15" placeholder="Paste"></textarea>
        <div id="paste-form-btn">
          <button type="submit">Paste!</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'paste-interface',
  components: {
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#paste-grid-container {
  .window-container-style();

  width: 850px;
  height: 400px;
  margin: auto;
  margin-top: 100px;
}

#paste-form {
  width: 100%;
  height: 100%;
  display: grid;
  grid-gap: 5px;
  grid-template-rows: 25px 1fr 45px;
}

#paste-form-title {
  .text-input-style();
}

#paste-form-text {
  .text-input-style();
}

#paste-form-btn {
  position: relative;

  button {
    .button-style();

    bottom: 0;
    position: absolute;
    width: 100%;
    height: 25px;
  }
}
</style>
