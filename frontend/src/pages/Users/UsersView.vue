<template>
  <div class="users-page">

    <PageHeader title="Usuarios">

      <div class="actions">

        <InputField
          v-model="busqueda"
          label="Buscar"
          placeholder="Buscar usuario..."
        />

        <PrimaryButton
          @click="modalVisible = true"
        >
          Nuevo Usuario
        </PrimaryButton>

      </div>

    </PageHeader>

    <DataTable
      :columns="columns"
      :rows="usuariosFiltrados"
    />

    <UserModal
      :visible="modalVisible"
      title="Nuevo Usuario"
      @cerrar="modalVisible = false"
      @guardar="guardarUsuario"
    />

  </div>
</template>

<script setup>

import { ref, computed, onMounted } from 'vue'

import PageHeader from '../../components/PageHeader.vue'
import PrimaryButton from '../../components/PrimaryButton.vue'
import InputField from '../../components/InputField.vue'
import DataTable from '../../components/DataTable.vue'
import UserModal from '../../components/UserModal.vue'

import {
  getUsers,
  createUser
} from '../../services/users'

const usuarios = ref({
  results: []
})

const modalVisible = ref(false)

const busqueda = ref('')

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

const usuariosFiltrados = computed(() => {

  return usuarios.value.results.filter(usuario =>

    usuario.nombre
      .toLowerCase()
      .includes(busqueda.value.toLowerCase())

  )

})

const cargarUsuarios = async () => {

  try {

    usuarios.value = await getUsers()

  } catch (error) {

    console.error(error)

  }

}

const guardarUsuario = async (datos) => {

  try {

    await createUser(datos)

    modalVisible.value = false

    await cargarUsuarios()

  } catch (error) {

    console.error(error)

    alert('No se pudo crear el usuario.')

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

.actions{

    display:flex;

    gap:20px;

    align-items:end;

}

</style>