<template>
  <div class="login-container">
    <div class="login-card">
      <h1>Mesa de Ayuda</h1>

      <h2>Iniciar Sesión</h2>

      <form @submit.prevent="login">
        <div class="form-group">
          <label>Usuario</label>

          <input
            v-model="username"
            type="text"
            placeholder="Ingrese su usuario"
            required
          />
        </div>

        <div class="form-group">
          <label>Contraseña</label>

          <input
            v-model="password"
            type="password"
            placeholder="Ingrese su contraseña"
            required
          />
        </div>

        <button type="submit">
          Ingresar
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useRouter } from 'vue-router'

import api from '../../services/api'

const router = useRouter()

const username = ref('')
const password = ref('')

const login = async () => {

  try {

    const response = await api.post('token/', {

      username: username.value,

      password: password.value,

    })

    console.log(response.data)

    localStorage.setItem(
      'access',
      response.data.access
    )

    localStorage.setItem(
      'refresh',
      response.data.refresh
    )

    alert('Inicio de sesión exitoso.')

    router.push('/dashboard')

  } catch (error) {

    console.error(error)

    alert('Usuario o contraseña incorrectos.')

  }

}

</script>

<style scoped>

.login-container {

  display: flex;

  justify-content: center;

  align-items: center;

  height: 100vh;

  background: #f4f6f9;

}

.login-card {

  background: white;

  width: 400px;

  padding: 30px;

  border-radius: 10px;

  box-shadow: 0 0 15px rgba(0,0,0,.15);

}

h1 {

  text-align: center;

  margin-bottom: 10px;

}

h2 {

  text-align: center;

  margin-bottom: 30px;

  color: #666;

}

.form-group {

  margin-bottom: 20px;

}

label {

  display: block;

  margin-bottom: 5px;

}

input {

  width: 100%;

  padding: 10px;

  border: 1px solid #ccc;

  border-radius: 5px;

  box-sizing: border-box;

}

button {

  width: 100%;

  padding: 12px;

  border: none;

  border-radius: 5px;

  background: #1976d2;

  color: white;

  font-size: 16px;

  cursor: pointer;

}

button:hover {

  background: #1565c0;

}

</style>