<template>
  <div
    v-if="visible"
    class="overlay"
  >
    <div class="modal">

      <div class="header">

        <h2>{{ title }}</h2>

      </div>

      <UserForm
        :user="user"
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

import UserForm from './UserForm.vue'
import PrimaryButton from '../../../components/PrimaryButton.vue'

defineProps({

  visible: Boolean,

  title: String,

  buttonText: String,

  user: Object

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

    background:rgba(0,0,0,.5);

    display:flex;

    justify-content:center;

    align-items:center;

    z-index:999;

}

.modal{

    background:white;

    width:600px;

    border-radius:10px;

    padding:30px;

    box-shadow:0 15px 40px rgba(0,0,0,.3);

}

.header{

    margin-bottom:20px;

}

.footer{

    margin-top:20px;

    display:flex;

    justify-content:flex-end;

}

</style>