<template>

  <form class="equipo-form" @submit.prevent="submitForm">

    <InputField
      label="Código"
      placeholder="Ingrese el código"
      v-model="form.codigo"
    />

    <div class="field">

      <label>Tipo</label>

      <select v-model="form.tipo">

        <option value="PC">PC</option>
        <option value="LAPTOP">Laptop</option>
        <option value="MONITOR">Monitor</option>
        <option value="IMPRESORA">Impresora</option>

      </select>

    </div>

    <InputField
      label="Modelo"
      placeholder="Ingrese el modelo"
      v-model="form.modelo"
    />

    <InputField
      label="Número de serie"
      placeholder="Ingrese el número de serie"
      v-model="form.numero_serie"
    />

    <InputField
      label="Procesador"
      placeholder="Ingrese el procesador"
      v-model="form.procesador"
    />

    <InputField
      label="Memoria RAM"
      placeholder="Ej: 16 GB"
      v-model="form.memoria_ram"
    />

    <InputField
      label="Disco"
      placeholder="Ej: 512 GB SSD"
      v-model="form.disco"
    />

    <InputField
      label="Dirección IP"
      placeholder="192.168.1.10"
      v-model="form.direccion_ip"
    />

    <InputField
      label="Dirección MAC"
      placeholder="AA:BB:CC:DD:EE:FF"
      v-model="form.direccion_mac"
    />

    <div class="field">

      <label>Marca</label>

      <select v-model="form.marca">

        <option
          v-for="marca in marcas"
          :key="marca.id"
          :value="marca.id"
        >
          {{ marca.nombre }}
        </option>

      </select>

    </div>

    <div class="field">

      <label>Sistema Operativo</label>

      <select v-model="form.sistema_operativo">

        <option
          v-for="so in sistemas"
          :key="so.id"
          :value="so.id"
        >
          {{ so.nombre }}
        </option>

      </select>

    </div>

    <div class="field">

      <label>Usuario asignado</label>

      <select v-model="form.usuario_asignado">

        <option
          v-for="usuario in usuarios"
          :key="usuario.id"
          :value="usuario.id"
        >
          {{ usuario.nombre }}
        </option>

      </select>

    </div>

    <div class="field">

      <label>Estado</label>

      <select v-model="form.estado">

        <option
          v-for="estado in estados"
          :key="estado.id"
          :value="estado.id"
        >
          {{ estado.nombre }}
        </option>

      </select>

    </div>

    <div class="field">

      <label>Ubicación</label>

      <select v-model="form.ubicacion">

        <option
          v-for="ubicacion in ubicaciones"
          :key="ubicacion.id"
          :value="ubicacion.id"
        >
          {{ ubicacion.nombre }}
        </option>

      </select>

    </div>

    <div class="buttons">

      <PrimaryButton type="submit">

        {{ buttonText }}

      </PrimaryButton>

    </div>

  </form>

</template>

<script setup>
import { reactive, watch, ref, onMounted } from 'vue'

import InputField from '../../../components/InputField.vue'
import PrimaryButton from '../../../components/PrimaryButton.vue'
import { getUsuariosSimple } from '../../../services/users'

import {

    getMarcas,

    getSistemasOperativos,

    getUbicaciones,

    getEstadosEquipo

} from '../../../services/inventory'



const props = defineProps({

  equipo: {

    type: Object,

    default: null

  },

  buttonText: {

    type: String,

    default: 'Guardar'

  }

})
const emit = defineEmits([

  'save'

])
const form = reactive({

  codigo: '',

  tipo: 'PC',

  marca: '',

  modelo: '',

  numero_serie: '',

  procesador: '',

  memoria_ram: '',

  disco: '',

  sistema_operativo: '',

  direccion_ip: '',

  direccion_mac: '',

  usuario_asignado: '',

  estado: '',

  ubicacion: ''

})

watch(

  () => props.equipo,

  (nuevo) => {

    if (nuevo) {

      form.codigo = nuevo.codigo

      form.tipo = nuevo.tipo

      form.marca = nuevo.marca

      form.modelo = nuevo.modelo

      form.numero_serie = nuevo.numero_serie

      form.procesador = nuevo.procesador

      form.memoria_ram = nuevo.memoria_ram

      form.disco = nuevo.disco

      form.sistema_operativo = nuevo.sistema_operativo

      form.direccion_ip = nuevo.direccion_ip

      form.direccion_mac = nuevo.direccion_mac

      form.usuario_asignado = nuevo.usuario_asignado

      form.estado = nuevo.estado

      form.ubicacion = nuevo.ubicacion

    }

    else {

      form.codigo = ''

      form.tipo = 'PC'

      form.marca = ''

      form.modelo = ''

      form.numero_serie = ''

      form.procesador = ''

      form.memoria_ram = ''

      form.disco = ''

      form.sistema_operativo = ''

      form.direccion_ip = ''

      form.direccion_mac = ''

      form.usuario_asignado = ''

      form.estado = ''

      form.ubicacion = ''

    }

  },

  {

    immediate: true

  }

)

const marcas = ref([])

const sistemas = ref([])

const usuarios = ref([])

const estados = ref([])

const ubicaciones = ref([])

const submitForm = () => {

    emit('save', {

        ...form

    })

}


onMounted(async () => {

    try {

        const respuestaUsuarios = await getUsuariosSimple()
        usuarios.value = respuestaUsuarios.results ?? respuestaUsuarios

        const respuestaMarcas = await getMarcas()
        marcas.value = respuestaMarcas.results ?? respuestaMarcas

        const respuestaSistemas = await getSistemasOperativos()
        sistemas.value = respuestaSistemas.results ?? respuestaSistemas

        const respuestaEstados = await getEstadosEquipo()
        estados.value = respuestaEstados.results ?? respuestaEstados

        const respuestaUbicaciones = await getUbicaciones()
        ubicaciones.value = respuestaUbicaciones.results ?? respuestaUbicaciones

        console.log("Usuarios:", usuarios.value)
        console.log("Marcas:", marcas.value)
        console.log("Sistemas:", sistemas.value)
        console.log("Estados:", estados.value)
        console.log("Ubicaciones:", ubicaciones.value)

    }

    catch (error) {

        console.error("Error cargando catálogos:", error)

    }

})

</script>

<style scoped>

.user-form{

    display:flex;

    flex-direction:column;

    gap:20px;

}

.row{

    display:flex;

    flex-direction:column;

}

label{

    font-weight:bold;

    margin-bottom:6px;

}

select{

    padding:10px;

    border-radius:6px;

    border:1px solid #ccc;

    font-size:15px;

}

.buttons{

    display:flex;

    justify-content:flex-end;

    margin-top:10px;

}

</style>