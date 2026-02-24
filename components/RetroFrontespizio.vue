<script setup lang="ts">
import Autori from './Autori.vue';
import Piede from './Piede.vue';
import Titolo from './Titolo.vue';
</script>

<template>
  <div class="slidev-layout cover">
    <div class="my-auto w-full">
      <Titolo />
      <Autori />
      <!-- Aggiungere automazione zoom in e poi out -->
      <div text-center text-5xl>Grazie per l'attenzione!</div>
      <!-- Aggiungere automazione zoom out e poi in -->
      <div text-center text-4xl>Domande?</div>
    </div>
  </div>
  <Piede />
</template>

<style lang="css" scoped></style>
