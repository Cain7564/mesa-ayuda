<template>

  <form class="equipo-form" @submit.prevent="submitForm">
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
      

<div class="field">

  <label>Memoria RAM</label>

  <div class="inline-field">

    <input
      type="number"
      min="1"
      v-model="form.memoria_ram"
      placeholder="16"
    />

    <span>GB</span>

  </div>

</div>

<div class="field">

  <label>Disco</label>

  <div class="disk-container">

    <input
      type="number"
      min="1"
      v-model="capacidadDisco"
      placeholder="512"
    />

    <select v-model="unidadDisco">

      <option value="GB">
        GB
      </option>

      <option value="TB">
        TB
      </option>

    </select>

    <select v-model="tipoDisco">

      <option value="SSD">
        SSD
      </option>

      <option value="HDD">
        HDD
      </option>

    </select>

  </div>

</div>

    <InputField
      label="Dirección IP"
      placeholder="192.168.1.100"
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


const capacidadDisco = ref('')

const unidadDisco = ref('GB')

const tipoDisco = ref('SSD')

const marcas = ref([])

const sistemas = ref([])

const usuarios = ref([])

const estados = ref([])

const ubicaciones = ref([])


watch(

    () => props.equipo,

    (nuevo) => {

        if (nuevo) {

            form.tipo = nuevo.tipo

            form.marca = nuevo.marca

            form.modelo = nuevo.modelo

            form.numero_serie = nuevo.numero_serie

            form.procesador = nuevo.procesador

            form.memoria_ram = nuevo.memoria_ram
                ? nuevo.memoria_ram.replace(' GB', '')
                : ''

            form.disco = nuevo.disco

            form.sistema_operativo = nuevo.sistema_operativo

            form.direccion_ip = nuevo.direccion_ip

            form.direccion_mac = nuevo.direccion_mac

            form.usuario_asignado = nuevo.usuario_asignado

            form.estado = nuevo.estado

            form.ubicacion = nuevo.ubicacion

            if (nuevo.disco) {

                const partes = nuevo.disco.split(' ')

                capacidadDisco.value = partes[0] || ''

                unidadDisco.value = partes[1] || 'GB'

                tipoDisco.value = partes[2] || 'SSD'

            }

        } else {

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

            capacidadDisco.value = ''

            unidadDisco.value = 'GB'

            tipoDisco.value = 'SSD'

        }

    },

    {

        immediate: true

    }

)

const submitForm = () => {

    emit('save', {

        ...form,

        memoria_ram: `${form.memoria_ram} GB`,

        disco: `${capacidadDisco.value} ${unidadDisco.value} ${tipoDisco.value}`

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

    } catch (error) {

        console.error('Error cargando catálogos:', error)

    }

})

</script>

<style scoped>

.equipo-form{

    display:grid;

    grid-template-columns:1fr 1fr;

    gap:20px;

}

.field{

    display:flex;

    flex-direction:column;

}

label{

    font-weight:600;

    margin-bottom:6px;

    color:#333;

}

input,
select,
textarea{

    width:100%;

    padding:10px 12px;

    border:1px solid #d1d5db;

    border-radius:8px;

    font-size:14px;

    box-sizing:border-box;

    transition:.2s;

}

input:focus,
select:focus,
textarea:focus{

    outline:none;

    border-color:#1976d2;

    box-shadow:0 0 0 3px rgba(25,118,210,.15);

}

.inline-field{

    display:flex;

    align-items:center;

    gap:10px;

}

.inline-field input{

    flex:1;

}

.inline-field span{

    font-weight:bold;

    color:#555;

    min-width:30px;

}

.disk-container{

    display:flex;

    gap:10px;

    align-items:center;

}

.disk-container input{

    flex:1;

}

.disk-container select{

    width:90px;

}

.buttons{

    grid-column:1 / 3;

    display:flex;

    justify-content:flex-end;

    gap:10px;

    margin-top:10px;

}


.full-width{

    grid-column:1 / 3;

}


@media(max-width:900px){

    .equipo-form{

        grid-template-columns:1fr;

    }

    .buttons{

        grid-column:1;

    }

}

</style>