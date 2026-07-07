<template>

  <div class="reports-page">

    <PageHeader title="Reportes" />

    <div class="cards">

      <div class="card">

        <h3>Usuarios</h3>

        <span>{{ reporte.usuarios }}</span>

      </div>

      <div class="card">

        <h3>Técnicos</h3>

        <span>{{ reporte.tecnicos }}</span>

      </div>

      <div class="card">

        <h3>Tickets</h3>

        <span>{{ reporte.tickets }}</span>

      </div>

      <div class="card">

        <h3>Equipos</h3>

        <span>{{ reporte.equipos }}</span>

      </div>

    </div>

    <div class="sections">

      <div class="section">

        <h2>Tickets</h2>

        <p>🟢 Abiertos: {{ reporte.tickets_abiertos }}</p>

        <p>🟡 En proceso: {{ reporte.tickets_proceso }}</p>

        <p>🔴 Cerrados: {{ reporte.tickets_cerrados }}</p>

      </div>

      <div class="section">

        <h2>Inventario</h2>

        <p>🟢 Activos: {{ reporte.equipos_activos }}</p>

        <p>🟠 En reparación: {{ reporte.equipos_reparacion }}</p>

        <p>🔵 En mantenimiento: {{ reporte.equipos_mantenimiento }}</p>

        <p>🔴 Dados de baja: {{ reporte.equipos_baja }}</p>

      </div>

    </div>

  </div>

</template>

<script setup>

import { ref, onMounted } from 'vue'

import PageHeader from '../../components/PageHeader.vue'

import { getReporteGeneral } from '../../services/reports'

const reporte = ref({

    usuarios:0,

    tecnicos:0,

    tickets:0,

    equipos:0,

    tickets_abiertos:0,

    tickets_proceso:0,

    tickets_cerrados:0,

    equipos_activos:0,

    equipos_reparacion:0,

    equipos_mantenimiento:0,

    equipos_baja:0

})

const cargarReporte = async () => {

    try{

        reporte.value = await getReporteGeneral()

    }

    catch(error){

        console.error(error)

    }

}

onMounted(()=>{

    cargarReporte()

})

</script>

<style scoped>

.reports-page{

    padding:20px;

}

.cards{

    display:grid;

    grid-template-columns:repeat(4,1fr);

    gap:20px;

    margin-bottom:30px;

}

.card{

    background:white;

    border-radius:10px;

    padding:25px;

    box-shadow:0 3px 10px rgba(0,0,0,.08);

    text-align:center;

}

.card h3{

    margin:0;

    color:#666;

}

.card span{

    display:block;

    margin-top:15px;

    font-size:32px;

    font-weight:bold;

    color:#1976d2;

}

.sections{

    display:grid;

    grid-template-columns:1fr 1fr;

    gap:25px;

}

.section{

    background:white;

    padding:25px;

    border-radius:10px;

    box-shadow:0 3px 10px rgba(0,0,0,.08);

}

.section h2{

    margin-top:0;

    margin-bottom:20px;

}

.section p{

    font-size:16px;

    margin:12px 0;

}

@media(max-width:900px){

    .cards{

        grid-template-columns:1fr 1fr;

    }

    .sections{

        grid-template-columns:1fr;

    }

}

</style>