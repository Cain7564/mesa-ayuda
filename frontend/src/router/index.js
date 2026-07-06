import { createRouter, createWebHistory } from 'vue-router'

import LoginView from '../pages/Login/LoginView.vue'
import DashboardView from '../pages/Dashboard/DashboardView.vue'
import UsersView from '../pages/Users/UsersView.vue'
import TicketsView from '../pages/Tickets/TicketsView.vue'
import InventoryView from '../pages/Inventory/InventoryView.vue'
import ReportsView from '../pages/Reports/ReportsView.vue'
import TecnicosView from '../pages/Tecnicos/TecnicosView.vue'

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
      },

      {
        path: 'users',
        name: 'users',
        component: UsersView
      },

      {
        path: 'tickets',
        name: 'tickets',
        component: TicketsView
      },

      {
        path: 'inventory',
        name: 'inventory',
        component: InventoryView
      },

      {
        path: 'reports',
        name: 'reports',
        component: ReportsView
      },

      {
        path: 'tecnicos',
        name: 'tecnicos',
        component: TecnicosView
        
      },
    ]

  }

]

const router = createRouter({

  history: createWebHistory(),

  routes,

})

export default router