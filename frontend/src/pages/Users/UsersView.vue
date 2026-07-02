<template>
  <div class="users-page">

    <div class="header">

      <h1>Usuarios</h1>

      <button @click="cargarUsuarios">

        Actualizar

      </button>

    </div>

    <DataTable
      :columns="columns"
      :rows="usuarios.results"
    />

  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'

import DataTable from '../../components/DataTable.vue'

import { getUsers } from '../../services/users'

const usuarios = ref({
  results: []
})

const columns = [

  {
    key: 'id',
    label: 'ID'
  },

  {
    key: 'nombre',
    label: 'Nombre'
  },

  {
    key: 'correo',
    label: 'Correo'
  },

  {
    key: 'rol',
    label: 'Rol'
  }

]

const cargarUsuarios = async () => {

  try {

    usuarios.value = await getUsers()

  } catch (error) {

    console.error(error)

  }

}

onMounted(() => {

  cargarUsuarios()

})

</script>

<style scoped>

.users-page{

    padding:20px;

}

.header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:20px;

}

button{

    background:#1976d2;

    color:white;

    border:none;

    padding:10px 20px;

    border-radius:5px;

    cursor:pointer;

}

button:hover{

    background:#1565c0;

}

</style>