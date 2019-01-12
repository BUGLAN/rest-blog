<template>
  <div v-title="title">
    <keep-alive>
      <NavHeader></NavHeader>
    </keep-alive>
    <router-view></router-view>
    <navFooter ></navFooter>
  </div>
</template>

<script>
import NavHeader from '@/components/NavHeader'
import NavFooter from '@/components/NavFooter'

export default {
  name: 'Home',
  components: { NavHeader, NavFooter },
  data () {
    return {
      'title': '首页 | BUGLAN的个人小站'
    }
  }
}
</script>

<style scoped>

</style>
