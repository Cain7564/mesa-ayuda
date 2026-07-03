<template>

  <table class="table">

    <thead>

      <tr>

        <th
          v-for="column in columns"
          :key="column.key"
        >

          {{ column.label }}

        </th>

        <th v-if="showActions">

          Acciones

        </th>

      </tr>

    </thead>

    <tbody>

      <tr
        v-for="row in rows"
        :key="row.id"
      >

        <td
          v-for="column in columns"
          :key="column.key"
        >

          <!-- Estado -->

          <template v-if="column.key === 'estado'">

            <span
              class="badge"
              :class="estadoClass(row.estado)"
            >

              {{ row.estado }}

            </span>

          </template>

          <!-- Prioridad -->

          <template v-else-if="column.key === 'prioridad'">

            <span
              class="badge"
              :class="prioridadClass(row.prioridad)"
            >

              {{ row.prioridad }}

            </span>

          </template>

          <!-- Fecha -->

          <template v-else-if="column.key === 'fecha'">

            {{ formatearFecha(row.fecha) }}

          </template>

          <!-- Valor normal -->

          <template v-else>

            {{ row[column.key] }}

          </template>

        </td>

        <td v-if="showActions">

          <slot
            name="actions"
            :row="row"
          />

        </td>

      </tr>

    </tbody>

  </table>

</template>

<script setup>

defineProps({

  columns: Array,

  rows: Array,

  showActions:{

    type:Boolean,

    default:false

  }

})

const prioridadClass = (prioridad) => {

  switch(prioridad){

    case 'Alta':

      return 'danger'

    case 'Media':

      return 'warning'

    case 'Baja':

      return 'success'

    default:

      return ''

  }

}

const estadoClass = (estado) => {

  switch(estado){

    case 'Abierto':

      return 'success'

    case 'En proceso':

      return 'warning'

    case 'Cerrado':

      return 'secondary'

    default:

      return ''

  }

}

const formatearFecha = (fecha) => {

  if(!fecha){

    return ''

  }

  return new Date(fecha).toLocaleString()

}

</script>

<style scoped>

.table{

    width:100%;

    border-collapse:collapse;

    background:white;

    border-radius:10px;

    overflow:hidden;

    box-shadow:0 2px 8px rgba(0,0,0,.08);

}

th{

    background:#1976d2;

    color:white;

    padding:14px;

    text-align:left;

}

td{

    padding:14px;

    border-bottom:1px solid #eee;

}

tr:hover{

    background:#f8f9fa;

}

.badge{

    padding:6px 12px;

    border-radius:20px;

    color:white;

    font-size:13px;

    font-weight:bold;

}

.success{

    background:#28a745;

}

.warning{

    background:#ffc107;

    color:#333;

}

.danger{

    background:#dc3545;

}

.secondary{

    background:#6c757d;

}

</style>