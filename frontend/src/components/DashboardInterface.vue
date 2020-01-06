<template>
  <div id="dashboard-interface">
    <div id="dashboard-grid-container">
      <div id="dashboard-paste-labels">
        <div><h3>Title</h3></div>
        <div><h3>Address</h3></div>
        <div><h3>Created</h3></div>
        <div><h3>Last Edited</h3></div>
      </div>
      <div class="dashboard-paste-container" v-for="paste in pastes.pastes" :key="paste.address">
        <div><h3>{{ paste.title }}</h3></div>
        <div><h3>{{ paste.address }}</h3></div>
        <div><h3>{{ paste.created }}</h3></div>
        <div><h3>{{ paste.last_edited }}</h3></div>
        <button @click="editPaste(paste)">Edit</button>
        <button @click="deletePaste(paste)">Delete</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import store from '../assets/static/vuex_config'

export default Vue.extend({
  name: 'dashboard-interface',
  methods: {
    editPaste: function (paste: any) {
      this.$router.push(`edit/${paste.address}`)
    },
    deletePaste: function (paste: any) {
      let token: any = {
        'x-access-token': store.getters.token
      }

      this.axios
        .delete(`paste?address=${paste.address}`, { headers: token })
        .then(response => {
          location.reload()
        })
        .catch(e => console.log(e))
    }
  },
  data () {
    return {
      pastes: {}
    }
  },
  beforeCreate () {
    if (store.getters.token === null) {
      this.$router.push('paste')
    }
  },
  mounted () {
    let token: any = {
      'x-access-token': store.getters.token
    }

    this.axios
      .get('session', { headers: token })
      .then(response => {
        let user = response.data

        this.axios
          .get(`paste?username=${user.username}`)
          .then(response => (this.pastes = response.data))
          .catch(e => console.error(e))
      })
      .catch(e => console.log(e))
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#dashboard-paste-labels {
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 3fr 2fr;

  div {
    margin-bottom: 30px;
    width: 100%;
    position: relative;

    h3 {
      margin-left: 5px;
      text-transform: uppercase;
      color: @dark-gray;
      font-size: 16px;
      font-weight: 500;
      position: absolute;
    }
  }
}

#dashboard-grid-container {
  width: 90%;
  margin: auto;
  margin-top: 100px;
  display: grid;
  grid-template-columns: 1fr;

  div {
    display: grid;
    grid-template-columns: 10fr 4fr 4fr 4fr 1fr 1fr;
  }
}

.dashboard-paste-container {
  &:nth-child(2n) {
    background: @light-blue;
  }

  div {
    padding: 5px;

    h3 {
      color: @dark-gray;
      font-size: 14px;
      font-weight: 300;
    }
  }

  button {
    margin-right: 5px;
    background: none;
    border: none;
    font-size: 14px;
    font-weight: 300;
    color: @dark-gray;

    &:hover {
      color: @white;
    }
  }
}
</style>
