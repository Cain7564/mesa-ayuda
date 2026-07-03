<template>

  <div class="users-page">

<PageHeader title="Usuarios">

  <div class="actions">

    <InputField
      v-model="busqueda"
      label="Buscar"
      placeholder="Buscar usuario..."
    />

    <div class="filter">

      <label>Rol</label>

      <select
        v-model="rolSeleccionado"
        @change="cargarUsuarios"
      >

        <option value="">

          Todos

        </option>

        <option value="ADMIN">

          Administrador

        </option>

        <option value="TECNICO">

          Técnico

        </option>

        <option value="USUARIO">

          Usuario

        </option>

      </select>

    </div>

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

    <Pagination
      :previous="usuarios.previous"
      :next="usuarios.next"
      :currentPage="currentPage"
      @previous="paginaAnterior"
      @next="siguientePagina"
    />

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

import { ref, computed, onMounted, watch } from 'vue'
import PageHeader from '../../components/PageHeader.vue'
import InputField from '../../components/InputField.vue'
import PrimaryButton from '../../components/PrimaryButton.vue'
import DataTable from '../../components/DataTable.vue'
import Pagination from '../../components/Pagination.vue'

import UserModal from './components/UserModal.vue'

import {

  getUsers,

  createUser,

  updateUser,

  deleteUser

} from '../../services/users'

const usuarios = ref({

  count: 0,

  next: null,

  previous: null,

  results: []

})

const busqueda = ref('')

const rolSeleccionado = ref('')

const modalVisible = ref(false)

const modalTitle = ref('Nuevo Usuario')

const buttonText = ref('Guardar')

const usuarioSeleccionado = ref(null)
const currentPage = ref(1)

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

        usuarios.value = await getUsers(

            currentPage.value,

            rolSeleccionado.value,
            busqueda.value

        )

    }

    catch(error){

        console.error(error)

    }

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

    console.log("===== DATOS ENVIADOS =====")
    console.log(datos)

    try {

        const datosEnviar = { ...datos }


        if (
            usuarioSeleccionado.value &&
            (!datosEnviar.password || datosEnviar.password.trim() === '')
        ) {

            delete datosEnviar.password

        }

        if (usuarioSeleccionado.value) {

            await updateUser(
                usuarioSeleccionado.value.id,
                datosEnviar
            )

            alert("Usuario actualizado correctamente.")

        } else {

            await createUser(datosEnviar)

            alert("Usuario creado correctamente.")

        }

        cerrarModal()

        await cargarUsuarios()

    } catch (error) {

        console.log("===== ERROR =====")

        console.log(error)

        if (error.response) {

            console.log(error.response.data)

            alert(
                JSON.stringify(
                    error.response.data,
                    null,
                    2
                )
            )

        }

    }

}

const siguientePagina = async () => {

    if (!usuarios.value.next) {

        return

    }

    currentPage.value++

    await cargarUsuarios()

}

const paginaAnterior = async () => {

    if (!usuarios.value.previous) {

        return

    }

    currentPage.value--

    await cargarUsuarios()

}

const eliminarUsuario = async (id) => {

  if (!confirm("¿Desea eliminar este usuario?")) {

    return

  }

  try {

    await deleteUser(id)

    await cargarUsuarios()

  }

  catch (error) {

    console.error(error)

  }

}

watch(busqueda, async () => {

  currentPage.value = 1

  await cargarUsuarios()

})

watch(rolSeleccionado, async () => {

  currentPage.value = 1

  await cargarUsuarios()

})

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

    align-items:flex-end;

    gap:20px;

    flex-wrap:wrap;

}

.filter{

    display:flex;

    flex-direction:column;

}

.filter select{

    padding:10px;

    border:1px solid #ccc;

    border-radius:6px;

    min-width:170px;

    font-size:14px;

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

    transition:.2s;

}

.delete-button:hover{

    background:#bb2d3b;

}

</style>