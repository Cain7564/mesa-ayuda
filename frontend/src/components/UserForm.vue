<template>

  <form @submit.prevent="guardar">

    <InputField
      label="Nombre"
      placeholder="Nombre"
      v-model="form.nombre"
    />

    <InputField
      label="Correo"
      placeholder="Correo"
      v-model="form.correo"
    />

    <InputField
      label="Contraseña"
      type="password"
      placeholder="Contraseña"
      v-model="form.password"
    />

    <div class="campo">

      <label>Rol</label>

      <select v-model="form.rol">

        <option>Administrador</option>

        <option>TECNICO</option>

        <option>USUARIO</option>

      </select>

    </div>

    <PrimaryButton type="submit">

      Guardar

    </PrimaryButton>

  </form>

</template>

<script setup>

import { reactive } from 'vue'

import InputField from './InputField.vue'
import PrimaryButton from './PrimaryButton.vue'

const emit = defineEmits([

    'guardar'

])

const form = reactive({

    nombre:'',

    correo:'',

    password:'',

    rol:'USUARIO'

})

const guardar = () => {

    emit(

        'guardar',

        {

            ...form

        }

    )

}

</script>

<style scoped>

form{

    display:flex;

    flex-direction:column;

    gap:20px;

}

.campo{

    display:flex;

    flex-direction:column;

}

select{

    padding:10px;

}

</style>