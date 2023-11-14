<template>
  <img @click="state.count += 1" :src="imageFile" />
  <p>Pets received: {{ state.count }}</p>
</template>

<script setup>
const props = defineProps(['imageFile']);
const state = reactive({
  count: 0,
});
</script>
