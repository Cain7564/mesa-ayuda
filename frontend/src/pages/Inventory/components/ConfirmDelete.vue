<template>

  <div
    v-if="visible"
    class="overlay"
  >

    <div class="dialog">

      <h2>{{ title }}</h2>

      <p>

        {{ message }}

      </p>

      <div class="buttons">

        <button
          class="cancel"
          @click="$emit('cancel')"
        >
          Cancelar
        </button>

        <button
          class="delete"
          @click="$emit('confirm')"
        >
          Eliminar
        </button>

      </div>

    </div>

  </div>

</template>

<script setup>

defineProps({

    visible: {
        type: Boolean,
        default: false
    },

    title: {
        type: String,
        default: 'Eliminar registro'
    },

    message: {
        type: String,
        default: '¿Está seguro que desea eliminar este registro?'
    }

})

defineEmits([

    'cancel',

    'confirm'

])

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

.dialog{

    width:420px;

    background:white;

    border-radius:10px;

    padding:30px;

    box-shadow:0 15px 40px rgba(0,0,0,.25);

}

h2{

    margin-top:0;

    margin-bottom:15px;

}

p{

    color:#555;

    margin-bottom:25px;

}

.buttons{

    display:flex;

    justify-content:flex-end;

    gap:10px;

}

.cancel{

    background:#6c757d;

    color:white;

    border:none;

    padding:10px 20px;

    border-radius:6px;

    cursor:pointer;

}

.cancel:hover{

    background:#5a6268;

}

.delete{

    background:#dc3545;

    color:white;

    border:none;

    padding:10px 20px;

    border-radius:6px;

    cursor:pointer;

}

.delete:hover{

    background:#bb2d3b;

}

</style>