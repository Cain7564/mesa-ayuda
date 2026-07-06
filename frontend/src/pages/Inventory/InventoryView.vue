<template>

  <div class="inventory-page">

    <PageHeader title="Inventario">

      <div class="actions">

        <InputField
          v-model="busqueda"
          label="Buscar"
          placeholder="Buscar equipo..."
        />

        <div class="filter">

          <label>Tipo</label>

          <select
            v-model="tipoSeleccionado"
            @change="cargarEquipos"
          >

            <option value="">
              Todos
            </option>

            <option value="PC">
              PC
            </option>

            <option value="LAPTOP">
              Laptop
            </option>

            <option value="MONITOR">
              Monitor
            </option>

            <option value="IMPRESORA">
              Impresora
            </option>

          </select>

        </div>

        <div class="filter">

          <label>Estado</label>

          <select
            v-model="estadoSeleccionado"
            @change="cargarEquipos"
          >

            <option value="">
              Todos
            </option>

            <option value="1">
              Activo
            </option>

            <option value="2">
              En reparación
            </option>

            <option value="3">
              Dado de baja
            </option>

            <option value="4">
              En mantenimiento
            </option>

          </select>

        </div>

        <div class="filter">

          <label>Ordenar</label>

          <select
            v-model="ordenSeleccionado"
            @change="cargarEquipos"
          >

            <option value="">
              Sin ordenar
            </option>

            <option value="codigo">
              Código (A-Z)
            </option>

            <option value="-codigo">
              Código (Z-A)
            </option>

            <option value="modelo">
              Modelo
            </option>

            <option value="tipo">
              Tipo
            </option>

          </select>

        </div>

        <PrimaryButton
          @click="abrirNuevoEquipo"
        >
          Nuevo Equipo
        </PrimaryButton>

      </div>

    </PageHeader>

    <DataTable
      :columns="columns"
      :rows="equipos.results"
      :showActions="true"
    >

      <template #actions="{ row }">

        <div class="buttons">

          <PrimaryButton
            @click="editarEquipo(row)"
          >
            Editar
          </PrimaryButton>

          <button
            class="delete-button"
            @click="eliminarEquipo(row.id)"
          >
            Eliminar
          </button>

        </div>

      </template>

    </DataTable>

    <Pagination
      :previous="equipos.previous"
      :next="equipos.next"
      :currentPage="currentPage"
      @previous="paginaAnterior"
      @next="siguientePagina"
    />

    <EquipoModal

      :visible="modalVisible"

      :title="modalTitle"

      :buttonText="buttonText"

      :equipo="equipoSeleccionado"

      @close="cerrarModal"

      @save="guardarEquipo"

    />

    <ConfirmDelete

      :visible="deleteDialogVisible"

      title="Eliminar equipo"

      message="¿Está seguro que desea eliminar este equipo?"

      @cancel="cancelarEliminar"

      @confirm="confirmarEliminar"

    />

  </div>

</template>
<style scoped>

.inventory-page{

    padding:20px;

}

.actions{

    display:flex;

    gap:20px;

    align-items:flex-end;

    flex-wrap:wrap;

}

.filter{

    display:flex;

    flex-direction:column;

}

.filter select{

    padding:10px;

    border:1px solid #ccc;

    border-radius:6px;

    min-width:170px;

    font-size:14px;

}

.buttons{

    display:flex;

    gap:10px;

}

.delete-button{

    background:#dc3545;

    color:white;

    border:none;

    padding:10px 15px;

    border-radius:6px;

    cursor:pointer;

    transition:.2s;

}

.delete-button:hover{

    background:#bb2d3b;

}

</style>