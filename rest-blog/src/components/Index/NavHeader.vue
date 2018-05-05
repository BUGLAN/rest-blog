<template>
  <header id="top">
    <ul>
      <li><router-link :to="{path: '/'}"  class="no-botterm"><img src="../../assets/home.svg" alt="">Home</router-link></li>
      <li><a  class="no-botterm"><img src="../../assets/archive.svg" alt="">Axis</a></li>
      <li><a  class="no-botterm"><img src="../../assets/tags.svg" alt="">Tags</a></li>
      <li><a  class="no-botterm"><img src="../../assets/about.svg" alt="">About</a></li>
      <li><a href="https://github.com/buglan" class="no-botterm"><img src="../../assets/github.svg" alt="">Github</a></li>
    </ul>
  </header>
</template>

<script>
  export default {

    name: "NavHeader",
    data () {
      return {
      }
  }}
</script>

<style scoped>

</style>
