<template>
  <div>
    <NavHeader></NavHeader>
    <router-view></router-view>
    <navFooter ></navFooter>
  </div>
</template>

<script>
  import NavHeader from '@/components/index/NavHeader'
  import NavFooter from '@/components/index/NavFooter'

  export default {
    name: "Home",
    components: {NavHeader, NavFooter}
  }
</script>

<style scoped>

</style>
