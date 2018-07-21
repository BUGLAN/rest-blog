<template>
  <div>
    <NavHeader></NavHeader>
    <TimeAxis></TimeAxis>
  </div>

</template>

<script>
import NavHeader from '@/components/index/NavHeader'
import TimeAxis from '@/components/axis/TimeAxis'
export default {
  name: "Axis",
  components: {NavHeader, TimeAxis},
}
</script>

<style scoped>

</style>
