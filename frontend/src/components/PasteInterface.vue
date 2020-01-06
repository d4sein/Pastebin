<template>
  <div id="paste-interface">
    <div id="paste-flex-container">
      <form
        id="paste-form"
        @submit.prevent="sendForm"
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
import store from '../assets/static/vuex_config'

export default Vue.extend({
  name: 'paste-interface',
  methods: {
    sendForm: function (event: any): any {
      this.titleError = this.title.length ? '' : 'Title cannot be empty'
      this.pasteError = this.paste.length ? '' : 'Paste cannot be empty'

      let data: any = {
        title: this.title,
        content: this.paste
      }

      let token: any = {
        'x-access-token': store.getters.token
      }

      this.axios
        .post('paste', data, { headers: token })
        .then(response => {
          if (response.status === 201) {
            this.$router.push(`paste/${response.data.address}`)
          }
        })
        .catch(e => console.error(e))
    }
  },
  data () {
    return {
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
