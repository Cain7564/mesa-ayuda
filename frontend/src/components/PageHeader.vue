<template>

  <div class="header">

    <h1>{{ title }}</h1>

    <slot />

  </div>

</template>

<script setup>

defineProps({

    title:String

})

</script>

<style scoped>

.header{

    display:flex;

    justify-content:space-between;

    align-items:center;

    margin-bottom:30px;

}

h1{

    margin:0;

}

</style>