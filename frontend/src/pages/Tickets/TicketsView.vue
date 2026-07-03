<template>

  <div class="tickets-page">

    <PageHeader title="Tickets">

      <div class="actions">

        <InputField
          v-model="busqueda"
          label="Buscar"
          placeholder="Buscar ticket..."
        />

        <div class="filter">

          <label>Estado</label>

          <select
            v-model="estadoSeleccionado"
            @change="cargarTickets"
          >

            <option value="">
              Todos
            </option>

            <option value="Abierto">
              Abierto
            </option>

            <option value="En proceso">
              En proceso
            </option>

            <option value="Cerrado">
              Cerrado
            </option>

          </select>

        </div>

        <div class="filter">

          <label>Prioridad</label>

          <select
            v-model="prioridadSeleccionada"
            @change="cargarTickets"
          >

            <option value="">
              Todas
            </option>

            <option value="Baja">
              Baja
            </option>

            <option value="Media">
              Media
            </option>

            <option value="Alta">
              Alta
            </option>

          </select>

        </div>

        <div class="filter">

          <label>Ordenar</label>

          <select
            v-model="ordenSeleccionado"
            @change="cargarTickets"
          >

            <option value="">
              Sin ordenar
            </option>

            <option value="fecha">
              Fecha ↑
            </option>

            <option value="-fecha">
              Fecha ↓
            </option>

            <option value="prioridad">
              Prioridad
            </option>

            <option value="estado">
              Estado
            </option>

          </select>

        </div>

        <PrimaryButton
          @click="abrirNuevoTicket"
        >
          Nuevo Ticket
        </PrimaryButton>

      </div>

    </PageHeader>

    <DataTable
      :columns="columns"
      :rows="tickets.results"
    />

    <Pagination
      :previous="tickets.previous"
      :next="tickets.next"
      :currentPage="currentPage"
      @previous="paginaAnterior"
      @next="siguientePagina"
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

import { getTickets } from '../../services/tickets'

const tickets = ref({

    count:0,

    next:null,

    previous:null,

    results:[]

})

const currentPage = ref(1)

const busqueda = ref('')

const estadoSeleccionado = ref('')

const columns = [

    {
        key:'id',
        label:'ID'
    },

    {
        key:'asunto',
        label:'Asunto'
    },

    {
        key:'usuario_nombre',
        label:'Usuario'
    },

    {
        key:'tecnico_nombre',
        label:'Técnico'
    },

    {
        key:'estado',
        label:'Estado'
    },

    {
        key:'prioridad',
        label:'Prioridad'
    },

    {
        key:'fecha',
        label:'Fecha'
    }

]

const cargarTickets = async () => {

    try{

        tickets.value = await getTickets(

            currentPage.value,

            estadoSeleccionado.value,

            '',

            busqueda.value

        )

    }

    catch(error){

        console.error(error)

    }

}

const abrirNuevoTicket = () => {

    alert('Aquí irá el formulario del ticket.')

}

const siguientePagina = async () => {

    if(!tickets.value.next){

        return

    }

    currentPage.value++

    await cargarTickets()

}

const paginaAnterior = async () => {

    if(!tickets.value.previous){

        return

    }

    currentPage.value--

    await cargarTickets()

}

watch(busqueda, async ()=>{

    currentPage.value=1

    await cargarTickets()

})

watch(estadoSeleccionado, async ()=>{

    currentPage.value=1

    await cargarTickets()

})

onMounted(()=>{

    cargarTickets()

})

</script>

<style scoped>

.tickets-page{

    padding:20px;

}

.actions{

    display:flex;

    gap:20px;

    align-items:flex-end;

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

}

</style>