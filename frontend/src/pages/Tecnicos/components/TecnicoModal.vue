<template>

  <div
    v-if="visible"
    class="overlay"
  >

    <div class="modal">

      <div class="header">

        <h2>{{ title }}</h2>

      </div>

      <TecnicoForm
        :tecnico="tecnico"
        :buttonText="buttonText"
        @save="guardar"
      />

      <div class="footer">

        <PrimaryButton
          @click="$emit('close')"
        >
          Cancelar
        </PrimaryButton>

      </div>

    </div>

  </div>

</template>

<script setup>

import TecnicoForm from './TecnicoForm.vue'
import PrimaryButton from '../../../components/PrimaryButton.vue'

defineProps({

  visible: Boolean,

  title: String,

  buttonText: String,

  tecnico: Object

})

const emit = defineEmits([

  'close',

  'save'

])

const guardar = (datos) => {

  emit('save', datos)

}

</script>

<style scoped>

.overlay{

    position:fixed;

    inset:0;

    background:rgba(0,0,0,.45);

    display:flex;

    justify-content:center;

    align-items:center;

    z-index:1000;

}

.modal{

    width:600px;

    background:white;

    border-radius:10px;

    padding:30px;

    box-shadow:0 15px 40px rgba(0,0,0,.25);

}

.header{

    margin-bottom:20px;

}

.footer{

    display:flex;

    justify-content:flex-end;

    margin-top:20px;

}

</style>