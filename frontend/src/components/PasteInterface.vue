<template>
  <div id="paste-interface">
    <div id="paste-flex-container">
      <form
        id="paste-form"
        @submit="sendForm"
      >
        <div class="input-error">{{ titleError }}</div>
        <input
          id="paste-form-title"
          v-model="title"
          name="title"
          type="text"
          placeholder="Title"
        >
        <div class="input-error">{{ pasteError }}</div>
        <textarea
          id="paste-form-text"
          v-model="paste"
          name="paste"
          spellcheck="false"
          cols="30" rows="15"
          placeholder="Paste">
        </textarea>
        <div id="paste-form-btn">
          <button type="submit">Paste!</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import '../assets/static/axios_config'

export default Vue.extend({
  name: 'paste-interface',
  methods: {
    sendForm: function (event: any): any {
      // If any of the inputs is empty
      if (!this.title || !this.paste) {
        if (!this.title) {
          this.titleError = 'Title cannot be empty'
        } else {
          this.titleError = ''
        }

        if (!this.paste) {
          this.pasteError = 'Paste cannot be empty'
        } else {
          this.pasteError = ''
        }

        return event.preventDefault()
      } else {
        // Reset error messages
        this.titleError = ''
        this.pasteError = ''
      }

      let data = {
        'title': this.title,
        'content': this.paste
      }

      this.axios
        .post('paste', data)
        .then(response => (this.formResponse = response.data))
        .catch(e => console.error(e))

      return event.preventDefault()
    }
  },
  data () {
    return {
      formResponse: Object,
      title: '',
      titleError: '',
      paste: '',
      pasteError: ''
    }
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#paste-flex-container {
  .window-container-style();

  width: 850px;
  margin: auto;
  margin-top: 100px;
}

#paste-form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

#paste-form-title {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#paste-form-text {
  .text-input-style();

  height: 300px;
  margin: 5px 0;
}

#paste-form-btn {
  button {
    .button-style();

    width: 100%;
    height: 25px;
    margin: 5px 0;
  }
}

.input-error {
  font-style: italic;
  font-size: 13px;
  color: rgb(238, 26, 26);
}
</style>
