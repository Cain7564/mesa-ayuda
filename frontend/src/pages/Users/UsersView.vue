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
          @click="abrirNuevoUsuario"
        >
          Nuevo Usuario
        </PrimaryButton>

      </div>

    </PageHeader>

    <DataTable
      :columns="columns"
      :rows="usuariosFiltrados"
      :showActions="true"
    >

      <template #actions="{ row }">

        <div class="buttons">

          <PrimaryButton
            @click="editarUsuario(row)"
          >
            Editar
          </PrimaryButton>

          <button
            class="delete-button"
            @click="eliminarUsuario(row.id)"
          >
            Eliminar
          </button>

        </div>

      </template>

    </DataTable>

    <UserModal

      :visible="modalVisible"

      :title="modalTitle"

      :buttonText="buttonText"

      :user="usuarioSeleccionado"

      @close="cerrarModal"

      @save="guardarUsuario"

    />

  </div>
</template>

<script setup>

import { ref, computed, onMounted } from 'vue'

import PageHeader from '../../components/PageHeader.vue'
import InputField from '../../components/InputField.vue'
import PrimaryButton from '../../components/PrimaryButton.vue'
import DataTable from '../../components/DataTable.vue'

import UserModal from './components/UserModal.vue'

import {

  getUsers,

  createUser,

  updateUser,

  deleteUser

} from '../../services/users'

const usuarios = ref({

  results: []

})

const busqueda = ref('')

const modalVisible = ref(false)

const modalTitle = ref('Nuevo Usuario')

const buttonText = ref('Guardar')

const usuarioSeleccionado = ref(null)

const columns = [

  {
    key:'id',
    label:'ID'
  },

  {
    key:'nombre',
    label:'Nombre'
  },

  {
    key:'correo',
    label:'Correo'
  },

  {
    key:'rol',
    label:'Rol'
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

  usuarios.value = await getUsers()

}

const abrirNuevoUsuario = () => {

  usuarioSeleccionado.value = null

  modalTitle.value = 'Nuevo Usuario'

  buttonText.value = 'Guardar'

  modalVisible.value = true

}

const editarUsuario = (usuario) => {

  usuarioSeleccionado.value = usuario

  modalTitle.value = 'Editar Usuario'

  buttonText.value = 'Actualizar'

  modalVisible.value = true

}

const cerrarModal = () => {

  modalVisible.value = false

}

const guardarUsuario = async (datos) => {

  try{

    if(usuarioSeleccionado.value){

      await updateUser(

        usuarioSeleccionado.value.id,

        datos

      )

    }

    else{

      await createUser(datos)

    }

    cerrarModal()

    await cargarUsuarios()

  }

  catch(error){

    console.error(error)

  }

}

const eliminarUsuario = async (id) => {

  if(

    !confirm(

      '¿Desea eliminar este usuario?'

    )

  ){

    return

  }

  try{

    await deleteUser(id)

    await cargarUsuarios()

  }

  catch(error){

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

.actions{

    display:flex;

    gap:20px;

    align-items:end;

}

.buttons{

    display:flex;

    gap:10px;

}

.delete-button{

    background:#dc3545;

    color:white;

    border:none;

    padding:10px 15px;

    border-radius:6px;

    cursor:pointer;

}

.delete-button:hover{

    background:#bb2d3b;

}

</style>