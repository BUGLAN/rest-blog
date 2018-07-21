<template>
  <div>
    <NavHeader></NavHeader>
    <router-view></router-view>
  </div>
</template>

<script>
import NavHeader from '@/components/index/NavHeader'
export default {
  name: "BasicManager",
  components: {NavHeader}
}
</script>

<style scoped>

</style>
