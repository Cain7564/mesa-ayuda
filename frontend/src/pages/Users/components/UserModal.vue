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