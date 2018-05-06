<template>
  <div>
    <NavHeader></NavHeader>
    <Msg></Msg>
  </div>
</template>

<script>
  import NavHeader from '@/components/index/NavHeader'
  import Msg from '@/components/about/Msg'

  export default {
    name: "About",
    components: {
      NavHeader, Msg
    }
  }
</script>

<style scoped>

</style>
