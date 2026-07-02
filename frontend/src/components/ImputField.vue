<template>

  <div class="input-group">

    <label>{{ label }}</label>

    <input

      :type="type"

      :placeholder="placeholder"

      :value="modelValue"

      @input="$emit('update:modelValue', $event.target.value)"

    />

  </div>

</template>

<script setup>

defineProps({

    label:String,

    placeholder:String,

    modelValue:String,

    type:{

        type:String,

        default:'text'

    }

})

defineEmits([

    'update:modelValue'

])

</script>

<style scoped>

.input-group{

    display:flex;

    flex-direction:column;

    gap:5px;

}

label{

    font-weight:bold;

}

input{

    padding:10px;

    border:1px solid #ccc;

    border-radius:6px;

}

</style>