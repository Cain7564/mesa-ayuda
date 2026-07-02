<template>
  <div class="dashboard">

    <h1>Dashboard</h1>

    <div v-if="loading">
      <p>Cargando información...</p>
    </div>

    <div v-else class="cards">

      <div class="card">
        <h3>👥 Usuarios</h3>
        <p>{{ dashboard.usuarios }}</p>
      </div>

      <div class="card">
        <h3>👨‍🔧 Técnicos</h3>
        <p>{{ dashboard.tecnicos }}</p>
      </div>

      <div class="card">
        <h3>🎫 Tickets</h3>
        <p>{{ dashboard.tickets_total }}</p>
      </div>

      <div class="card">
        <h3>💻 Equipos</h3>
        <p>{{ dashboard.equipos_total }}</p>
      </div>

      <div class="card">
        <h3>🟢 Tickets Abiertos</h3>
        <p>{{ dashboard.tickets_abiertos }}</p>
      </div>

      <div class="card">
        <h3>🟡 En Proceso</h3>
        <p>{{ dashboard.tickets_en_proceso }}</p>
      </div>

      <div class="card">
        <h3>✅ Tickets Cerrados</h3>
        <p>{{ dashboard.tickets_cerrados }}</p>
      </div>

      <div class="card">
        <h3>🖥 Equipos Activos</h3>
        <p>{{ dashboard.equipos_activos }}</p>
      </div>

      <div class="card">
        <h3>🛠 En Reparación</h3>
        <p>{{ dashboard.equipos_reparacion }}</p>
      </div>

      <div class="card">
        <h3>⚙ En Mantenimiento</h3>
        <p>{{ dashboard.equipos_mantenimiento }}</p>
      </div>

    </div>

  </div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import api from '../../services/api'

const loading = ref(true)

const dashboard = ref({})

const cargarDashboard = async () => {

  try {

    const token = localStorage.getItem('access')

    const response = await api.get('dashboard/general/', {

      headers: {

        Authorization: `Bearer ${token}`

      }

    })

    dashboard.value = response.data

  } catch (error) {

    console.error(error)

  } finally {

    loading.value = false

  }

}

onMounted(() => {

  cargarDashboard()

})

</script>

<style scoped>

.dashboard{

    padding:20px;

}

.cards{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

    gap:20px;

    margin-top:30px;

}

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