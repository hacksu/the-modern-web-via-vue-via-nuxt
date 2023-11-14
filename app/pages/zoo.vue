<template>
  <div>
    <Animal v-for="animal in animals" :imageFile="animal" />
  </div>
</template>

<script setup>
const animals = ref([]);
$fetch('/api/loadzoo').then((res) => (animals.value = res));
</script>
