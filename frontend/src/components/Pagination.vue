<template>
  <div
    v-if="showPagination"
    class="pagination"
  >
    <button
      class="btn"
      @click="$emit('previous')"
      :disabled="!previous"
    >
      ⬅ Anterior
    </button>

    <span class="page">

      Página {{ currentPage }}

    </span>

    <button
      class="btn"
      @click="$emit('next')"
      :disabled="!next"
    >
      Siguiente ➡
    </button>
  </div>
</template>

<script setup>

import { computed } from 'vue'

const props = defineProps({

  previous: {
    type: String,
    default: null
  },

  next: {
    type: String,
    default: null
  },

  currentPage: {
    type: Number,
    default: 1
  }

})

defineEmits([

  'previous',

  'next'

])

const showPagination = computed(() => {

  return props.previous || props.next

})

</script>

<style scoped>

.pagination{

    display:flex;

    justify-content:center;

    align-items:center;

    gap:20px;

    margin-top:25px;

}

.btn{

    background:#1976d2;

    color:white;

    border:none;

    padding:10px 18px;

    border-radius:6px;

    cursor:pointer;

    transition:.2s;

}

.btn:hover:not(:disabled){

    background:#1565c0;

}

.btn:disabled{

    background:#bdbdbd;

    cursor:not-allowed;

}

.page{

    font-weight:bold;

    color:#444;

}

</style>