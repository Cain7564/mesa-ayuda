<template>
  <div class="layout">

    <aside class="sidebar">

      <h2>Mesa de Ayuda</h2>

      <ul>

        <li>
          <RouterLink to="/dashboard">
            Dashboard
          </RouterLink>
        </li>

        <li>
          <RouterLink to="/users">
            Usuarios
          </RouterLink>
        </li>

        <li>
          <RouterLink to="/tecnicos">
            Técnicos
          </RouterLink>
        </li>
        
        <li>
          <RouterLink to="/tickets">
            Tickets
          </RouterLink>
        </li>

        <li>
          <RouterLink to="/inventory">
            Inventario
          </RouterLink>
        </li>

        <li>
          <RouterLink to="/reports">
            Reportes
          </RouterLink>
        </li>

        <li>
          <RouterLink to="/login">
            Cerrar sesión
          </RouterLink>
        </li>

      </ul>

    </aside>

    <main class="content">

      <RouterView />

    </main>

  </div>
</template>

<script setup>

import { RouterView, RouterLink } from 'vue-router'

</script>

<style scoped>

.layout {

    display: flex;

    height: 100vh;

}

.sidebar {

    width: 250px;

    background: #1f2937;

    color: white;

    padding: 20px;

}

.sidebar h2 {

    text-align: center;

    margin-bottom: 30px;

}

.sidebar ul {

    list-style: none;

    padding: 0;

}

.sidebar li {

    margin-bottom: 10px;

}

.sidebar a {

    display: block;

    color: white;

    text-decoration: none;

    padding: 15px;

    border-radius: 6px;

    transition: background 0.3s;

}

.sidebar a:hover {

    background: #374151;

}

.router-link-active {

    background: #2563eb;

    font-weight: bold;

}

.content {

    flex: 1;

    padding: 30px;

    background: #f4f6f9;

}

</style>