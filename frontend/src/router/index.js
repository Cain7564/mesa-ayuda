import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../pages/Login/LoginView.vue'
import DashboardView from '../pages/Dashboard/DashboardView.vue'
import MainLayout from '../layouts/MainLayout.vue'

const routes = [

  {
    path: '/login',
    name: 'login',
    component: LoginView
  },

  {
    path: '/',
    component: MainLayout,

    children: [

      {
        path: '',
        redirect: '/dashboard'
      },

      {
        path: 'dashboard',
        name: 'dashboard',
        component: DashboardView
      }

    ]

  }

]

const router = createRouter({

  history: createWebHistory(),

  routes,

})

export default router