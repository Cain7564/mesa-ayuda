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

      <input
        type="number"
        v-model="form.usuario"
      />

    </div>

    <div class="field">

      <label>Técnico</label>

      <input
        type="number"
        v-model="form.tecnico"
      />

    </div>

    <div class="field">

      <label>Categoría</label>

      <input
        type="number"
        v-model="form.categoria"
      />

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