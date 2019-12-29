<template>
  <div id="paste-interface">
    <div id="paste-grid-container">
      <form v-on:submit="this.getPasteForm" id="paste-form">
        <input
          v-model="title"
          id="paste-form-title"
          name="title"
          type="text"
          placeholder="Title"
        >
        <textarea
          v-model="paste"
          id="paste-form-text"
          name="paste"
          spellcheck="false"
          cols="30" rows="15"
          placeholder="Paste">
        </textarea>
        <div id="paste-form-btn">
          <button type="button" @click="this.getPasteForm">Paste!</button>
        </div>
      </form>
    </div>
    {{ info }}
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import '../assets/static/axios_config'

export default Vue.extend({
  name: 'paste-interface',
  components: {
  },
  methods: {
    getPasteForm: function (): void {
      this.axios
        .post('paste/', {
          title: 'meu titulo',
          paste: this.paste
        })
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.error(error)
        })
    }
  },
  data () {
    return {
      info: null,
      title: '',
      paste: ''
    }
  },
  mounted () {
    this.axios
      .get('paste/')
      .then(response => (this.info = response.data))
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
