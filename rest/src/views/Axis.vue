<template>
  <div>
    <NavHeader></NavHeader>
    <TimeAxis></TimeAxis>
  </div>

</template>

<script>
import NavHeader from '@/components/NavHeader'
import TimeAxis from '@/components/TimeAxis'
export default {
  name: 'Axis',
  components: { NavHeader, TimeAxis }
}
</script>

<style scoped>

</style>
