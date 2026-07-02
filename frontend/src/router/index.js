import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../pages/Login/LoginView.vue'
import DashboardView from '../pages/Dashboard/DashboardView.vue'
const routes = [

  {
    path:'/',
    redirect:'/login'
  },

  {
    path:'/login',
    name:'login',
    component:LoginView
  },

  {
    path:'/dashboard',
    name:'dashboard',
    component:DashboardView
  }

]

const router = createRouter({

  history: createWebHistory(),

  routes,

})

export default router