<template>
  <div id="paste-content-interface">
    <div id="paste-content-flex-container">
      <form id="paste-content-form">
        <input id="paste-content-form-title" v-model="paste.title">
        <textarea
          id="paste-content-form-text"
          v-model="paste.content"
          spellcheck="false"
          cols="30" rows="15"
        >
        </textarea>
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
  data () {
    return {
      paste: {}
    }
  },
  created () {
    let address = this.$route.params.address

    let token: any = {
      'x-access-token': store.getters.token
    }

    this.axios
      .get(`paste?address=${address}`, { headers: token })
      .then(response => {
        this.paste = response.data
      })
      .catch(e => console.log(e))
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#paste-content-flex-container {
  .window-container-style();

  width: 850px;
  margin: auto;
  margin-top: 100px;
}

#paste-content-form {
  width: 100%;
  display: flex;
  flex-direction: column;
}

#paste-content-form-title {
  .text-input-style();

  height: 25px;
  margin: 5px 0;
}

#paste-content-form-text {
  .text-input-style();

  height: 300px;
  margin: 5px 0;
}
</style>
