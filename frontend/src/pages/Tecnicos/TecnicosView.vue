<template>

  <div class="tecnicos-page">

    <PageHeader title="Técnicos">

      <div class="actions">

        <InputField
          v-model="busqueda"
          label="Buscar"
          placeholder="Buscar técnico..."
        />

        <PrimaryButton
          @click="abrirNuevoTecnico"
        >
          Nuevo Técnico
        </PrimaryButton>

      </div>

    </PageHeader>

    <DataTable
      :columns="columns"
      :rows="tecnicos.results"
      :showActions="true"
    >

      <template #actions="{ row }">

        <div class="buttons">

          <PrimaryButton
            @click="editarTecnico(row)"
          >
            Editar
          </PrimaryButton>

          <button
            class="delete-button"
            @click="eliminarTecnico(row.id)"
          >
            Eliminar
          </button>

        </div>

      </template>

    </DataTable>

    <Pagination
      :previous="tecnicos.previous"
      :next="tecnicos.next"
      :currentPage="currentPage"
      @previous="paginaAnterior"
      @next="siguientePagina"
    />

    <TecnicoModal
      :visible="modalVisible"
      :title="modalTitle"
      :buttonText="buttonText"
      :tecnico="tecnicoSeleccionado"
      @close="cerrarModal"
      @save="guardarTecnico"
    />

  </div>

</template>

<script setup>

import { ref, watch, onMounted } from 'vue'

import PageHeader from '../../components/PageHeader.vue'
import InputField from '../../components/InputField.vue'
import PrimaryButton from '../../components/PrimaryButton.vue'
import DataTable from '../../components/DataTable.vue'
import Pagination from '../../components/Pagination.vue'

import TecnicoModal from './components/TecnicoModal.vue'

import {
  getTecnicos,
  createTecnico,
  updateTecnico,
  deleteTecnico
} from '../../services/tecnicos'

const tecnicos = ref({
  count: 0,
  next: null,
  previous: null,
  results: []
})

const currentPage = ref(1)

const busqueda = ref('')

const modalVisible = ref(false)

const modalTitle = ref('Nuevo Técnico')

const buttonText = ref('Guardar')

const tecnicoSeleccionado = ref(null)

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
    key:'especialidad',
    label:'Especialidad'
  }

]

const cargarTecnicos = async () => {

    try {

        tecnicos.value = await getTecnicos(

            currentPage.value,

            busqueda.value,

            ''

        )

    }

    catch(error){

        console.error(error)

    }

}

const abrirNuevoTecnico = () => {

    tecnicoSeleccionado.value = null

    modalTitle.value = 'Nuevo Técnico'

    buttonText.value = 'Guardar'

    modalVisible.value = true

}

const editarTecnico = (tecnico) => {

    tecnicoSeleccionado.value = tecnico

    modalTitle.value = 'Editar Técnico'

    buttonText.value = 'Actualizar'

    modalVisible.value = true

}

const cerrarModal = () => {

    modalVisible.value = false

}

const guardarTecnico = async (datos) => {

    console.log("===== DATOS TECNICO =====")
    console.log(datos)

    try {

        if (tecnicoSeleccionado.value) {

            await updateTecnico(
                tecnicoSeleccionado.value.id,
                datos
            )

            alert("Técnico actualizado correctamente.")

        } else {

            await createTecnico(datos)

            alert("Técnico creado correctamente.")

        }

        cerrarModal()

        await cargarTecnicos()

    }

    catch(error){

        console.log("===== ERROR =====")

        console.log(error.response)

        if(error.response){

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

const eliminarTecnico = async (id) => {

    if(!confirm("¿Desea eliminar este técnico?")){

        return

    }

    try{

        await deleteTecnico(id)

        await cargarTecnicos()

    }

    catch(error){

        console.error(error)

    }

}

const siguientePagina = async () => {

    if(!tecnicos.value.next){

        return

    }

    currentPage.value++

    await cargarTecnicos()

}

const paginaAnterior = async () => {

    if(!tecnicos.value.previous){

        return

    }

    currentPage.value--

    await cargarTecnicos()

}

watch(busqueda, async ()=>{

    currentPage.value = 1

    await cargarTecnicos()

})

onMounted(()=>{

    cargarTecnicos()

})

</script>

<style scoped>

.tecnicos-page{

    padding:20px;

}

.actions{

    display:flex;

    gap:20px;

    align-items:flex-end;

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