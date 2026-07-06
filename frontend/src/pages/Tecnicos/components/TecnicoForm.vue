<template>

  <form class="tecnico-form" @submit.prevent="submitForm">

    <InputField
      label="Nombre"
      placeholder="Ingrese el nombre"
      v-model="form.nombre"
    />

    <InputField
      label="Especialidad"
      placeholder="Ingrese la especialidad"
      v-model="form.especialidad"
    />

    <div class="buttons">

      <PrimaryButton type="submit">

        {{ buttonText }}

      </PrimaryButton>

    </div>

  </form>

</template>

<script setup>

import { reactive, watch } from 'vue'

import InputField from '../../../components/InputField.vue'
import PrimaryButton from '../../../components/PrimaryButton.vue'

const props = defineProps({

    tecnico:{

        type:Object,

        default:null

    },

    buttonText:{

        type:String,

        default:'Guardar'

    }

})

const emit = defineEmits([

    'save'

])

const form = reactive({

    nombre:'',

    especialidad:''

})

watch(

    ()=>props.tecnico,

    (nuevo)=>{

        if(nuevo){

            form.nombre=nuevo.nombre

            form.especialidad=nuevo.especialidad

        }

        else{

            form.nombre=''

            form.especialidad=''

        }

    },

    {

        immediate:true

    }

)

const submitForm=()=>{

    emit('save',{

        ...form

    })

}

</script>

<style scoped>

.tecnico-form{

    display:flex;

    flex-direction:column;

    gap:20px;

}

.buttons{

    display:flex;

    justify-content:flex-end;

}

</style>