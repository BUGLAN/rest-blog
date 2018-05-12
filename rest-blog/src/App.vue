<template>
  <div>
    <router-view></router-view>
    <keep-alive>
    <Footer></Footer>
    </keep-alive>
  </div>
</template>

<script>
  import Footer from '@/components/all/Footer'
  export default {
    name: "App",
    components: {Footer}
  }
</script>
<style>
  @import "../static/css/main.css";
</style>
