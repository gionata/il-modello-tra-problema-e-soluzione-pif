<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
  nome: {
    default: 'Gionata Massi',
  },
  affiliazione: {
    default: 'IIS Savoia Benincasa',
  },
  citta: {
    default: 'Ancona'
  },
  presentatore: {
    default: "no",
  }
})

const nome = ref(props.nome);
const affiliazione = ref(props.affiliazione);
const citta = ref(props.citta);
const presentatore = props.presentatore == "no" ? false : true;
</script>

<template>
  <div>
    <b>
      {{ nome }}
    </b><span v-if="presentatore"><sup>*</sup></span><br>
    <i>{{ affiliazione }}, {{ citta }}</i>
  </div>
</template>

<style lang="css" scoped>
div {
  margin: 10px auto;
  text-align: center;
  color: rgb(101, 102, 92);
  font-size: 1.2rem;
}
</style>
