<template>
  <div id="dashboard-interface">
    <div id="dashboard-grid-container">
      <div id="dashboard-pastes-labels">
        <div class="dashboard-label"><h3>Title</h3></div>
        <div class="dashboard-label"><h3>Address</h3></div>
        <div class="dashboard-label"><h3>Created</h3></div>
        <div class="dashboard-label"><h3>Last Edited</h3></div>
      </div>
      <div class="dashboard-paste-container" v-for="paste in pastes.pastes" :key=paste.title>
        <div class="dashboard-paste-item"><h3>{{ paste.title }}</h3></div>
        <div class="dashboard-paste-item"><h3>{{ paste.address }}</h3></div>
        <div class="dashboard-paste-item"><h3>{{ paste.created }}</h3></div>
        <div class="dashboard-paste-item"><h3>{{ paste.last_edited }}</h3></div>
        <button>Edit</button>
        <button>Delete</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'dashboard-interface',
  data () {
    return {
      pastes: Object
    }
  },
  mounted () {
    this.axios
      .get('paste?username=d4sein')
      .then(response => (this.pastes = response.data))
      .catch(e => console.error(e))
  }
})
</script>

<style lang="less" scoped>
@import '../assets/static/config';

#dashboard-pastes-labels {
  display: grid;
  grid-template-columns: 10fr 3fr 3fr 3fr 2fr;
}

.dashboard-label {
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

  button {
    margin-right: 5px;
    background: none;
    border: none;
    font-size: 14px;
    color: @dark-gray;

    &:hover {
      color: @white;
    }
  }
}

.dashboard-paste-item {
  padding: 5px;
  h3 {
    color: @dark-gray;
    font-size: 16px;
    font-weight: 400;
  }
}
</style>
