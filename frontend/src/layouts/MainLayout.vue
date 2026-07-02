<template>

  <div class="layout">

    <aside class="sidebar">

      <h2>Mesa de Ayuda</h2>

      <ul>

        <li>Dashboard</li>

        <li>Usuarios</li>

        <li>Tickets</li>

        <li>Inventario</li>

        <li>Reportes</li>

        <li>Cerrar sesión</li>

      </ul>

    </aside>

    <main class="content">

      <RouterView />

    </main>

  </div>

</template>

<script setup>

import { RouterView } from 'vue-router'

</script>

<style scoped>

.layout{

    display:flex;

    height:100vh;

}

.sidebar{

    width:250px;

    background:#1f2937;

    color:white;

    padding:20px;

}

.sidebar h2{

    text-align:center;

    margin-bottom:30px;

}

.sidebar ul{

    list-style:none;

    padding:0;

}

.sidebar li{

    padding:15px;

    cursor:pointer;

}

.sidebar li:hover{

    background:#374151;

}

.content{

    flex:1;

    padding:30px;

    background:#f4f6f9;

}

</style>