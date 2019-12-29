<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="less">
@import 'assets/static/config';
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap&css');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Roboto', Arial, Helvetica, sans-serif;
  background: @saturated-blue;
}

a {
  text-decoration: none;
  color: @dark-blue;

  &:hover {
    color: @white;
  }
}

li {
  list-style-type: none;
}

button {
  cursor: pointer;
}
</style>
