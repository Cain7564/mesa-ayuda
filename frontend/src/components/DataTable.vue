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

          {{ row[column.key] }}

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

</script>

<style scoped>

.table{

    width:100%;

    border-collapse:collapse;

}

th{

    background:#1976d2;

    color:white;

    padding:12px;

}

td{

    padding:12px;

    border-bottom:1px solid #ddd;

}

</style>