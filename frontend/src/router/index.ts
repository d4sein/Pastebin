import Vue from 'vue'
import VueRouter from 'vue-router'
import Paste from '../views/Paste.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Dashboard from '../views/Dashboard.vue'
import PasteContent from '../views/PasteContent.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/paste',
    alias: '/',
    name: 'paste',
    component: Paste
  },
  {
    path: '/paste/:address',
    name: 'pasteContent',
    component: PasteContent
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
