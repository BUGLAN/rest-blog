<template>
  <div>
    <NavHeader></NavHeader>
    <Msg></Msg>
  </div>
</template>

<script>
import NavHeader from '@/components/NavHeader'
import Msg from '@/components/Msg'

export default {
  name: 'About',
  components: {
    NavHeader, Msg
  }
}
</script>

<style scoped>

</style>
