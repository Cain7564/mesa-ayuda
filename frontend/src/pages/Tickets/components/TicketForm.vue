<template>

  <form class="ticket-form" @submit.prevent="submitForm">

    <InputField
      label="Asunto"
      placeholder="Ingrese el asunto"
      v-model="form.asunto"
    />

    <div class="field">

      <label>Descripción</label>

      <textarea
        v-model="form.descripcion"
        rows="4"
      ></textarea>

    </div>

    <div class="field">

      <label>Prioridad</label>

      <select v-model="form.prioridad">

        <option value="Alta">Alta</option>
        <option value="Media">Media</option>
        <option value="Baja">Baja</option>

      </select>

    </div>

    <div class="field">

      <label>Estado</label>

      <select v-model="form.estado">

        <option value="Abierto">Abierto</option>
        <option value="En proceso">En proceso</option>
        <option value="Cerrado">Cerrado</option>

      </select>

    </div>

    <div class="field">

      <label>Usuario</label>

      <select
        v-model="form.usuario"
      >

        <option
          value=""
        >

          Seleccione...

        </option>

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

      <label>Técnico</label>

      <select
        v-model="form.tecnico"
      >

        <option
          value=""
        >

          Seleccione...

        </option>

        <option

          v-for="tecnico in tecnicos"

          :key="tecnico.id"

          :value="tecnico.id"

        >

          {{ tecnico.nombre }}

        </option>

      </select>

    </div>

    <div class="field">

      <label>Categoría</label>

      <select
        v-model="form.categoria"
      >

        <option
          value=""
        >

          Seleccione...

        </option>

        <option

          v-for="categoria in categorias"

          :key="categoria.id"

          :value="categoria.id"

        >

          {{ categoria.nombre }}

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

import { reactive, watch } from 'vue'

import InputField from '../../../components/InputField.vue'
import PrimaryButton from '../../../components/PrimaryButton.vue'
import {

    getUsuariosSimple,

    getTecnicosSimple

} from '../../../services/users'

import {

    getCategoriasSimple

} from '../../../services/tickets'

import {

    onMounted,

    ref

} from 'vue'

const usuarios = ref([])

const tecnicos = ref([])

const categorias = ref([])

const props = defineProps({

  ticket: {

    type: Object,

    default: null

  },

  buttonText: {

    type: String,

    default: 'Guardar'

  }

})

const emit = defineEmits(['save'])

const form = reactive({

  asunto: '',

  descripcion: '',

  prioridad: 'Media',

  estado: 'Abierto',

  usuario: '',

  tecnico: '',

  categoria: ''

})

watch(

  () => props.ticket,

  (nuevo) => {

    if (nuevo) {

      form.asunto = nuevo.asunto
      form.descripcion = nuevo.descripcion
      form.prioridad = nuevo.prioridad
      form.estado = nuevo.estado
      form.usuario = nuevo.usuario
      form.tecnico = nuevo.tecnico
      form.categoria = nuevo.categoria

    } else {

      form.asunto = ''
      form.descripcion = ''
      form.prioridad = 'Media'
      form.estado = 'Abierto'
      form.usuario = ''
      form.tecnico = ''
      form.categoria = ''

    }

  },

  {

    immediate: true

  }

)

const submitForm = () => {

  emit('save', {

    ...form

  })

}

onMounted(async () => {

    usuarios.value = await getUsuariosSimple()

    tecnicos.value = await getTecnicosSimple()

    categorias.value = await getCategoriasSimple()

})

</script>

<style scoped>

.ticket-form{

    display:flex;

    flex-direction:column;

    gap:18px;

}

.field{

    display:flex;

    flex-direction:column;

}

label{

    font-weight:bold;

    margin-bottom:5px;

}

textarea{

    padding:10px;

    border:1px solid #ccc;

    border-radius:6px;

    resize:vertical;

}

select{

    padding:10px;

    border:1px solid #ccc;

    border-radius:6px;

}

.buttons{

    display:flex;

    justify-content:flex-end;

}

</style>