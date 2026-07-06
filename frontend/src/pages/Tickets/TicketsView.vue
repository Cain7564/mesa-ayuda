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
  :showActions="true"
>

  <template #actions="{ row }">

    <div class="buttons">

      <PrimaryButton
        @click="editarTicket(row)"
      >
        Editar
      </PrimaryButton>

      <button
        class="delete-button"
        @click="eliminarTicket(row.id)"
      >
        Eliminar
      </button>

    </div>

  </template>

</DataTable>

    <Pagination
      :previous="tickets.previous"
      :next="tickets.next"
      :currentPage="currentPage"
      @previous="paginaAnterior"
      @next="siguientePagina"
    />

    <TicketModal

    :visible="modalVisible"

    :title="modalTitle"

    :buttonText="buttonText"

    :ticket="ticketSeleccionado"

    @close="cerrarModal"

    @save="guardarTicket"

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
import TicketModal from './components/TicketModal.vue'

import { getTickets, createTicket, updateTicket, deleteTicket } from '../../services/tickets'

const tickets = ref({

    count:0,

    next:null,

    previous:null,

    results:[]

})

const currentPage = ref(1)

const modalVisible = ref(false)

const modalTitle = ref('Nuevo Ticket')

const buttonText = ref('Guardar')

const ticketSeleccionado = ref(null)

const busqueda = ref('')

const estadoSeleccionado = ref('')

const prioridadSeleccionada = ref('')

const ordenSeleccionado = ref('')

const columns = [

  {
    key: 'id',
    label: 'ID'
  },

  {
    key: 'asunto',
    label: 'Asunto'
  },

  {
    key: 'usuario_nombre',
    label: 'Usuario'
  },

  {
    key: 'tecnico_nombre',
    label: 'Técnico'
  },

  {
    key: 'categoria_nombre',
    label: 'Categoría'
  },

  {
    key: 'estado',
    label: 'Estado'
  },

  {
    key: 'prioridad',
    label: 'Prioridad'
  },

  {
    key: 'fecha',
    label: 'Fecha'
  }

]

const cargarTickets = async () => {

    try{

        tickets.value = await getTickets(

            currentPage.value,
            estadoSeleccionado.value,
            prioridadSeleccionada.value,
            busqueda.value,
            ordenSeleccionado.value

        )

    }

    catch(error){

        console.error(error)

    }

}

const abrirNuevoTicket = () => {

    ticketSeleccionado.value = null

    modalTitle.value = 'Nuevo Ticket'

    buttonText.value = 'Guardar'

    modalVisible.value = true

}

const editarTicket = (ticket) => {

    ticketSeleccionado.value = ticket

    modalTitle.value = 'Editar Ticket'

    buttonText.value = 'Actualizar'

    modalVisible.value = true

}

const cerrarModal = () => {

    modalVisible.value = false

}
const guardarTicket = async (datos) => {

    console.log("===== DATOS DEL TICKET =====")
    console.log(datos)

    try {

        const datosEnviar = {

            ...datos

        }

        if (ticketSeleccionado.value) {

            await updateTicket(

                ticketSeleccionado.value.id,

                datosEnviar

            )

            alert(" Ticket actualizado correctamente.")

        }

        else {

            const ticket = await createTicket(

                datosEnviar

            )

            alert(

                ` Ticket #${ticket.id} creado correctamente.`

            )

        }

        cerrarModal()

        await cargarTickets()

    }

    catch(error){

        console.log("===== ERROR =====")

        console.log(error)

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

        else{

            alert("No fue posible comunicarse con el servidor.")

        }

    }

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

watch(prioridadSeleccionada, async ()=>{

    currentPage.value=1

    await cargarTickets()

})

watch(ordenSeleccionado, async ()=>{

    currentPage.value=1

    await cargarTickets()

})

onMounted(()=>{

    cargarTickets()

})

const eliminarTicket = async (id) => {

    if(!confirm("¿Desea eliminar este ticket?")){

        return

    }

    try{

        await deleteTicket(id)

        await cargarTickets()

    }

    catch(error){

        console.error(error)

    }

}
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