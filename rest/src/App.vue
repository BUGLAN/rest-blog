<template>
  <div>
    <div class="main">
      <router-view></router-view>
    </div>
    <keep-alive>
      <Footer></Footer>
    </keep-alive>
  </div>
</template>

<script>
import Footer from '@/components/Footer'
export default {
  name: 'App',
  components: { Footer }
}
</script>
<style>
@import './assets/css/main.css'
</style>
