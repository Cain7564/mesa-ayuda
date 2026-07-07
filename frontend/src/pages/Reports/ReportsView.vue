<template>

  <div class="reports-page">

    <PageHeader title="Reportes" />

    <div class="grid">

      <div class="card">

        <h2>🎫 Tickets por Estado</h2>

        <div class="item">

          <span>🟢 Abiertos</span>

          <strong>{{ reporte.tickets_abiertos }}</strong>

        </div>

        <div class="item">

          <span>🟡 En proceso</span>

          <strong>{{ reporte.tickets_proceso }}</strong>

        </div>

        <div class="item">

          <span>🔴 Cerrados</span>

          <strong>{{ reporte.tickets_cerrados }}</strong>

        </div>

      </div>

      <div class="card">

        <h2>🔥 Tickets por Prioridad</h2>

        <div class="item">

          <span>🔴 Alta</span>

          <strong>{{ reporte.tickets_alta }}</strong>

        </div>

        <div class="item">

          <span>🟡 Media</span>

          <strong>{{ reporte.tickets_media }}</strong>

        </div>

        <div class="item">

          <span>🟢 Baja</span>

          <strong>{{ reporte.tickets_baja }}</strong>

        </div>

      </div>

      <div class="card">

        <h2>💻 Inventario</h2>

        <div class="item">

          <span>🟢 Activos</span>

          <strong>{{ reporte.equipos_activos }}</strong>

        </div>

        <div class="item">

          <span>🟠 En reparación</span>

          <strong>{{ reporte.equipos_reparacion }}</strong>

        </div>

        <div class="item">

          <span>🔵 En mantenimiento</span>

          <strong>{{ reporte.equipos_mantenimiento }}</strong>

        </div>

        <div class="item">

          <span>🔴 Baja</span>

          <strong>{{ reporte.equipos_baja }}</strong>

        </div>

      </div>

      <div class="card">

        <h2>🖥 Equipos por Tipo</h2>

        <div class="item">

          <span>PC</span>

          <strong>{{ reporte.pc }}</strong>

        </div>

        <div class="item">

          <span>Laptop</span>

          <strong>{{ reporte.laptop }}</strong>

        </div>

        <div class="item">

          <span>Monitor</span>

          <strong>{{ reporte.monitor }}</strong>

        </div>

        <div class="item">

          <span>Impresora</span>

          <strong>{{ reporte.impresora }}</strong>

        </div>

      </div>

    </div>

  </div>

</template>

<script setup>

import { ref, onMounted } from 'vue'

import PageHeader from '../../components/PageHeader.vue'

import { getReporteGeneral } from '../../services/reports'

const reporte = ref({

    tickets_abiertos:0,

    tickets_proceso:0,

    tickets_cerrados:0,

    tickets_alta:0,

    tickets_media:0,

    tickets_baja:0,

    equipos_activos:0,

    equipos_reparacion:0,

    equipos_mantenimiento:0,

    equipos_baja:0,

    pc:0,

    laptop:0,

    monitor:0,

    impresora:0

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

.grid{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(350px,1fr));

    gap:25px;

}

.card{

    background:white;

    border-radius:10px;

    padding:25px;

    box-shadow:0 4px 15px rgba(0,0,0,.08);

}

.card h2{

    margin-top:0;

    margin-bottom:20px;

    color:#1976d2;

}

.item{

    display:flex;

    justify-content:space-between;

    padding:10px 0;

    border-bottom:1px solid #eee;

}

.item:last-child{

    border-bottom:none;

}

.item strong{

    color:#1976d2;

}

</style>