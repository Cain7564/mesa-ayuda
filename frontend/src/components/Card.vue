<template>

  <div class="card">

    <h3>{{ titulo }}</h3>

    <p>{{ valor }}</p>

  </div>

</template>

<script setup>

defineProps({

  titulo: String,

  valor: [String, Number]

})

</script>

<style scoped>

.card{

    background:white;

    padding:20px;

    border-radius:10px;

    box-shadow:0 0 10px rgba(0,0,0,.1);

    text-align:center;

}

.card h3{

    margin-bottom:15px;

    color:#1976d2;

}

.card p{

    font-size:32px;

    font-weight:bold;

    margin:0;

}

</style>