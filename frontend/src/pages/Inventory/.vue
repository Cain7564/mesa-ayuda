<template>

  <div class="inventory-page">

    <PageHeader title="Inventario">

      <div class="actions">

        <InputField
          v-model="busqueda"
          label="Buscar"
          placeholder="Buscar equipo..."
        />

        <div class="filter">

          <label>Tipo</label>

          <select
            v-model="tipoSeleccionado"
          >

            <option value="">
              Todos
            </option>

            <option value="PC">
              PC
            </option>

            <option value="LAPTOP">
              Laptop
            </option>

            <option value="MONITOR">
              Monitor
            </option>

            <option value="IMPRESORA">
              Impresora
            </option>

          </select>

        </div>

        <div class="filter">

          <label>Estado</label>

          <select
            v-model="estadoSeleccionado"
          >

            <option value="">
              Todos
            </option>

            <option value="1">
              Activo
            </option>

            <option value="2">
              En reparación
            </option>

            <option value="3">
              Dado de baja
            </option>

            <option value="4">
              En mantenimiento
            </option>

          </select>

        </div>

        <div class="filter">

          <label>Ordenar</label>

          <select
            v-model="ordenSeleccionado"
          >

            <option value="">
              Sin ordenar
            </option>

            <option value="codigo">
              Código (A-Z)
            </option>

            <option value="-codigo">
              Código (Z-A)
            </option>

            <option value="modelo">
              Modelo
            </option>

            <option value="tipo">
              Tipo
            </option>

          </select>

        </div>

        <PrimaryButton
          @click="abrirNuevoEquipo"
        >
          Nuevo Equipo
        </PrimaryButton>

      </div>

    </PageHeader>

    <DataTable
      :columns="columns"
      :rows="equipos.results"
      :showActions="true"
    >

      <template #actions="{ row }">

        <div class="buttons">

          <PrimaryButton
            @click="editarEquipo(row)"
          >
            Editar
          </PrimaryButton>

          <button
            class="delete-button"
            @click="eliminarEquipo(row.id)"
          >
            Eliminar
          </button>

        </div>

      </template>

    </DataTable>

    <Pagination
      :previous="equipos.previous"
      :next="equipos.next"
      :currentPage="currentPage"
      @previous="paginaAnterior"
      @next="siguientePagina"
    />

    <EquipoModal

      :visible="modalVisible"

      :title="modalTitle"

      :buttonText="buttonText"

      :equipo="equipoSeleccionado"

      @close="cerrarModal"

      @save="guardarEquipo"

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
import EquipoModal from './components/EquipoModal.vue'

import {

  getEquipos,

  createEquipo,

  updateEquipo,

  deleteEquipo

} from '../../services/inventory'

const equipos = ref({

    count:0,

    next:null,

    previous:null,

    results:[]

})

const currentPage = ref(1)

const modalVisible = ref(false)

const modalTitle = ref('Nuevo Equipo')

const buttonText = ref('Guardar')

const equipoSeleccionado = ref(null)

const busqueda = ref('')

const tipoSeleccionado = ref('')

const estadoSeleccionado = ref('')

const ordenSeleccionado = ref('')

const columns = [

    {
        key:'codigo',
        label:'Código'
    },

    {
        key:'tipo',
        label:'Tipo'
    },

    {
        key:'marca_nombre',
        label:'Marca'
    },

    {
        key:'modelo',
        label:'Modelo'
    },

    {
        key:'usuario_nombre',
        label:'Usuario'
    },

    {
        key:'estado_nombre',
        label:'Estado'
    },

    {
        key:'ubicacion_nombre',
        label:'Ubicación'
    }

]

const cargarEquipos = async () => {

    try{

        equipos.value = await getEquipos(

            currentPage.value,

            tipoSeleccionado.value,

            estadoSeleccionado.value,

            busqueda.value,

            ordenSeleccionado.value

        )

    }

    catch(error){

        console.error(error)

    }

}

const abrirNuevoEquipo = () => {

    equipoSeleccionado.value = null

    modalTitle.value = 'Nuevo Equipo'

    buttonText.value = 'Guardar'

    modalVisible.value = true

}

const editarEquipo = (equipo) => {

    equipoSeleccionado.value = equipo

    modalTitle.value = 'Editar Equipo'

    buttonText.value = 'Actualizar'

    modalVisible.value = true

}

const cerrarModal = () => {

    modalVisible.value = false

}

const guardarEquipo = async (datos) => {

    try{

        if(equipoSeleccionado.value){

            await updateEquipo(

                equipoSeleccionado.value.id,

                datos

            )

            alert("Equipo actualizado correctamente.")

        }

        else{

            await createEquipo(datos)

            alert("Equipo creado correctamente.")

        }

        cerrarModal()

        await cargarEquipos()

    }

    catch(error){

        console.error(error)

        if(error.response){

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

const eliminarEquipo = async (id) => {

    if(!confirm("¿Desea eliminar este equipo?")){

        return

    }

    try{

        await deleteEquipo(id)

        await cargarEquipos()

    }

    catch(error){

        console.error(error)

    }

}

const siguientePagina = async () => {

    if(!equipos.value.next){

        return

    }

    currentPage.value++

    await cargarEquipos()

}

const paginaAnterior = async () => {

    if(!equipos.value.previous){

        return

    }

    currentPage.value--

    await cargarEquipos()

}

watch(busqueda, async()=>{

    currentPage.value = 1

    await cargarEquipos()

})

watch(tipoSeleccionado, async()=>{

    currentPage.value = 1

    await cargarEquipos()

})

watch(estadoSeleccionado, async()=>{

    currentPage.value = 1

    await cargarEquipos()

})

watch(ordenSeleccionado, async()=>{

    currentPage.value = 1

    await cargarEquipos()

})

onMounted(()=>{

    cargarEquipos()

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