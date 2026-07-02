<template>

  <div>

    <h1>Usuarios</h1>

    <button @click="cargarUsuarios">

      Actualizar

    </button>

    <table>

      <thead>

        <tr>

          <th>ID</th>

          <th>Nombre</th>

          <th>Correo</th>

          <th>Rol</th>

        </tr>

      </thead>

      <tbody>

        <tr
          v-for="usuario in usuarios.results"
          :key="usuario.id"
        >

          <td>{{ usuario.id }}</td>

          <td>{{ usuario.nombre }}</td>

          <td>{{ usuario.correo }}</td>

          <td>{{ usuario.rol }}</td>

        </tr>

      </tbody>

    </table>

  </div>

</template>

<script setup>

import { ref, onMounted } from 'vue'

import { getUsers } from '../../services/users'

const usuarios = ref({

    results: []

})

const cargarUsuarios = async () => {

    usuarios.value = await getUsers()

}

onMounted(() => {

    cargarUsuarios()

})

</script>

<style scoped>

table{

    width:100%;

    border-collapse:collapse;

    margin-top:20px;

}

th{

    background:#1976d2;

    color:white;

    padding:10px;

}

td{

    padding:10px;

    border-bottom:1px solid #ddd;

}

button{

    padding:10px 20px;

    margin-top:20px;

}

</style>