<template>
  <div id="paste-edit-interface">
    <div id="paste-edit-flex-container">
      <form id="paste-edit-form" @submit.prevent="savePaste">
        <div class="input-error">{{ titleError }}</div>
        <input id="paste-edit-form-title" v-model="paste.title">
        <div class="input-error">{{ contentError }}</div>
        <textarea
          id="paste-edit-form-text"
          v-model="paste.content"
          spellcheck="false"
          cols="30" rows="15"
        >
        </textarea>
        <div id="paste-edit-form-btn">
          <button type="submit">Save!</button>
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
  name: 'paste-content-interface',
  methods: {
    savePaste: function () {
      this.titleError = this.paste.title.length ? '' : 'Title cannot be empty'
      this.contentError = this.paste.content.length ? '' : 'Paste cannot be empty'

      let token: any = {
        'x-access-token': store.getters.token
      }

      this.axios
        .put(`paste?address=${this.address}`, this.paste, { headers: token })
        .then(response => {
          this.$router.push(`../paste/${this.address}`)
        })
        .catch(e => console.log(e))
    }
  },
  data () {
    return {
      paste: { 'title': '', 'content': '' },
      address: '',
      titleError: '',
      contentError: ''
    }
  },
  created () {
    this.address = this.$route.params.address

    this.axios
      .get(`paste?address=${this.address}`)
      .then(response => {
        this.paste = response.data
      })
      .catch(e => console.log(e))
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#paste-edit-flex-container {
  .window-container-style();

  width: 850px;
  margin: auto;
  margin-top: 100px;
}

#paste-edit-form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

#paste-edit-form-title {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#paste-edit-form-text {
  .text-input-style();

  height: 300px;
  margin: 5px 0;
}

#paste-edit-form-btn {
  button {
    .button-style();

    width: 100%;
    height: 25px;
    margin: 5px 0;
  }
}

.input-error {
  .input-error-style();
}
</style>
