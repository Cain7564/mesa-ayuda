<template>

  <button
    class="btn"
    :type="type"
    @click="$emit('click')"
  >

    <slot />

  </button>

</template>

<script setup>

defineProps({

  type:{

    type:String,

    default:'button'

  }

})

defineEmits(['click'])

</script>

<style scoped>

.btn{

    background:#1976d2;

    color:white;

    border:none;

    padding:10px 20px;

    border-radius:6px;

    cursor:pointer;

    transition:.3s;

    font-size:15px;

}

.btn:hover{

    background:#1565c0;

}

</style>