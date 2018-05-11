<template>
  <header id="top">
    <ul>
      <li>
        <router-link :to="{path: '/'}" class="no-botterm"><img src="../../assets/home.svg">Home</router-link>
      </li>
      <li>
        <router-link :to="{path: '/axis'}" class="no-botterm"><img src="../../assets/archive.svg">Axis</router-link>
      </li>
      <!--<li><a  class="no-botterm"><img src="../../assets/tags.svg" alt="">Tags</a></li>-->
      <li>
        <router-link :to="{path: '/about'}" class="no-botterm"><img src="../../assets/@.svg">About</router-link>
      </li>
      <li><a href="https://github.com/buglan" class="no-botterm"><img src="../../assets/github.svg">Github</a></li>
      <li>
        <router-link :to="{path: '/manage'}" class="no-botterm"><img src="../../assets/manager.svg">Manage</router-link>
      </li>
    </ul>
  </header>
</template>

<script>
  export default {

    name: "NavHeader",
    data() {
      return {}
    }
  }
</script>

<style scoped>

</style>
