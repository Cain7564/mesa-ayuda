<template>
  <form class="user-form" @submit.prevent="submitForm">

    <div class="row">
      <InputField
        label="Nombre"
        placeholder="Ingrese el nombre"
        v-model="form.nombre"
      />
    </div>

    <div class="row">
      <InputField
        label="Correo"
        placeholder="Ingrese el correo"
        type="email"
        v-model="form.correo"
      />
    </div>

    <div class="row">
      <InputField
        label="Contraseña"
        placeholder="Ingrese la contraseña"
        type="password"
        v-model="form.password"
      />
    </div>

    <div class="row">

      <label>Rol</label>

      <select v-model="form.rol">

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

  user: {
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

  nombre: '',

  correo: '',

  password: '',

  rol: 'USUARIO'

})

watch(

  () => props.user,

  (newUser) => {

    if (newUser) {

      form.nombre = newUser.nombre
      form.correo = newUser.correo
      form.password = ''
      form.rol = newUser.rol

    } else {

      form.nombre = ''
      form.correo = ''
      form.password = ''
      form.rol = 'USUARIO'

    }

  },

  {

    immediate: true

  }

)

const submitForm = () => {

  emit('save', {

    nombre: form.nombre,

    correo: form.correo,

    password: form.password,

    rol: form.rol

  })

}

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