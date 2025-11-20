<template>
  <button :class="{ negative: armed }" class="circular ui icon mini button" @click="toggle" @mouseleave="armed = false">
    <i class="icon small close"></i>
  </button>
</template>

<script setup lang="ts">

import { ref, defineEmits } from 'vue'

const armed = ref(false)

const emit = defineEmits<{
  remove: []
}>()

const toggle = async () => {
  if (armed.value) {
    emit('remove')
    armed.value = false
  }
  else {
    armed.value = !armed.value
  }
}

</script>
