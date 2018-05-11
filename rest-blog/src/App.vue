<template>
  <div>
    <router-view></router-view>
    <Footer></Footer>
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
