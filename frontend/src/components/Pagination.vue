<template>

  <div class="pagination">

    <button
      @click="$emit('previous')"
      :disabled="!previous"
    >
      ⬅ Anterior
    </button>

    <span>

      Página {{ currentPage }}

    </span>

    <button
      @click="$emit('next')"
      :disabled="!next"
    >
      Siguiente ➡

    </button>

  </div>

</template>

<script setup>

defineProps({

    previous: String,

    next: String,

    currentPage: Number

})

defineEmits([

    'previous',

    'next'

])

</script>

<style scoped>

.pagination{

    margin-top:20px;

    display:flex;

    justify-content:center;

    align-items:center;

    gap:20px;

}

button{

    padding:10px 20px;

    background:#1976d2;

    color:white;

    border:none;

    border-radius:6px;

    cursor:pointer;

}

button:disabled{

    background:#bdbdbd;

    cursor:not-allowed;

}

</style>